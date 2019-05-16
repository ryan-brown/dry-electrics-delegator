import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import LiveBatteryTable from "../../components/LiveBatteryTable/LiveBatteryTable";

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = { loading: true, data: [] };
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
        that.state = { loading: false, data };
      });
  }

  render() {
    return (
      <Page>
        {(() => {
          const { data = [], loading = true } = this.state;
          if (loading)
            return (
              <h2>
                <object
                  width="200px"
                  data="/static/loader.svg"
                  type="image/svg+xml"
                  aria-label="loader svg"
                />
              </h2>
            );
          if (!data.length)
            return <h2>Nobody is currently reporting charging data.</h2>;
          return <LiveBatteryTable data={this.state.data} />;
        })()}
      </Page>
    );
  }
}

ReactDOM.render(<HomePage />, document.getElementById("root"));
