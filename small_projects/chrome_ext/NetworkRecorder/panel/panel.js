
// document.getElementById("start").addEventListener("click", change);
document.getElementById("insertText").addEventListener("click", addRowWithText);
document.getElementById("recButton").addEventListener("click", recClick);
document.getElementById("btnClear").addEventListener("click", clearRows);

// function change() // no ';' here
// {
//     if (this.value == "Start") {
//         this.value = "Stop"
//         chrome.devtools.network.onRequestFinished.addListener(listner)
//     }
//     else {
//         this.value = "Start";
//         chrome.devtools.network.onRequestFinished.removeListener(listner)
//     }
// }

function clearRows() {
    tbl = document.getElementById('request_details')
    var rowCount = tbl.rows.length;
    for (var i = rowCount - 1; i > 0; i--) {
        tbl.deleteRow(i);
    }
}

function addRowWithText() {
    table = document.getElementById('request_details')
    inputText = document.getElementById("step")
    rowCount = table.rows.length;
    cellCount = table.rows[0].cells.length;
    row = table.insertRow(rowCount);
    cell = row.insertCell(0)
    cell.colSpan = "5"
    cell.innerHTML = inputText.value

    inputText.value = ''
}

function recClick() {
    console.log("*************** inside recClick")
    recLabel = document.getElementById('lblRecord')

    if (this.classList.contains('notRec')) {
        this.classList.remove('notRec')
        this.classList.add('Rec')
        recLabel.innerHTML = "Recording..."
        chrome.devtools.network.onRequestFinished.addListener(listner)
    }
    else {
        this.classList.remove('Rec')
        this.classList.add('notRec')
        recLabel.innerHTML = "Record Steps"
        chrome.devtools.network.onRequestFinished.removeListener(listner)
    }
}


function listner(request) {
    console.log(request.request.method)
    console.log("URL", request.request.url)
    console.log(request.response.headers)

    whiteList = ['text/html', 'application/json']

    lstContentType = request.response.headers.filter((headerObj) => {
        return headerObj.name === 'Content-Type'
    })

    contentType = lstContentType[0].value
    console.log("CONTENT TYPE", contentType)

    for (value of whiteList) {
        if (contentType.includes(value)) {
            addRow(request, contentType)
        }
    }
}

function addRow(request, contentType) {
    table = document.getElementById('request_details')
    rowCount = table.rows.length;
    cellCount = table.rows[0].cells.length;
    row = table.insertRow(rowCount);

    cell = row.insertCell(0)
    cell.innerHTML = request.request.method

    cell = row.insertCell(1)
    cell.innerHTML = request.request.url

    url = new URL(request.request.url)
    console.log(url.pathname)

    cell = row.insertCell(2)
    cell.innerHTML = url.pathname

    cell = row.insertCell(3)
    cell.innerHTML = url.search

    cell = row.insertCell(4)
    cell.innerHTML = contentType
}


// window.onload = function (event) {
//     chrome.runtime.sendMessage({
//         command: "sendToConsole",
//         tabId: chrome.devtools.inspectedWindow.tabId,
//         args: "It worked"
//     });
// }