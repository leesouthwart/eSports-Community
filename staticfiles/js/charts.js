

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawDayChart);
google.charts.setOnLoadCallback(drawWeekChart);
google.charts.setOnLoadCallback(drawMonthChart);
google.charts.setOnLoadCallback(drawBugsChart);
google.charts.setOnLoadCallback(drawContentsChart);

    
    var chart_options = {
          'width':'100%',
          'height': 250,
          'chartArea': {'width': '100%', 'height': '80%'},
          'legend': {'position':  'bottom'},
          pieSliceText: 'value',
          colors: ['#d80707','#ffa500','#32d832']
        }
    
    
    
    function drawDayChart() {
    
        var data = google.visualization.arrayToDataTable([
          ['Issue Type', 'Amount per Day'],
          ['Bug', 5],
          ['Content Suggestion', 2]
          
        ]);

        var options = chart_options;

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));
        
        chart.draw(data, options);
        
        
      }
      
    
    function drawWeekChart() {
        
        var data = google.visualization.arrayToDataTable([
            ['Issue Type', 'Amount per Week'],
            ['Bug', 16],
            ['Content Suggestion', 11]
            
            ]);
            
            var options =chart_options;
           
            var chart = new google.visualization.PieChart(document.getElementById('piechart2'));
            
            chart.draw(data, options);
    }
    
    function drawMonthChart() {
        
        var data = google.visualization.arrayToDataTable([
            ['Issue Type', 'Amount per Month'],
            ['Bug', 62],
            ['Content Suggestion', 48]
            
            ]);
            
            var options = chart_options;
            
            var chart = new google.visualization.PieChart(document.getElementById('piechart3'));
            
            chart.draw(data,options)
    }




    function drawBugsChart() {
        
        
        
        bugs_completed = parseInt(bugs_completed, 10);
        bugs_progress = parseInt(bugs_progress, 10);
        bugs_backlog = parseInt(bugs_backlog, 10);
        console.log(bugs_progress);
        
        var data = google.visualization.arrayToDataTable([
          ['Status', 'Amount'],
          ['Backlog', bugs_backlog],
          ['In Progress', bugs_progress],
          ['Completed', bugs_completed]
          
        ]);

        var options = chart_options;

        var chart = new google.visualization.PieChart(document.getElementById('piechart4'));
        
        chart.draw(data, options);
       
    }    
        
    function drawContentsChart() {
        
        
        
        contents_completed = parseInt(contents_completed, 10);
        contents_progress = parseInt(contents_progress, 10);
        contents_backlog = parseInt(contents_backlog, 10);
        console.log(bugs_progress);
        
        var data = google.visualization.arrayToDataTable([
          ['Status', 'Amount'],
          ['Backlog', contents_backlog],
          ['In Progress', contents_progress],
          ['Completed', contents_completed]
          
        ]);

        var options = chart_options;

        var chart = new google.visualization.PieChart(document.getElementById('piechart5'));
        
        chart.draw(data, options);
        
        
      }
      
// resize upon window size change
$(document).ready(function () {
  $(window).resize(function(){
	  	drawDayChart();
	  	drawWeekChart();
	  	drawMonthChart();
	});
});

