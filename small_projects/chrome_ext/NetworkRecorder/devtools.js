console.log("Chrome Extension ...............")

chrome.devtools.panels.create(
    'Network Recorder',
    '',
    'panel/panel.html',
    null // no callback
);


