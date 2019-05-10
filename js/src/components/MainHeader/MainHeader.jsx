import React, {Fragment} from 'react'
import "./MainHeader.css"
import "./ProfileView.css"
import "./TitleView.css"
import "./TitleViewText.css"

class TitleView extends React.Component {
  render() {
    return (
      <div className="TitleView">
        <a href="/">
          <img height="50" width="50" src="/static/logo.svg" alt="Dry Electrics Delegator Logo" />
        </a>
        <div className="TitleViewText">
          <a href="/">Dry</a>
          <a href="/">Electrics</a>
          <a href="/">Delegator</a>
        </div>
      </div>
    )
  }
}

class ProfileView extends React.Component {
  render() {
    return (
      <div className="ProfileView">
        {this.props.currentUser.isAuthenticated ?
          <LoggedInView username={this.props.currentUser.username} /> :
          <LoggedOutView />
        }
      </div>
    )
  }
}

class LoggedInView extends React.Component {
  render() {
    return (
      <Fragment>
        <div>Stay Wet, { this.props.username }</div>
        <div>
          <a href="/settings">Settings</a>{" "}
          <a href={`/users/${this.props.username}`}>Profile</a>{" "}
          <a href="/logout">Logout</a>
        </div>
      </Fragment>
    )
  }
}

class LoggedOutView extends React.Component {
  render() {
    return (
      <Fragment>
        <a href="/login">Login</a>
        <a href="/signup">Sign Up</a>
      </Fragment>
    )
  }
}

class MainHeader extends React.Component {
  render() {
    return (
      <header className="MainHeader">
        <TitleView />
        <ProfileView currentUser={window.gon.currentUser}/>
      </header>
    )
  }
}

export default MainHeader;