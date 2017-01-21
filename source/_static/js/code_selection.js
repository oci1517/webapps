// Extension purement JS développée par Samuel Fringeli
// (https://bitbucket.org/samuel_fringeli/sphinx-code-selection/src)


function getRandomId() {
    return Math.random().toString(36).substr(2, 5);
}

function selectText(elementId) {
    var text = document.getElementById(elementId);

    if (document.body.createTextRange) {
        var range = document.body.createTextRange();
        range.moveToElementText(text);
        range.select();
    }

    else if (window.getSelection) {
        var selection = window.getSelection();
        var range = document.createRange();
        range.selectNodeContents(text);
        selection.removeAllRanges();
        selection.addRange(range);
    }
}

function goToParentNode(element, n) {
    for (var i = 0; i < n; i++) {
        element = element.parentNode;
    }
    return element;
}

function main() {
    var preBlocks = document.getElementsByTagName('pre');
    var hasLines = false;

    for (var i = 0; i < preBlocks.length; i++) {
        var preBlock = preBlocks[i]

        if (preBlock.parentNode.className !== 'linenodiv') {
            if (hasLines) {
                var codeBlockDiv = goToParentNode(preBlock, 6);
                hasLines = false;
            }
            else {
                var codeBlockDiv = goToParentNode(preBlock, 2);
            }
            var mainDiv = codeBlockDiv.parentNode;

            var randomId = getRandomId();
            preBlock.id = randomId;

            var selectButton = document.createElement('a');
            var selectButtonText = document.createTextNode("Sélectionner ce code : Ctrl+C / Ctrl+V pour copier / coller dans TigerJython");
            selectButton.appendChild(selectButtonText);

            selectButton.style.position = 'relative';
            selectButton.style.bottom = '24px';
            selectButton.style.left = '2px';

            selectButton.onmouseover = function() {
                this.style.textDecoration = 'underline';
                this.style.color = '#2980B9';
            }
            selectButton.onmouseleave = function() {
                this.style.textDecoration = '';
            }

            selectButton.setAttribute('onclick', 'selectText("'+randomId+'")');
            mainDiv.insertBefore(selectButton, codeBlockDiv.nextSibling);
        }
        else {
            hasLines = true;
        }
    }
}

$(function () {
    main();
    console.log("lancé extension copie du code");
});
