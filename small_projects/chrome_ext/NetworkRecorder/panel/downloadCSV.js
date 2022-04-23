document.getElementById("downloadCSV").addEventListener("click", downloadCSVFile);

function tableToCSV() {
    var csv_data = [];

    var rows = document.getElementsByTagName('tr');
    if (rows.length <= 1) {
        throw new Error("Attempting Download before recording the URLs")
    }

    for (var i = 0; i < rows.length; i++) {

        var cols = rows[i].querySelectorAll('td,th');
        var csvrow = [];
        for (var j = 0; j < cols.length; j++) {

            csvrow.push(cols[j].innerHTML);
        }
        csv_data.push(csvrow.join(","));
    }
    csv_data = csv_data.join('\n');
    return csv_data

}

function downloadCSVFile() {
    try {
        csv_data = tableToCSV()
        CSVFile = new Blob([csv_data], { type: "text/csv" });

        // Create to temporary link to initiate
        // download process
        var temp_link = document.createElement('a');

        // Download csv file
        temp_link.download = "RecordedURLs.csv";
        var url = window.URL.createObjectURL(CSVFile);
        temp_link.href = url;

        // This link should not be displayed
        temp_link.style.display = "none";
        document.body.appendChild(temp_link);

        // Automatically click the link to trigger download
        temp_link.click();
        document.body.removeChild(temp_link);
    }
    catch (ex) {
        alert("Please Start recording the URLs before downloading")
    }
}