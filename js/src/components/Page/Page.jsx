import React, {Fragment} from 'react'
import MainHeader from '../MainHeader/MainHeader'
import MainFooter from '../MainFooter/MainFooter'
import "./Page.css"

class Page extends React.Component {
  render() {
    return (
      <div className="Page">
        <MainHeader />
        <div style={{flexGrow: "1"}}>
          {this.props.children}
        </div>
        <MainFooter />
      </div>
    );
  }
}

export default Page;