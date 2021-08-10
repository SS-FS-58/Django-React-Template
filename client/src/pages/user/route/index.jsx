import * as React from 'react';
import { Switch, Route } from 'react-router-dom';

import Setting from '../Setting';
import Notification from '../Notification';

function UserRoute() {
  return (
    <Switch>
      <Route path="/user/setting" component={Setting} />
      <Route path="/user/notification" component={Notification} />
    </Switch>
  );
}

export default UserRoute;
