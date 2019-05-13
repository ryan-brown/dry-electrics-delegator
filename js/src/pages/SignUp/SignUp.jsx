import React from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import TableForm from "../../components/TableForm/TableForm";
import FlashMessage from "../../components/FlashMessage/FlashMessage";

const signupFormData = [
  {
    title: "Email",
    name: "email",
    type: "text"
  },
  {
    title: "Username",
    name: "username",
    type: "text"
  },
  {
    title: "Password",
    name: "password",
    type: "password"
  },
  {
    title: "Confirm Password",
    name: "confirm",
    type: "password"
  }
];

const LoginPage = () => (
  <Page>
    <h2>Sign Up</h2>
    <FlashMessage messages={window.gon.flashMessages} />
    <TableForm rows={signupFormData} />
  </Page>
);

ReactDOM.render(<LoginPage />, document.getElementById("root"));
