import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import HistoryChart from "../../components/HistoryChart/HistoryChart";

const HistoryPage = () => (
  <Page>
    <h2>{`${window.gon.currentUser.username} Battery History`}</h2>
    <HistoryChart />
  </Page>
);

ReactDOM.render(<HistoryPage />, document.getElementById("root"));
