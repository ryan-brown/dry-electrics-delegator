import React from "react";
import MainHeader from "../MainHeader/MainHeader";
import MainBody from "../MainBody/MainBody";
import MainFooter from "../MainFooter/MainFooter";
import "./Page.css";

const Page = props => (
  <div className="Page">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <MainHeader />
    <MainBody>{props.children}</MainBody>
    <MainFooter />
  </div>
);

export default Page;
