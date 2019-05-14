import React from "react";
import MainHeader from "../MainHeader/MainHeader";
import MainFooter from "../MainFooter/MainFooter";
import "./Page.css";

const Page = props => (
  <div className="Page">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <MainHeader />
    <div style={{ flexGrow: "1" }}>{props.children}</div>
    <MainFooter />
  </div>
);

export default Page;
