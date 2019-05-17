import React from "react";
import moment from "moment";
import Avatar from "../Avatar/Avatar";
import "./LiveBatteryTable.css";

moment.relativeTimeThreshold("s", 60);
moment.relativeTimeThreshold("ss", 1);
moment.relativeTimeThreshold("m", 60);

const LiveBatteryUpdateTime = props => {
  const { time } = props;
  return moment.unix(parseInt(time, 10)).fromNow();
};

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
