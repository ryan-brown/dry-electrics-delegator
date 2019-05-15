import React from "react";
import "./HistoryChart.css";
import drawChart from "./user-chart";

class HistoryChart extends React.Component {
  componentDidMount() {
    drawChart();
  }

  render() {
    return (
      <div className="HistoryChart">
        <div id="chart-controls">
          <input type="datetime-local" id="start-time" />
          <input type="datetime-local" id="end-time" />
          <button type="button" id="today-button">
            Today
          </button>
          <button type="button" id="week-button">
            This Week
          </button>
          <button type="button" id="all-button">
            All Data
          </button>
          <br />
        </div>
        <div id="inner-chart" />
      </div>
    );
  }
}

export default HistoryChart;
