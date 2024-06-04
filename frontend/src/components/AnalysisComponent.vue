<template>
    <div id="charts-container">
        <h1>Dashboard</h1>
        
        <div id="all-charts">
          <div class="chart-container">
              <h2>Temperature</h2>
              <canvas ref="barChart1" width="1000" height="300"></canvas>
          </div>

          <div class="chart-container">
              <h2>Turbidity</h2>
              <canvas ref="barChart2" width="1000" height="300"></canvas>
          </div>
          
          <div class="chart-container">
              <h2>pH</h2>
              <canvas ref="barChart3" width="1000" height="300"></canvas>
          </div>

          <div class="chart-container">
              <h2>TDS</h2>
              <canvas ref="barChart4" width="1000" height="300"></canvas>
          </div>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      barChart1: null,
      barChart2: null,
      barChart3: null,
      barChart4: null,
      lineChart: null,
      donutChart: null,
    };
  },
  mounted() {
    this.renderBarChart1();
    this.renderBarChart2();
    this.renderBarChart3();
    this.renderBarChart4();
  },
  methods: {
    renderBarChart1() {
      const ctx = this.$refs.barChart1.getContext('2d');
      this.barChart1 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average Temperature',
            data: [10, 15, 7, 12, 8],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },

    renderBarChart2() {
      const ctx = this.$refs.barChart2.getContext('2d');
      this.barChart2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average Humidity',
            data: [16, 15, 14, 14, 18],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },

    renderBarChart3() {
      const ctx = this.$refs.barChart3.getContext('2d');
      this.barChart3 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average PH',
            data: [13, 12, 7, 5, 20],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },

    renderBarChart4() {
      const ctx = this.$refs.barChart4.getContext('2d');
      this.barChart3 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average TDS',
            data: [13, 12, 7, 5, 20],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },
    
    renderDonutChart() {
      const ctx = this.$refs.donutChart.getContext('2d');
      this.donutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['Label 1', 'Label 2', 'Label 3'],
          datasets: [{
            data: [30, 40, 30],
            backgroundColor: ['#1497DD', '#1497DD', '#1497DD'],
          }],
        },
        options: {
          cutout: '80%',
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    },
  },
};
</script>

<style>
#charts-container {
    height: 90%;
    width: 90%;
    overflow-y: scroll;
}

#charts-container::-webkit-scrollbar {
  width: 8px;
  border-radius: 15px;
}

#charts-container::-webkit-scrollbar-thumb {
  background-color: #1497DD;
  border-radius: 6px;
}

#charts-container::-webkit-scrollbar-track {
  background: #f1f1f1;
}

#all-charts {
    height: 90%;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
}

.chart-container {
  margin: 20px;
}
</style>