document.addEventListener('DOMContentLoaded', function () {
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const scores = [78, 85, 69, 92, 80, 75, null, null, null, null, null, null];

  const validScores = scores.filter(score => score !== null);
  const overall = validScores.reduce((a, b) => a + b, 0) / validScores.length;

  document.getElementById('overallPerformance').innerText = overall.toFixed(2);

  const ctx = document.getElementById('areaChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: months,
      datasets: [{
        label: 'Performance %',
        data: scores,
        fill: true,
        tension: 0.4,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        pointBackgroundColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          title: {
            display: true,
            text: 'Performance (%)'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Months'
          }
        }
      },
      plugins: {
        legend: {
          display: true
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return context.parsed.y !== null ? `${context.parsed.y}%` : 'No Data';
            }
          }
        }
      }
    }
  });
});


