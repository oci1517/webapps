#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 C�dric Donner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'cdonner'

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

from sphinx.util.compat import make_admonition

from sphinx.directives import code

from .sqltable import SQLTable



class ActiveSQL(Directive):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'fiddle' : directives.uri,
        'connection_string' : directives.unchanged,
        'no-output' : directives.flag,
        'no-query' : directives.flag,
        'corrige' : directives.flag
    }

    def run(self):
        ''' Cette fonction doit retourner une liste de noeuds '''

        env = self.state.document.settings.env
        app = env.app
        def show_output():
            return (not 'no-output' in self.options) or \
                ('corrige' in self.options) and app.config.sqlexos_output_corrige

        def show_query():
            return (not 'no-query' in self.options) or \
                ('corrige' in self.options) and app.config.sqlexos_query_corrige

        # si env.sql_default_connection_string n'a pas �t� d�finie dans une
        # directive sql-connection-config, il faut l'initialiser � la chaine vide
        if not hasattr(env, 'sql_default_connection_string'):
            env.sql_default_connection_string = ''

        res_nodes = []

        try:
            title = self.arguments[0]
        except:
            title = ''

        connection_string = self.options.get('connection_string',
            env.sql_default_connection_string)


        if 'fiddle' in self.options:
            fiddle_target = self.options.get('fiddle')
            res_nodes += [nodes.raw(
                    '',
                    '<div>Lien SQLFiddle : <a href="{t}">{t}</a></div>'.format(t=fiddle_target),
                    format='html') ]

        # �crire le code SQL si le flag no-query n'a pas �t� pass� lors de l'appel
        if show_query():
            # res_nodes += nodes.paragraph(text=u"Requête SQL : ")
            print("SQL affiché dans corrigé")
            res_nodes += code.CodeBlock(
                name=self.name, arguments=['sql'], options={},
                lineno=self.lineno,
                content_offset=self.content_offset,
                block_text=self.block_text,
                state=self.state,
                state_machine=self.state_machine,
                content = self.content
            ).run()

        # afficher le r�sultat de la requ�te si l'argument no_output n'est pas d�fini
        if show_output():
            # res_nodes += nodes.paragraph(text=u"Résultat de la requête : ")
            res_nodes += SQLTable(
                name=self.name, arguments=[''],
                options = {'connection_string' : connection_string},
                lineno=self.lineno,
                content_offset=self.content_offset,
                block_text=self.block_text,
                state=self.state,
                state_machine=self.state_machine,
                content = self.content
            ).run()


        #res_nodes += [nodes.paragraph(text='Lien SQLFiddle : ' + fiddle_target)]
        # res_nodes += [nodes.target('lien', '', ids=['lien'], refuri='http://www.google.com')]

        # res_nodes += make_admonition(fiddle_link_node, self.name, ['Lien SQLFiddle'], {}, [self.options.get('fiddle', '')],
        #                             self.lineno, self.content_offset,
        #                             self.block_text, self.state, self.state_machine)


        return res_nodes

class sqlexplain(nodes.Admonition, nodes.Element):
    pass

def visit_sqlexplain_node(self, node):
    self.visit_admonition(node)

def depart_sqlexplain_node(self, node):
    self.depart_admonition(node)

class SQLExplain(Directive):

    required_arguments = 0
    optional_arguments = 0

    has_content = True
    option_spec = {
        'fiddle' : directives.uri
    }

    def run(self):
        ''' Cette fonction doit retourner une liste de noeuds '''

        env = self.state.document.settings.env
        app = env.app

        res_nodes = []

        # ajouter l'admonition n�cessaire
        ad = make_admonition(sqlexplain, self.name, ['But de la requete'], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        return ad

class SQLConnectionConfig(Directive):

    required_arguments = 1
    optional_arguments = 0

    has_content = False

    def run(self):
        ''' Cette fonction doit retourner une liste de noeuds '''

        env = self.state.document.settings.env
        app = env.app



        try:
            env.sql_default_connection_string = self.arguments[0]
            app.info('Next SQL queries will be run against %s by default' % env.sql_default_connection_string)
        except:
            self.severe('No connection string passed as required argument')
            env.sql_default_connection_string = 'unknown database'

        return []


def setup(app):

    # indique s'il faut ou non afficher les requ�tes SQL des exercices (pour
    # les corrig�s)
    app.add_config_value('sqlexos_query_corrige', True, True)
    # indique s'il faut ou non afficher les r�sultats des requ�tes SQL des
    # exercices (pour les corrig�s)
    app.add_config_value('sqlexos_output_corrige', True, True)

    app.add_node(sqlexplain,
                 html=(visit_sqlexplain_node, depart_sqlexplain_node),
                 latex=(visit_sqlexplain_node, depart_sqlexplain_node),
                 text=(visit_sqlexplain_node, depart_sqlexplain_node))

    app.add_directive('sql', ActiveSQL)
    app.add_directive('sql-explain', SQLExplain)
    app.add_directive('butreq', SQLExplain)
    app.add_directive('sql-connection-config', SQLConnectionConfig)
    app.info('Initializing ActiveSQL')

    # app.add_stylesheet('codemirror.css')

    # app.add_javascript('jquery.highlight.js')
