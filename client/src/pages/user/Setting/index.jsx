import * as React from 'react';
import { useDispatch } from 'react-redux';
// import { useHistory } from 'react-router-dom';
import {
  Box,
  Button,
  Card,
  CardActions,
  CardContent,
  Container,
  Divider,
  Grid,
  Typography,
} from '@material-ui/core';
import { useFormik } from 'formik';

import { InputField } from 'src/components';
import { userSettings } from 'src/store/actions/user';

import validationSchema from './schema';
import useStyles from './style';

function Setting() {
  // const history = useHistory();
  const dispatch = useDispatch();

  const classes = useStyles();

  const handleSubmit = async (values) => {
    await dispatch(
      userSettings(values),
    );
  };

  const formik = useFormik({
    initialValues: {
      first_name: '',
      last_name: '',
      phone_number: '',
      email: '',
      password: '',
      password2: '',
      old_password: '',
    },
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <Container maxWidth="lg">
      <form onSubmit={formik.handleSubmit}>
        <Typography variant="h4">User Setting</Typography>
        <Divider />
        <Card elevation={1}>
          <CardContent>
            <Typography variant="h6" style={{ marginBottom: 16 }}>Setting</Typography>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Frist Name:
                </Typography>
                <InputField
                  formik={formik}
                  label="First Name"
                  name="first_name"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Last Name:
                </Typography>
                <InputField
                  formik={formik}
                  label="Last Name"
                  name="last_name"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Phone Number:
                </Typography>
                <InputField
                  formik={formik}
                  label="Phone Number"
                  name="phone_number"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Email:
                </Typography>
                <InputField
                  formik={formik}
                  type="email"
                  label="Email"
                  name="email"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Password :
                </Typography>
                <InputField
                  formik={formik}
                  type="password"
                  label="Password"
                  name="password"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Retype Password :
                </Typography>
                <InputField
                  formik={formik}
                  type="password"
                  label="Retype Password"
                  name="password2"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Old Password :
                </Typography>
                <InputField
                  formik={formik}
                  type="password"
                  label="Old Password"
                  name="old_password"
                />
              </Grid>
            </Grid>
          </CardContent>
          <CardActions>
            <Box display="flex" justifyContent="flex-end" width="100%" marginBottom="16px">
              <Button type="submit" color="primary" variant="contained">
                Update
              </Button>
            </Box>
          </CardActions>
        </Card>
      </form>
    </Container>
  );
}

export default Setting;
