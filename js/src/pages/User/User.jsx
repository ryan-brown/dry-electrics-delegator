import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";

const UserPage = () => (
  <Page>
    <h2>Profile</h2>
    <div>{window.gon.user.email}</div>
    <div>{window.gon.user.username}</div>
    <div>
      <a href={`${window.gon.user.username}/history`}>Battery History</a>
    </div>
  </Page>
);

ReactDOM.render(<UserPage />, document.getElementById("root"));