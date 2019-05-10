import React from "react";
import "./TableForm.css";

const TableForm = props => (
  <form method="POST" action="">
    <table className="TableForm">
      <tbody>
        {props.rows.map(row => {
          return (
            <tr key={row.title}>
              <td>{row.title}</td>
              <td>
                <input
                  type={row.type}
                  name={row.name}
                  defaultValue={row.default || ""}
                />
              </td>
            </tr>
          );
        })}
        <tr key="submit">
          <td colSpan="2" align="center">
            <button type="submit">Submit</button>
          </td>
        </tr>
      </tbody>
    </table>
  </form>
);

export default TableForm;
