function setInnerText(element, value) {
    if (element.innerText) {
        element.innerText = value;
    } else {
        element.textContent = value;
    }
}

function includeGadget(url) {
    const allowedGadgets = ["/static/gadget.js"]; // Whitelist of allowed gadgets
    if (!allowedGadgets.includes(url)) {
        setInnerText(document.getElementById("log"), "Invalid gadget.");
        return;
    }

    var scriptEl = document.createElement('script');
    scriptEl.src = url;

    scriptEl.onload = function() { 
        setInnerText(document.getElementById("log"), "Loaded gadget from " + url);
    }
    scriptEl.onerror = function() { 
        setInnerText(document.getElementById("log"), "Couldn't load gadget from " + url);
    }

    document.head.appendChild(scriptEl);
}

function getGadgetName() { 
    return window.location.hash.substr(1) || "/static/gadget.js";
}

function init() {
    includeGadget(getGadgetName());

    window.addEventListener("message", function(event) {
        if (event.source == parent) {
            includeGadget(getGadgetName());
        }
    }, false);
}
