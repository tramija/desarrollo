$(function () {
    
    $('#fecha_inicio').datetimepicker({
        format: "YYYY-MM-DD",
        date: moment().format("YYYY-MM-DD"),
        locale :'es'
    });
    $('#fecha_terminacion').datetimepicker({
        format: "YYYY-MM-DD",
        date: moment().format("YYYY-MM-DD"),
        locale :'es'
    });
    
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
            {"data": "hallazgo"},
            {"data": "descripcionActividades"},
            {"data": "responsable"},
            {"data": "image"},
            {"data": "fecha_inicio"},
            {"data": "fecha_terminacion"},
           
        ],
        columnDefs: [

            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + row.image + '" class="img-fluid mx-auto d-block" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/tarea/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/tarea/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});