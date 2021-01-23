window.onload=render;
function render(){
let drawdate=document.getElementById("drawdate").value;
var req=new XMLHttpRequest();
req.onreadystatechange=function(){
    if(req.readyState==4 && req.status==200){
        insights=JSON.parse(this.responseText);
        var ctx = document.getElementById('myChart').getContext('2d');
        ctx.height = 10;
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Logins', 'Change Password', 'Tasks added', 'Delete Tasks', 'Edit Tasks', 'Task Completed','Task Searched'],
        datasets: [{
            label: '# Tasks insight',
            data: [insights.logins,insights.changepassword,insights.addtasks,insights.deletetasks,insights.edittasks,insights.completetask,insights.searchtask],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive:true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

}
}
req.open("GET","insightsdataset?drawdate="+drawdate,true)
req.send();
}