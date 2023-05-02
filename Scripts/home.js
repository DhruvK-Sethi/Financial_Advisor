// var ctx_1 = document.getElementById('myChart_1').getContext('2d');
// var ctx_2 = document.getElementById('myChart_2').getContext('2d');
// var myChart = new Chart(ctx_1, {
//     type: 'doughnut',
//     options: 'maintainAspectRatio',
//     data: {
//         // labels: ['Blue'],
        
//         datasets: [{
//             data: [100,30],
//             backgroundColor: [   
//                 'rgba(255, 99, 132, 0.8)',
//                 'rgba(54, 162, 235, 0.8)'                
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)'               
//             ],
//             borderWidth: 1,
            
//         }]
//     },
//     options: {
//         cutoutPercentage: 30,
//         legend: {
//             display: true,
//             position: 'top'
//         },
//         responsive: false,
//         maintainAspectRatio: true
//     }
// });
// var myChart = new Chart(ctx_2, {
//     type: 'doughnut',
//     data: {
//         // labels: ['Blue'],
//         datasets: [{
//             data: [100,70],
//             backgroundColor: [   
//                 'rgba(255, 20, 132, 0.8)',
//                 'rgba(154, 160, 235, 0.8)'                
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)'               
//             ],
//             borderWidth: 1,
            
//         }]
//     },
//     options: {
//         cutoutPercentage: 30,
//         legend: {
//             display: true,
//             position: 'top'
//         },
//         responsive: false,
//         maintainAspectRatio: true
//     }
// });


google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    // allocation percentages
    var domestic_equity = parseInt(document.getElementById('domestic').value);
    var us_equity = parseInt(document.getElementById('us').value);
    var gold = parseInt(document.getElementById('gold').value);
    var debt = parseInt(document.getElementById('debt').value);
    var crypto = parseInt(document.getElementById('crypto').value);
    var reits = parseInt(document.getElementById('reits').value);

    // data for pie chart
    var data = google.visualization.arrayToDataTable([
        ['Asset Class', 'Percentage'],
        ['Domestic Equity', domestic_equity],
        ['US Equity', us_equity],
        ['Gold', gold],
        ['Debt', debt],
        ['Crypto', crypto],
        ['REITs', reits]
    ]);

    // options for pie chart
    var options = {
        title: 'Investment Allocation',
        pieHole: 0.2,
        slices: {
            0: { color: 'blue' },
            1: { color: 'orange' },
            2: { color: 'green' },
            3: { color: 'red' },
            4: { color: 'pink' },
            5: { color: 'yellow' }

        },
        width: 500,
        height: 500

    };

    // create pie chart object
    var chart = new google.visualization.PieChart(document.getElementById('myChart_1'));

    // draw the chart
    chart.draw(data, options);
}

function updateChart() {
    drawChart();
}