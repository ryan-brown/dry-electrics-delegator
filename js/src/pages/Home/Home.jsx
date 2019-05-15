import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import LiveBatteryTable from "../../components/LiveBatteryTable/LiveBatteryTable";

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: [] };
  }

  componentDidMount() {
    this.getStats();
    this.interval = setInterval(() => this.getStats(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  getStats() {
    const that = this;
    fetch("/api/stats")
      .then(response => {
        return response.json();
      })
      .then(data => {
        that.setState({ data });
      });
  }

  render() {
    return (
      <Page>
        {this.state.data.length > 0 ? (
          <LiveBatteryTable data={this.state.data} />
        ) : (
          <h2>Nobody is currently reporting charging data.</h2>
        )}
      </Page>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("root"));
