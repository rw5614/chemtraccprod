// Call the dataTables jQuery plugin
$(document).ready(function () {
    $('#dataTable').DataTable({
        "ajax": {
            "url": "/test_data",
            "dataSrc": "data"
        },
        columns: [
            {data: "RFID_number"},
            {data: "customer_id"},
            {data: "foo"},
            {data: "reen_eggs"},
            {data: "loc"},
            {data: "name"},
            {data: "timestamp"}
        ]
    });
});

// function loadDataTable(numItems) {
//   $(document).ready(function() {
//     $('#example').DataTable( {
//         "processing": true,
//         "serverSide": true,
//         "searching": false, // Disables the search bar.
//         "ajax": "scripts/server_processing.php", // This should be our endpoint. We need to wrap this in a function 
//         "deferLoading": numItems // We need to tell datatables how many items there are.
//     } );
//   } );
// }