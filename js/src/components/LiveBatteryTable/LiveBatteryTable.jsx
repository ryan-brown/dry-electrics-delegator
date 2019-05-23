import React from "react";
import moment from "moment";
import Avatar from "../Avatar/Avatar";
import "./LiveBatteryTable.css";

moment.relativeTimeThreshold("s", 60);
moment.relativeTimeThreshold("ss", 1);
moment.relativeTimeThreshold("m", 60);

class LiveBatteryUpdateTime extends React.Component {
  constructor(props) {
    super(props);
    const { time } = props;
    this.state = { time };
  }

  componentDidMount() {
    const that = this;
    this.interval = setInterval(() => {
      that.setState({
        time: this.state.time
      });
    }, 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    return <div>{moment.unix(parseInt(this.state.time, 10)).fromNow()}</div>;
  }
}

const LiveBatteryRow = props => {
  const { user } = props;
  return (
    <tr key={user[0]} style={{ backgroundColor: user[0] }}>
      <td>
        <a href={`/users/${user[1]}`}>
          <Avatar width="32" height="32" username={user[1]} />
        </a>
      </td>
      <td>
        <a href={`/users/${user[1]}`}>{user[1]}</a>
      </td>
      <td>{user[2]}</td>
      <td>{user[3]}</td>
      <td>
        <LiveBatteryUpdateTime time={user[4]} />
      </td>
    </tr>
  );
};

const LiveBatteryTable = props => (
  <div className="LiveBatteryTable">
    <table>
      <tbody>
        <tr>
          <th />
          <th>User</th>
          <th>Percentage</th>
          <th>Charging</th>
          <th>Updated At</th>
        </tr>
        {props.data.map(user => {
          return <LiveBatteryRow user={user} />;
        })}
      </tbody>
    </table>
  </div>
);

export default LiveBatteryTable;
