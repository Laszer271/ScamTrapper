document.addEventListener('DOMContentLoaded', function () {
    const bg = chrome.extension.getBackgroundPage()
    const treshold = 50;
    Object.keys(bg.scams).forEach(function (url) {
        if (bg.scams[url] >= treshold) {
            const div = document.createElement('div')
            div.textContent = `${url}: ${bg.scams[url]}`
            document.body.appendChild(div)
        }
    })
}, false)

