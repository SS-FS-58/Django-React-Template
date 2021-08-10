import React from 'react';
import { Provider } from 'react-redux';
import { ThemeProvider } from '@material-ui/styles';
import { ConnectedRouter } from 'connected-react-router';

import Routes from 'src/routes';

import configureStore, { history } from './store';
import theme from './theme';
import GlobalStyles from './components/GlobalStyles';

import './theme/global.css';

const store = configureStore();

function App() {
  return (
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <ThemeProvider theme={theme}>
          <GlobalStyles />
          <Routes />
        </ThemeProvider>
      </ConnectedRouter>
    </Provider>
  );
}

export default App;
