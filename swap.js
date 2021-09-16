// author: xetra11
// https://github.com/xetra11

{   
    function htmlToElement(html) {
        var template = document.createElement('template');
        html = html.trim();
        template.innerHTML = html;
        return template.content.firstChild;
    }

    const swap = function(nodeA, nodeB) {
        const parentA = nodeA.parentNode;
        const siblingA = nodeA.nextSibling === nodeB ? nodeA : nodeA.nextSibling;

        // Move `nodeA` to before the `nodeB`
        nodeB.parentNode.insertBefore(nodeA, nodeB);

        // Move `nodeB` to before the sibling of `nodeA`
        parentA.insertBefore(nodeB, siblingA);
    };

    const neighborButtonNode = document.body.querySelector(".btn.ml-2.d-none.d-md-block")
    const swapButtonNode = htmlToElement('<a class="btn ml-2 d-none d-md-block swap-button" href>Swap View</a>')

    swapButtonNode.addEventListener("click", (event) => { 
        event.preventDefault()
        event.stopPropagation()
        const readmeNode = document.body.querySelector("#readme")
        const codeNode = document.body.querySelector(".Box.mb-3")
        swap(readmeNode, codeNode)
    })

    neighborButtonNode.parentNode.insertBefore(swapButtonNode, neighborButtonNode)
}
