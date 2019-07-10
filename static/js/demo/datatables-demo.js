// Call the dataTables jQuery plugin
$(document).ready(function () {
  var table = $('#dataTable').DataTable({
    // "searching": false
  });

  $('#dataTable tbody').on('click', 'tr', function() {
    var data = table.row( this ).data();
    alert(data);
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