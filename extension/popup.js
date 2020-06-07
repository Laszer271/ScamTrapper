/*
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
*/

document.addEventListener('DOMContentLoaded', function () {
    const bg = chrome.extension.getBackgroundPage()
    const treshold = 50;
    Object.keys(bg.scams).forEach(function (url) {
        if (bg.scams[url] >= treshold) {
            const div = document.createElement('div')
            div.textContent = `${url}: ${bg.scams[url]}`
            document.body.appendChild(div)
            /*
            chrome.identity.getAuthToken({ 'interactive': true }, function (token) {
                if (token === undefined) {
                    console.log('Error authenticating with Google Drive');
                } else {
                    gapi.load('client', function () {
                        gapi.client.setToken({ access_token: token });
                        gapi.client.load('drive', 'v3', function () {
                            gapi.client.load('sheets', 'v4', function () {
                                console.log(url)
                                var sheetId = '1LX6erktlVPWjmqkUU1zD5VEPrawy6rF575mi7Ujv-EU'
                                appendToSheet(sheetId, url).then();
                            });
                        });
                    });
                }
            });
            */
        }
    })

    /*
    document.querySelector('button').addEventListener('click', onclick, false)

    function onclick() {
        chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
            //let a = document.createElement('a');
            //let csvContent = "data:text/csv;charset=utf-8,";
            //csvContent += funkcja(bg.scams["links"]);
            //a.href = "data:application/octet-stream," + encodeURIComponent(bg.scams["links"]);
            //a.download = 'url.txt';
            //a.click();
            //var encodedUri = encodeURI(csvContent);
            //window.open(encodedUri);

            writeReport(".\links.csv", funkcja(bg.scams["links"]))
        })
    }

    function writeReport(path, reportText) {

        var reportFile = new File([""], path);

        console.log(reportText);
        reportFile.open("a");
        reportFile.write(reportText + ",\n");
        reportFile.close();

    }

    function funkcja(rowArray) {
        let row = rowArray.join(",\n");
        csvContent = row + "\r\n";
        return csvContent;
    }

    function setCount(res) {
        const div = document.createElement('div')
        div.textContent = `${res.count} bears`
        document.body.appendChild(div)
    }
    */
}, false)

