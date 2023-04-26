var ctx_1 = document.getElementById('myChart_1').getContext('2d');
var ctx_2 = document.getElementById('myChart_2').getContext('2d');
var myChart = new Chart(ctx_1, {
    type: 'doughnut',
    data: {
        // labels: ['Blue'],
        datasets: [{
            data: [100,30],
            backgroundColor: [   
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)'                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'               
            ],
            borderWidth: 1,
            
        }]
    },
    options: {
        cutoutPercentage: 30,
        legend: {
            display: true,
            position: 'top'
        },
        responsive: false,
        maintainAspectRatio: true
    }
});
var myChart = new Chart(ctx_2, {
    type: 'doughnut',
    data: {
        // labels: ['Blue'],
        datasets: [{
            data: [100,70],
            backgroundColor: [   
                'rgba(255, 20, 132, 0.8)',
                'rgba(154, 160, 235, 0.8)'                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'               
            ],
            borderWidth: 1,
            
        }]
    },
    options: {
        cutoutPercentage: 30,
        legend: {
            display: true,
            position: 'top'
        },
        responsive: false,
        maintainAspectRatio: true
    }
});
