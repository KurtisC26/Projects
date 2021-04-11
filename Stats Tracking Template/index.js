var t = $('#possession-table').DataTable();
var counter = 1;
var index = 1;

$('#submit').on('click', function(e) {
    e.preventDefault();
    var date = $(".add-date").val();
    var pg = $(".add-pg").val();
    var sg = $(".add-sg").val();
    var sf = $(".add-sf").val();
    var pf = $(".add-pf").val();
    var c = $(".add-c").val();
    var opponent = $(".add-opponent").val();
    var arena = $(".add-arena").val();
    var start = $(".add-start").val();
    var play_call = $(".add-play-call").val();
    var passes = $(".add-passes").val();
    var movement = $(".add-movement").val();
    var shot_selection = $(".add-shot-selection").val();
    var quality = $(".add-shot-quality").val();
    var shot_result = $(".add-shot-result").val();
    var player = $(".add-player").val();

    t.row.add([
        date,
        pg,
        sg,
        sf,
        pf,
        c,
        opponent,
        arena,
        index,
        start,
        play_call,
        movement,
        passes,
        shot_selection,
        quality,
        shot_result,
        player
    ]).draw(false);
    index = index + 1;
    counter++;
});

function download_csv(csv, filename) {
    var csvFile;
    var downloadLink;
    csvFile = new Blob([csv], {type: "text/csv"});
    downloadLink = document.createElement("a");
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();
}

function export_table_to_csv(html, filename) {
	var csv = [];
	var rows = document.querySelectorAll("table tr");
    for (var i = 0; i < rows.length; i++) {
		var row = [], cols = rows[i].querySelectorAll("td, th");
        for (var j = 0; j < cols.length; j++)
            row.push(cols[j].innerText);
		csv.push(row.join(","));
	}
    download_csv(csv.join("\n"), filename);
}

document.querySelector(".myclass").addEventListener("click", function () {
    var html = document.querySelector("table").outerHTML;
	export_table_to_csv(html, "PBP_Stats.csv");
});
