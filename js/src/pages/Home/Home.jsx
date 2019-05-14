import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import "./HomePageTable.css"

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data: []};
  }

  getStats() {
    const that = this;
    fetch('/api/stats').then(function(response) {
      return response.json()
    }).then(function(data) {
      that.setState({ data: data });
    })
  }

  componentDidMount() {
    this.getStats()
    this.interval = setInterval(() => this.getStats(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    return (
    <Page>
      {(this.state.data.length > 0) ? 
        <HomePageTable data={this.state.data} /> :
        <h2>Nobody is currently reporting charging data.</h2>
      }
    </Page>
    );
  }
}

const HomePageTable = props => (
    <div className="HomePageTable">
      <table><tbody>
        <tr>
          <th>User</th>
          <th>Percentage</th>
          <th>Charging</th>
          <th>Updated At</th>
        </tr>
        {props.data.map(user => {
          return (
            <tr key={user[0]} style={{backgroundColor:user[0]}}>
              <td>
                <a href={`/users/${user[1]}`}>{user[1]}</a>
              </td>
              <td>
                {user[2]}
              </td>
              <td>
                {user[3]}
              </td>
              <td>
                {moment.unix(parseInt(user[4])).fromNow()}
              </td>
            </tr>
          )
        })}
      </tbody></table>
    </div>
);

ReactDOM.render(<HomePage />, document.getElementById("root"));
