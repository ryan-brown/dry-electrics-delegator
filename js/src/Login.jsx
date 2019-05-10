import React from "react";
import ReactDOM from "react-dom";
import Page from "./components/Page/Page";
import TableForm from "./components/TableForm/TableForm";
import FlashMessage from "./components/FlashMessage/FlashMessage";

const loginFormData = [
  {
    title: "Email",
    name: "email",
    type: "text"
  },
  {
    title: "Password",
    name: "password",
    type: "password"
  }
];

const LoginPage = () => (
  <Page>
    <h2>Log In</h2>
    <FlashMessage messages={window.gon.flashMessages} />
    <TableForm rows={loginFormData} />
  </Page>
);

ReactDOM.render(<LoginPage />, document.getElementById("root"));
