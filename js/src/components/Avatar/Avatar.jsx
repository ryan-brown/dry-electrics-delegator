import React from "react";
import "./Avatar.css";

const Avatar = props => (
  <div className="Avatar">
    <img
      alt="Avatar"
      width={props.width || 64}
      height={props.height || 64}
      src={`/static/${props.username}.png`}
    />
  </div>
);

export default Avatar;
