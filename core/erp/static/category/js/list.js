$(function () {

    
   
    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });
    $('#fecha_correccion').datetimepicker({
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
            {"data": "descripcionProblema"},
            {"data": "clasificacion"},
            {"data": "normaIncumplida"},
            {"data": "tipoAccion"},
            {"data": "fuentePlan"},
            {"data": "entidad"},
            {"data": "proceso"},
            {"data": "tratamientoInmediato"},
            {"data": "analisisCausa"},
            {"data": "causaRaiz"},
            {"data": "evidencia"},
            {"data": "estado"},
        ],
        columnDefs: [

            
            {
                targets: [ -2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/category/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/category/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});