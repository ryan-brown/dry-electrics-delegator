import React from "react";
import "./HistoryChart.css"

const HistoryChart = () => (
  <div className="HistoryChart">
    <div id="chart-controls">
      <input type="datetime-local" id="start-time" />
      <input type="datetime-local" id="end-time" />
      <button id="today-button">Today</button>
      <button id="week-button">This Week</button>
      <button id="all-button">All Data</button><br />
    </div>
    <div id="inner-chart"></div>
  </div>
);

export default HistoryChart;
