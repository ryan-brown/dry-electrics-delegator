import React from "react";
import moment from "moment";
import "./LiveBatteryTable.css";

moment.relativeTimeThreshold("s", 60);
moment.relativeTimeThreshold("ss", 1);
moment.relativeTimeThreshold("m", 60);

const LiveBatteryTable = props => (
  <div className="LiveBatteryTable">
    <table>
      <tbody>
        <tr>
          <th>User</th>
          <th>Percentage</th>
          <th>Charging</th>
          <th>Updated At</th>
        </tr>
        {props.data.map(user => {
          return (
            <tr key={user[0]} style={{ backgroundColor: user[0] }}>
              <td>
                <a href={`/users/${user[1]}`}>{user[1]}</a>
              </td>
              <td>{user[2]}</td>
              <td>{user[3]}</td>
              <td>{moment.unix(parseInt(user[4], 10)).fromNow()}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  </div>
);

export default LiveBatteryTable;
