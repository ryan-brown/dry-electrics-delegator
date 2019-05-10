import React, {Fragment} from 'react'
import ReactDOM from 'react-dom'
import Page from './components/Page/Page'

class PrivacyPolicyPage extends React.Component {
  render() {
    return (
      <Page>
        <PrivacyPolicyContent />
      </Page>
    );
  }
}

const PrivacyPolicyContent = () => (
  <Fragment>
    <h2>Privacy Policy</h2>

    <p>The Dry Electrics service does not share personal information with third parties nor do we store any information about your visit to this site. If you are running the <a href="https://github.com/ryan-brown/dry-electrics-delegator">client software</a>, the submitted data about your battery percentage, charger status, timestamp, and name will be collected.</p>

    <p>This privacy policy is subject to change without notice and was last updated on November 20, 2018. If you have any questions feel free to contact us directly here: electrics@fortheusers.org.</p>
  </Fragment>
)

ReactDOM.render(<PrivacyPolicyPage />, document.getElementById('root'))