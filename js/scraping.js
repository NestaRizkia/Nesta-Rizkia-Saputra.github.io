
$(function() {
    // Mengambil data dari file json
    $.get('Data-Scraping/Data.json', function(obj) {
        // Tag tabel awal
        var str = "<table border=1>";
        // Judul tabel
        str += "<tr><td>No</td><td>Judul Berita</td><td>Kategori</td><td>waktu terbit</td><td>waktu scraping</td></tr>";
        // Looping data headline dengan fungsi $.each() Jquery
        $.each(obj, function(n, data) {
            // Isi tabel
            str += "<tr>";
            str += "<td>" + (n + 1) + "</td>";
            str += "<td>" + data.title + "</td>";
            str += "<td>" + data.category + "</td>";
            str += "<td>" + data.publish_time + "</td>";
            str += "<td>" + data.scraping_time + "</td>";
            str += "</tr>";                
        });
        // Tag tabel penutup
        str += "</tabel>";
        // Display semua headline ke html dengan id=media
        $("#Data-Scraping").html(str);
    });
});
