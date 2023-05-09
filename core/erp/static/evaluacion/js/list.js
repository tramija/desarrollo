$(function () {

   
    
   
    // $('#date_joined').datetimepicker({
    //     format: 'YYYY-MM-DD H:M',
    //     date: moment().format("YYYY-MM-DD H:M"),
    //     locale: 'es',
    //     //minDate: moment().format("YYYY-MM-DD")
    // });
    
    // $('#fecha_cierre').datetimepicker({
    //     format: "YYYY-MM-DD",
    //     date: moment().format("YYYY-MM-DD"),
    //     locale :'es'
    // });
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "position"},
            {"data": "name"},
            {"data": "date_joined"},
            {"data": "responsable"},
            {"data": "img"},
            {"data": "observaciones"},
            {"data": "planMejora"},
            {"data": "fecha_cierre"},
            {"data": "estado"},
        ],
        columnDefs: [


            {
                targets: [-5],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + row.img + '" class="img-fluid mx-auto d-block" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/evaluacion/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/evaluacion/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});