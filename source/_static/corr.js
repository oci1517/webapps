var corrections = document.getElementsByClassName('admonition-adm-corrige'); // variable globale

function get_title(element) {
	return element.getElementsByClassName('admonition-title')[0];
}

function showHandler(n) { 
	return function() { 
		show(n); 
	}
}

function hideHandler(n) { 
	return function() { 
		hide(n); 
	}
}

function hide(n) {
	corrections[n].style.marginBottom = '24px';
	var title = get_title(corrections[n]);
	title.innerHTML = 'Corrigé (cliquer pour afficher)';
	title.onclick = showHandler(n);
	var next = title.nextElementSibling;
	while (next != null) {
		if (typeof(next.style) !== 'undefined') {
			next.style.display = 'none';
		}
		next = next.nextElementSibling;
	}
}

function show(n) {
	corrections[n].style.marginBottom = '';
	var title = get_title(corrections[n]);
	title.innerHTML = 'Corrigé (cliquer pour masquer)';
	title.onclick = hideHandler(n);
	var next = title.nextElementSibling;
	while (next !== null) {
		next.style.display = 'block';
		next = next.nextElementSibling;
	}
}

function main() {
	for (var i = 0; i < corrections.length; i++) {
		var title = get_title(corrections[i]);
		title.style.backgroundColor = 'rgb(26,188,156)';
		title.style.cursor = 'pointer';
		hide(i);
	}
}

main();