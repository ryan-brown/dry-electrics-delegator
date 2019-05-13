import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import TableForm from "../../components/TableForm/TableForm";
import FlashMessage from "../../components/FlashMessage/FlashMessage";

const settingsFormData = [
  {
    title: "Email",
    name: "email",
    type: "text",
    default: window.gon.currentUser.email
  },
  {
    title: "Username",
    name: "username",
    type: "text",
    default: window.gon.currentUser.username
  },
  {
    title: "New Password",
    name: "password",
    type: "password"
  },
  {
    title: "Confirm Password",
    name: "confirm",
    type: "password"
  },
  {
    title: `Reset Zap Token (${window.gon.currentUser.zapToken})`,
    name: "new_zap",
    type: "checkbox",
    default: "checked"
  }
];

const SettingsPage = () => (
  <Page>
    <h2>Settings</h2>
    <FlashMessage messages={window.gon.flashMessages} />
    <TableForm rows={settingsFormData} />
  </Page>
);

ReactDOM.render(<SettingsPage />, document.getElementById("root"));
