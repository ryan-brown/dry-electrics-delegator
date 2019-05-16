import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import Avatar from "../../components/Avatar/Avatar";

const UserPage = () => (
  <Page>
    <h2>Profile</h2>
    <Avatar username={window.gon.user.username} />
    <div>{window.gon.user.email}</div>
    <div>{window.gon.user.username}</div>
    <div>
      <a href={`${window.gon.user.username}/history`}>Battery History</a>
    </div>
  </Page>
);

ReactDOM.render(<UserPage />, document.getElementById("root"));
