import React from "react";
import "./Avatar.css";

const Avatar = props => (
  <div className="Avatar">
    <img
      alt="Avatar"
      width={props.width || 64}
      height={props.height || 64}
      src={`/static/profile_pictures/${props.username}.png?${Date.now()}`}
      onError={e => {
        e.target.onerror = null;
        e.target.src = "/static/logo.png";
      }}
    />
  </div>
);

export default Avatar;
