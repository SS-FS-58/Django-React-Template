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
  TextField,
  Typography,
} from '@material-ui/core';
import { Autocomplete } from '@material-ui/lab';
import { useFormik } from 'formik';

import { InputField } from 'src/components';
import { basicInfo } from 'src/store/actions/business';

import validationSchema from './schema';

const SECTORS = [
  'SECTOR 1',
  'SECTOR 2',
  'SECTOR 3',
  'SECTOR 4',
  'SECTOR 5',
];

function BasicInfo() {
  // const history = useHistory();
  const dispatch = useDispatch();

  const handleSubmit = async (values) => {
    await dispatch(
      basicInfo(values),
    );
  };

  const formik = useFormik({
    initialValues: {
      business_name: '',
      address_1: '',
      address_2: '',
      city: '',
      state: '',
      zipcode: '',
      phone_number: '',
      email: '',
      website: '',
      sector: [],
      industry: '',
      number_of_employees: 0,
      description_of_business: '',
    },
    validationSchema,
    onSubmit: handleSubmit,
  });

  const handleChangeSectors = (event, values) => {
    formik.setFieldValue('sector', values);
  };

  return (
    <Container maxWidth="lg">
      <form onSubmit={formik.handleSubmit}>
        <Typography variant="h4">Business</Typography>
        <Divider />
        <Card elevation={1}>
          <CardContent>
            <Typography variant="h6" style={{ marginBottom: 16 }}>Basic Info</Typography>
            <Grid container spacing={3}>
              <Grid item xs={12}>
                <InputField
                  formik={formik}
                  label="Business Name"
                  name="business_name"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  label="Address"
                  name="address_1"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  label="Address Line2"
                  name="address_2"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  label="City"
                  name="city"
                />
              </Grid>
              <Grid item xs={12} sm={6} md={3}>
                <InputField
                  formik={formik}
                  type="select"
                  label="State"
                  name="state"
                  options={[
                    { label: 'California', value: 'CA' },
                    { label: 'New York', value: 'NY' },
                  ]}
                />
              </Grid>
              <Grid item xs={12} sm={6} md={3}>
                <InputField
                  formik={formik}
                  label="Zip"
                  name="zipcode"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  label="Phone Number"
                  name="phone_number"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  type="email"
                  label="Email"
                  name="email"
                />
              </Grid>
              <Grid item xs={12}>
                <InputField
                  formik={formik}
                  label="Website"
                  name="website"
                />
              </Grid>
              <Grid item xs={12}>
                <Autocomplete
                  multiple
                  options={SECTORS}
                  onChange={handleChangeSectors}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      variant="outlined"
                      label="Sector(s)"
                    />
                  )}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  label="Industry"
                  name="industry"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  type="number"
                  label="Number of Employees"
                  name="number_of_employees"
                />
              </Grid>
              <Grid item xs={12}>
                <InputField
                  formik={formik}
                  label="Description of Business"
                  name="description_of_business"
                  multiline
                  rows={5}
                />
              </Grid>
            </Grid>
          </CardContent>
          <CardActions>
            <Box display="flex" justifyContent="flex-end" width="100%" marginBottom="16px">
              <Button type="submit" color="primary" variant="contained">
                Next
              </Button>
            </Box>
          </CardActions>
        </Card>
      </form>
    </Container>
  );
}

export default BasicInfo;
