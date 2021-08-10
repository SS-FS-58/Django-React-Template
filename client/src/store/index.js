import { createBrowserHistory } from 'history';
import { applyMiddleware, createStore, compose } from 'redux';
import thunk from 'redux-thunk';
import { routerMiddleware } from 'connected-react-router';

import createRootReducer from './reducers';
import { isActionTypeFail } from '../utils/api';

export const history = createBrowserHistory();

// eslint-disable-next-line no-unused-vars
const crashReporter = (store) => (next) => (action) => {
  try {
    if (isActionTypeFail(action.type)) {
      console.error(action.payload);
    }
    return next(action);
  } catch (err) {
    console.error('Caught an exception!', err);
    throw err;
  }
};

// eslint-disable-next-line
export default (preloadedState = {}) => {
  const middlewares = [thunk, routerMiddleware(history), crashReporter];
  const enhancers = [applyMiddleware(...middlewares)];

  const composeEnhancers = process.env.NODE_ENV !== 'production'
    && typeof window === 'object'
    && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
    ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({
      shouldHotReload: false,
    })
    : compose;

  const store = createStore(
    createRootReducer(history),
    preloadedState,
    composeEnhancers(...enhancers),
  );

  return store;
};
