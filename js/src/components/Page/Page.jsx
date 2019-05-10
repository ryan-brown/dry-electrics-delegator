import React from "react";
import MainHeader from "../MainHeader/MainHeader";
import MainFooter from "../MainFooter/MainFooter";
import "./Page.css";

const Page = props => (
  <div className="Page">
    <MainHeader />
    <div style={{ flexGrow: "1" }}>{props.children}</div>
    <MainFooter />
  </div>
);

export default Page;
