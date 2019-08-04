// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// https://upload.wikimedia.org/wikipedia/commons/7/7d/Pedro_luis_romani_ruiz.gif

// Pie Chart Example
function renderChart(data, labels) {
  var ctx = document.getElementById("myPieChart");
  var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ["Direct", "Referral", "Social"], // labels
      datasets: [{
        data: [55, 30, 15], // data
        backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'], // some color generator function
        hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'], // some color generator function
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        caretPadding: 10,
      },
      legend: {
        display: false
      },
      cutoutPercentage: 80,
    },
  });
};

function getChartData() {
  $("#loadingMessage").html('<img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/Pedro_luis_romani_ruiz.gif" alt="Loading...">');
  $.ajax({
    url: "chartdata",
    success: function (result) {
      $("#loadingMessage").html('');
      // var data = [];
      // data.push(result.thisWeek);
      // data.push(result.lastWeek);
      // var labels = result.labels;
      // renderChart(data, labels);
      renderChart('1', '2');
    },
    error: function (err) {
      $("#loadingMessage").html("Error");
    }
  });
};

getChartData();