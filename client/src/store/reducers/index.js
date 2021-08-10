import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';

import authReducer from './auth';
import businessReducer from './business';
import userReducer from './user';

const createRootReducer = (history) => combineReducers({
  router: connectRouter(history),
  auth: authReducer,
  business: businessReducer,
  user: userReducer,
});

export default createRootReducer;
