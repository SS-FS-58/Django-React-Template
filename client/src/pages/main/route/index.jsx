import * as React from 'react';
import { Switch, Route } from 'react-router-dom';

import DashboardPage from '../Dashboard';

function MainRoute() {
  return (
    <Switch>
      <Route path="/main/dashboard" component={DashboardPage} />
    </Switch>
  );
}

export default MainRoute;
