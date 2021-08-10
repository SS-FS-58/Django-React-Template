import * as React from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';

import MainRoute from 'src/pages/main/route';
import BusinessRoute from 'src/pages/business/route';
import SearchPage from 'src/pages/search';
import UserRoute from 'src/pages/user/route';
import LoginPage from 'src/pages/auth/Login';
import { Layout } from 'src/components';

function Routes() {
  return (
    <>
      <Switch>
        <Route path="/login" component={LoginPage} />
        <Layout>
          <Switch>
            <Route path="/main" component={MainRoute} />
            <Route path="/business" component={BusinessRoute} />
            <Route path="/search" component={SearchPage} />
            <Route path="/user" component={UserRoute} />
          </Switch>
        </Layout>
        <Redirect to="/" />
      </Switch>
    </>
  );
}

export default Routes;
