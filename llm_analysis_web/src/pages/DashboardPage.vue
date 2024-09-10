<template>
    <q-page padding>
      <div class="q-pa-md">
        <q-select
          v-model="selectedItem"
          :options="options"
          label="Select an item"
          @input="updateCharts"
          outlined
        />
        <q-separator spaced />
  
        <q-card class="q-pa-md">
          <div class="row q-col-gutter-md">
            <div class="col-xs-12 col-md-6">
              <div ref="pieChart1" style="width:100%;height:400px;"></div>
            </div>
            <div class="col-xs-12 col-md-6">
              <div ref="pieChart2" style="width:100%;height:400px;"></div>
            </div>
          </div>
          <div class="row q-col-gutter-md q-mt-md">
            <div class="col-xs-12 col-md-6">
              <div ref="barChart1" style="width:100%;height:400px;"></div>
            </div>
            <div class="col-xs-12 col-md-6">
              <div ref="barChart2" style="width:100%;height:400px;"></div>
            </div>
          </div>
        </q-card>
      </div>
    </q-page>
</template>
  
<script>
import Plotly from 'plotly.js-dist';

export default {
  data() {
    return {
      selectedItem: null,
      options: [
        { label: 'Data Set 1', value: 'set1' },
        { label: 'Data Set 2', value: 'set2' },
        { label: 'Data Set 3', value: 'set3' }
      ],
      dataSets: {
        set1: {
          pie1: { labels: ['A', 'B', 'C'], values: [10, 20, 30] },
          pie2: { labels: ['X', 'Y', 'Z'], values: [5, 15, 25] },
          bar1: { x: ['Jan', 'Feb', 'Mar'], y: [15, 25, 35] },
          bar2: { x: ['Red', 'Green', 'Blue'], y: [50, 30, 20] }
        },
        set2: {
          pie1: { labels: ['D', 'E', 'F'], values: [20, 30, 50] },
          pie2: { labels: ['L', 'M', 'N'], values: [10, 20, 40] },
          bar1: { x: ['Apr', 'May', 'Jun'], y: [25, 35, 45] },
          bar2: { x: ['Orange', 'Purple', 'Yellow'], y: [60, 40, 30] }
        },
        set3: {
          pie1: { labels: ['G', 'H', 'I'], values: [15, 25, 60] },
          pie2: { labels: ['O', 'P', 'Q'], values: [15, 25, 35] },
          bar1: { x: ['Jul', 'Aug', 'Sep'], y: [45, 55, 65] },
          bar2: { x: ['Pink', 'Black', 'White'], y: [70, 50, 40] }
        }
      }
    };
  },
  methods: {
    plotCharts() {
      const selectedData = this.dataSets[this.selectedItem];

      // Pie Chart 1
      Plotly.newPlot(this.$refs.pieChart1, [{
        type: 'pie',
        labels: selectedData.pie1.labels,
        values: selectedData.pie1.values
      }]);

      // Pie Chart 2
      Plotly.newPlot(this.$refs.pieChart2, [{
        type: 'pie',
        labels: selectedData.pie2.labels,
        values: selectedData.pie2.values
      }]);

      // Bar Chart 1
      Plotly.newPlot(this.$refs.barChart1, [{
        type: 'bar',
        x: selectedData.bar1.x,
        y: selectedData.bar1.y
      }]);

      // Bar Chart 2
      Plotly.newPlot(this.$refs.barChart2, [{
        type: 'bar',
        x: selectedData.bar2.x,
        y: selectedData.bar2.y
      }]);
    },
    updateCharts() {
      if (this.selectedItem) {
        this.plotCharts();
      }
    }
  },
  mounted() {
    this.selectedItem = 'set1';  // Default data set on page load
    this.plotCharts();
  }
};
</script>

<style scoped>
.q-page {
  background-color: #f5f5f5;
}

.q-card {
  background-color: white;
}

.q-separator {
  margin: 20px 0;
}

.q-select {
  margin-bottom: 10px;
}
</style>
