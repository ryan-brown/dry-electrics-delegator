import React, { Fragment } from "react";
import "./MainHeader.css";
import "./ProfileView.css";
import "./TitleView.css";
import "./TitleViewText.css";

const TitleView = () => (
  <div className="TitleView">
    <a href="/">
      <img
        height="50"
        width="50"
        src="/static/logo.svg"
        alt="Dry Electrics Delegator Logo"
      />
    </a>
    <div className="TitleViewText">
      <a href="/">Dry</a>
      <a href="/">Electrics</a>
      <a href="/">Delegator</a>
    </div>
  </div>
);

const ProfileView = props => (
  <div className="ProfileView">
    {props.currentUser.isAuthenticated ? (
      <LoggedInView username={props.currentUser.username} />
    ) : (
      <LoggedOutView />
    )}
  </div>
);

const LoggedInView = props => (
  <Fragment>
    <div>
      Stay Wet,
      {props.username}
    </div>
    <div>
      <a href="/settings">Settings</a>
      <a href={`/users/${props.username}`}>Profile</a>
      <a href="/logout">Logout</a>
    </div>
  </Fragment>
);

const LoggedOutView = () => (
  <Fragment>
    <a href="/login">Login</a>
    <a href="/signup">Sign Up</a>
  </Fragment>
);

const MainHeader = () => (
  <header className="MainHeader">
    <TitleView />
    <ProfileView currentUser={window.gon.currentUser} />
  </header>
);

export default MainHeader;
