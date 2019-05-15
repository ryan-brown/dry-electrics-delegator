import React, { Fragment } from "react";
import ReactDOM from "react-dom";
import Page from "../../components/Page/Page";
import "./NotFound.css";

const NotFoundPage = () => (
  <Page>
    <NotFoundContent />
  </Page>
);

const NotFoundContent = () => (
  <Fragment>
    <div className="NotFound">
      <div id="content">
        <img
          height="200"
          width="200"
          src="/static/electrics_404.svg"
          alt="Battery Problem"
        />
        <div id="textContent">
          <h2>Yikes, this page is out of power!</h2>
          <p>Or, well, we couldn't find the page you were looking for.</p>
          <p>
            Double-check that the URL is correct, otherwise
            <a href="/">click here to go to the homepage</a>.
          </p>
        </div>
      </div>
    </div>
  </Fragment>
);

ReactDOM.render(<NotFoundPage />, document.getElementById("root"));
