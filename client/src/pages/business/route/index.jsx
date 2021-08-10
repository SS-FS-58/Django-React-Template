import * as React from 'react';
import { Switch, Route } from 'react-router-dom';

import BasicInfoPage from '../BasicInfo';
import BusinessCondition from '../BusinessCondition';
import PreferencePage2 from '../Preference2';
import BusinessFinancePage from '../Finance';
import BusinessPreference1Page from '../Preference';

function BusinessRoute() {
  return (
    <Switch>
      <Route path="/business/basic-info" component={BasicInfoPage} />
      <Route path="/business/condition" component={BusinessCondition} />
      <Route path="/business/finance" component={BusinessFinancePage} />
      <Route path="/business/preference" component={BusinessPreference1Page} />
      <Route path="/business/preference2" component={PreferencePage2} />
    </Switch>
  );
}

export default BusinessRoute;
