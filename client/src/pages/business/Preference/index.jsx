import * as React from 'react';
import { useDispatch } from 'react-redux';
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
import { businessPreference1 } from 'src/store/actions/business';

import { InputField } from 'src/components';
import {
  TOLERANCE_RISKS,
  EXPECTED_DURATIONS,
  INVESTOR_TYPES,
  COUNTRIES,
} from 'src/constants';

import validationSchema from './schema';

function Preference() {
  const dispatch = useDispatch();

  const handleSubmit = async (values) => {
    await dispatch(
      businessPreference1(values),
    );
  };

  const formik = useFormik({
    initialValues: {
      riskTolerance: '',
      expectedDuration: '',
      investorType: '',
      preferredSector0: 0,
      preferredSector1: 0,
      preferredSector2: 0,
      targetCashBalance: '',
      dislikedAssetClass: [0, 0, 0],
      interestedAssetClass: [0, 0, 0],
      countryRefused: ['', '', ''],
      countryInterested: ['', '', ''],
    },
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <Container maxWidth="lg">
      <form onSubmit={formik.handleSubmit}>
        <Typography variant="h4">Business</Typography>
        <Divider />
        <Card elevation={1}>
          <CardContent>
            <Typography variant="h6" style={{ marginBottom: 16 }}>Preference (Part 1):</Typography>
            <Grid container spacing={3}>
              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  How Would You Describe Your Risk Tolerance Level (0~10), if in
                  Inverse Correlation with Rewards:
                </Typography>
              </Box>
              <Grid item xs={12} sm={10}>
                <InputField
                  formik={formik}
                  type="select"
                  name="riskTolerance"
                  options={TOLERANCE_RISKS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={2} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  What&apos;s Your Expected Duration till Maturity of Your Core Business Investment:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="expectedDuration"
                  options={EXPECTED_DURATIONS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={8} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  For Equity or Index Investment, Which of the Following Would You Describe
                  Yourself as:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="investorType"
                  options={INVESTOR_TYPES.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={8} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  What&apos;s Your Preferred Liquid Investment Industry Sector(s):
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="preferredSector0"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="preferredSector1"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="preferredSector2"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  What&apos;s Your Business&apos; Target Cash Balance?
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="number"
                  name="targetCashBalance"
                />
              </Grid>
              <Grid item sm={8} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Name up to 3 Sectors or Asset Classes You Strongly Dislike:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="dislikedAssetClass[0]"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="dislikedAssetClass[1]"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="dislikedAssetClass[2]"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Name up to 3 Sectors or Asset Classes Beyond Core Business Domain You
                  Are Interested in:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="interestedAssetClass[0]"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="interestedAssetClass[1]"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="interestedAssetClass[2]"
                  options={new Array(5).fill(0).map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Name up to 3 Countries and Markets You Refuse to Involve in:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="countryRefused[0]"
                  options={COUNTRIES.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="countryRefused[1]"
                  options={COUNTRIES.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="countryRefused[2]"
                  options={COUNTRIES.map((value) => ({ label: value, value }))}
                />
              </Grid>

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Name up to 3 Countries and Markets beyond Your Home Country You Are Interested in:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="countryInterested[0]"
                  options={COUNTRIES.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="countryInterested[1]"
                  options={COUNTRIES.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="countryInterested[2]"
                  options={COUNTRIES.map((value) => ({ label: value, value }))}
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

export default Preference;
