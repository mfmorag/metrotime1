
//morris area chart

$(function () {
    //morris donut chart
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Activo",
            value: 2
        }, {
            label: "Inactivo",
            value: 1
        }, {
            label: "Mantenimiento",
            value: 1
        }],
        resize: true
    });
    //morris bar chart
});
