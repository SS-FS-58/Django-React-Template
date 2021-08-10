import { createMuiTheme } from '@material-ui/core';

import {
  PRIMARY,
  SECONDARY,
  TEXT_PRIMARY,
  TEXT_SECONDARY,
  SUCCESS,
  ERROR,
} from 'src/constants/colors';

const theme = createMuiTheme({
  palette: {
    background: {
      light: '#F9F7FC',
      default: '#fff',
      dark: SECONDARY,
    },
    primary: {
      main: PRIMARY,
      contrastText: '#fff',
    },
    secondary: {
      main: SECONDARY,
      contrastText: '#fff',
    },
    text: {
      primary: TEXT_PRIMARY,
      secondary: TEXT_SECONDARY,
    },
    success: {
      main: SUCCESS,
    },
    error: {
      main: ERROR,
    },
  },
  typography: {
    fontFamily: 'Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"',
  },
});

theme.overrides = {
  MuiAlert: {
    root: {
      fontSize: '1rem',
    },
  },
  MuiButton: {
    root: {
      fontSize: 16,
      textTransform: 'unset',
    },
    contained: {
      boxShadow: 'none',
      '&:hover': {
        boxShadow: 'none',
      },
    },
  },
  MuiDivider: {
    root: {
      marginTop: 24,
      marginBottom: 24,
    },
  },
};

export default theme;
