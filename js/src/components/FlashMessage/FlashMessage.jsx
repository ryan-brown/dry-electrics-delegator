import React, { Fragment } from "react";
import "./FlashMessage.css";

const FlashMessage = ({ messages = [] }) =>
  messages.map(message => {
    return (
      <Fragment key={message}>
        <span className="FlashMessage">{message}</span>
        <br />
      </Fragment>
    );
  });

export default FlashMessage;
