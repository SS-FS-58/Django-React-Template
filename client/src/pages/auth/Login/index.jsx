import * as React from 'react';
import { Box, Typography } from '@material-ui/core';

import Logo from 'src/assets/images/logo.svg';
import LoginForm from './LoginForm';

import useStyles from './style';

function Login() {
  const classes = useStyles();

  return (
    <Box className={classes.root}>
      <Box className={classes.wrapper}>
        <img className={classes.logo} src={Logo} alt="prussian" width="300" />
        <Typography variant="h5" color="textPrimary">Welcome back!</Typography>
        <Typography variant="body1">Sign in to your account to continue</Typography>
        <LoginForm />
      </Box>
    </Box>
  );
}

export default Login;
