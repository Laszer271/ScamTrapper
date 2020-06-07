
function appendToSheet(sheetId, url) {
    var appendParams = {
        'spreadsheetId': sheetId,
        'range': 'A:A',
        'valueInputOption': 'RAW',
    };
    var valueRangeBody = {
        'majorDimension': 'ROWS',
        'values': [
            [url, 'scam']
        ]
    };
    return gapi.client.sheets.spreadsheets.values.append(appendParams, valueRangeBody);
}

//links = [];
window.scams = {}
const treshold = 50;
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    u = request.url
    window.scams[request.url] = request.count
    window.scams["frazy"] = request.f
    if (window.scams[request.url] >= treshold) {
        alert("Scam alert!!!")

        //let a = document.createElement('a');
        //let csvContent = "data:text/csv;charset=utf-8,";
        //a.href = "data:application/octet-stream," + encodeURIComponent(u);
        //a.download = 'url.txt';
        //a.click();
        chrome.identity.getAuthToken({ 'interactive': true }, function (token) {

            if (token === undefined) {
                console.log('Error authenticating with Google Drive');
            } else {
                gapi.load('client', function () {
                    gapi.client.setToken({ access_token: token });
                    gapi.client.load('drive', 'v3', function () {

                        gapi.client.load('sheets', 'v4', function () {
                            var sheetId = '1LX6erktlVPWjmqkUU1zD5VEPrawy6rF575mi7Ujv-EU'
                            appendToSheet(sheetId, u).then();
                        });
                    });
                });
            }
        });
    }
})

//window.scams["links"] = links;

chrome.browserAction.onClicked.addListener(function (tab) {
    chrome.tabs.create({ url: 'popup.html' })
})

