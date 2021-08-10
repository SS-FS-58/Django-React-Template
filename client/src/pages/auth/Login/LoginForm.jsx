import * as React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  Button,
  Checkbox,
  CircularProgress,
  FormControlLabel,
  makeStyles,
} from '@material-ui/core';
import { Alert } from '@material-ui/lab';
import { useFormik } from 'formik';

import { login } from 'src/store/actions/auth';
import { requestFail } from 'src/utils/api';
import { LOGIN_REQUEST } from 'src/store/types';
import InputField from 'src/components/InputField';
import validationSchema from './schema';

const useStyles = makeStyles(() => ({
  root: {
    width: '100%',
    marginTop: 20,
  },
  mb10: {
    marginBottom: 10,
  },
}));

function LoginForm() {
  const classes = useStyles();

  const [rememberMe, setRememberMe] = React.useState(false);
  const [submitting, setSubmitting] = React.useState(false);
  const [error, setError] = React.useState('');

  const dispatch = useDispatch();
  const { status: authStatus, error: authError } = useSelector((state) => state.auth);

  React.useEffect(() => {
    const queries = new URLSearchParams(window.location.search);
    const type = queries.get('type');

    if (type === 'idle') {
      setError('Error! Your session has timed out. Please sign in again.');
      setTimeout(() => {
        setError('');
      }, 5000);
    }
  }, []);

  const handleChangeRemember = (event) => {
    setRememberMe(event.target.checked);
  };

  const handleSubmit = async (values) => {
    setSubmitting(true);
    await dispatch(
      login({
        ...values,
        rememberMe,
      }),
    );
    setSubmitting(false);
  };

  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
    },
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <form className={classes.root} onSubmit={formik.handleSubmit}>
      {(authStatus === requestFail(LOGIN_REQUEST) || !!error) && (
        <Alert variant="filled" severity="error" style={{ marginBottom: '24px' }}>
          {authError || error}
        </Alert>
      )}
      <InputField
        className={classes.mb10}
        formik={formik}
        name="username"
        label="User Name"
        placeholder="User Name"
        // inputProps={{
        //   'data-cy': 'email',
        // }}
      />
      <InputField
        className={classes.mb10}
        formik={formik}
        type="password"
        name="password"
        label="Password"
        placeholder="********"
        inputProps={{
          'data-cy': 'password',
        }}
      />
      <FormControlLabel
        className={classes.mb10}
        control={(
          <Checkbox
            checked={rememberMe}
            onChange={handleChangeRemember}
            name="checkedB"
            color="primary"
          />
        )}
        label="Remember me"
      />
      <Button type="submit" variant="contained" color="primary" fullWidth disabled={submitting || formik.isSubmitting}>
        {submitting || formik.isSubmitting ? (
          <CircularProgress size={28} />
        ) : 'Sign in'}
      </Button>
    </form>
  );
}

export default LoginForm;
