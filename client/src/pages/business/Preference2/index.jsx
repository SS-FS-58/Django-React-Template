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
import { businessPreference2 } from 'src/store/actions/business';

import { InputField } from 'src/components';
import {
  SPENDING_AMOUNT,
  CHOICE1,
  CHOICE2,
  CHOICE3,
  TIME,
} from 'src/constants';

import validationSchema from './schema';

function Preference() {
  const dispatch = useDispatch();

  const handleSubmit = async (values) => {
    await dispatch(
      businessPreference2(values),
    );
  };

  const formik = useFormik({
    initialValues: {
      majorSpending: '',
      amountSpending: 0,
      amountAssets: 0,
      choice1: '',
      choice2: '',
      choice3: '',
      time: '',
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
            <Typography variant="h6" style={{ marginBottom: 16 }}>Preference (Part 2):</Typography>
            <Grid container spacing={3}>
              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  What Major Investment or Spending You Are Set to
                  Make Next 6-9 Months and What Amount (approx):
                </Typography>
              </Box>
              <Grid item container xs={12} sm={12} spacing={3}>
                <Grid item xs={6} sm={6}>
                  <InputField
                    formik={formik}
                    type="select"
                    name="majorSpending"
                    options={SPENDING_AMOUNT.map((value) => ({ label: value, value }))}
                  />
                </Grid>
                <Grid item xs={6} sm={6}>
                  <InputField
                    formik={formik}
                    type="number"
                    name="amountSpending"
                  />
                </Grid>
              </Grid>
              <Grid item sm={2} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  What Amount of Cash or Other Short Term Assets You Are Free to Set aside:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="number"
                  name="amountAssets"
                />
              </Grid>
              <Grid item sm={8} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  With $50k Capital of Yours at Risk, between $100k Guranteed Gain and
                  $1M Gain with 50%
                  <br />
                  Chance to win which would you pick:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="choice1"
                  options={CHOICE1.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={8} />
              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Under the same condition, what If It is $100k Guranteed vs $500k with 50% chance:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="choice2"
                  options={CHOICE2.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={8} />
              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Under the same condition, what If It is $100k Guranteed vs $1M with 30% chance:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="choice3"
                  options={CHOICE3.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item sm={8} />
              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  How often can you allocate at least 30 minutes without distraction
                  on our platform within the next 6-9 months:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  name="time"
                  options={TIME.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={12}>
                <Typography variant="body1">
                  Other Conditions or preference important to you? Email us at
                  contact@prussiananalytics.com:
                </Typography>
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
