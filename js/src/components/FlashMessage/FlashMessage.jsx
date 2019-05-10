import React, {Fragment} from 'react'
import "./FlashMessage.css"

class FlashMessage extends React.Component {
  render() {
    return (
      <Fragment>
        {this.props.messages.map((message, index) => {
          return <Fragment key={index}><span className="FlashMessage">{message}</span><br /></Fragment>
        })}
      </Fragment>
    )
  }
}

export default FlashMessage;
