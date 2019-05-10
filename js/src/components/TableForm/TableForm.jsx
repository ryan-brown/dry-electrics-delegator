import React, {Fragment} from 'react'
import "./TableForm.css"

class TableForm extends React.Component {
  render() {
    return (
      <form method="POST" action="">
      <table className="TableForm"><tbody>
        {this.props.rows.map((row, index) => {
          return (
            <tr key={index}>
              <td>{row.title}</td>
              <td><input type={row.type} name={row.name} defaultValue={row.default || ""} /></td>
            </tr>
          )
        })}
        <tr key="submit">
          <td colSpan="2" align="center"><button type="submit">Submit</button></td>
        </tr>
      </tbody></table>
      </form>
    )
  }
}

export default TableForm;
