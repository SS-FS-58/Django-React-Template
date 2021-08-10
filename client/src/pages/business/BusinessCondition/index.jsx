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
import { businessCondition } from 'src/store/actions/business';

import { InputField } from 'src/components';
import {
  COMPANY_FORMATIONS,
  BUSINESS_MODELS,
  CORE_COMPETITIVENESS,
  TOP_RISKS,
  RIVALRY_SECTORS,
} from 'src/constants';

import validationSchema from './schema';
import useStyles from './style';

function BusinessCondition() {
  const dispatch = useDispatch();

  const classes = useStyles();

  const handleSubmit = async (values) => {
    await dispatch(
      businessCondition(values),
    );
  };

  const formik = useFormik({
    initialValues: {
      companyFormation: '',
      businessModel: '',
      technologyLeverage: 0,
      competitiveness: [
        '',
        '',
        '',
      ],
      businessGrowth: {
        2020: 0,
        2021: 0,
        2022: 0,
      },
      risks: [
        '',
        '',
        '',
      ],
      rivalrySector: '',
      competitors: [
        '',
        '',
        '',
      ],
      supplyChainRisk: '',
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
            <Typography variant="h6" style={{ marginBottom: 16 }}>Business Condition</Typography>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  Company Formation:
                </Typography>
                <InputField
                  formik={formik}
                  type="select"
                  label="Company Formation"
                  name="companyFormation"
                  options={COMPANY_FORMATIONS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12}>
                <Typography className={classes.spacing} variant="body1">
                  Based on Industry & Sector, How Would You Describe Your Business Model:
                </Typography>
                <InputField
                  formik={formik}
                  type="select"
                  label="Business Model"
                  name="businessModel"
                  options={BUSINESS_MODELS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <Typography className={classes.spacing} variant="body1">
                  How Much Do You Leverage On New Technologies to Grow Your Business (0 ~ 10):
                </Typography>
                <InputField
                  formik={formik}
                  type="select"
                  label="Technology Leverage"
                  name="technologyLeverage"
                  options={new Array(11).fill(0)
                    .map((_, index) => ({ label: index, value: index }))}
                />
              </Grid>
              <Grid item sm={6} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Top 3 Core Competitiveness:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Core Competitiveness 1"
                  name="competitiveness[0]"
                  options={CORE_COMPETITIVENESS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Core Competitiveness 2"
                  name="competitiveness[1]"
                  options={CORE_COMPETITIVENESS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Core Competitiveness 3"
                  name="competitiveness[2]"
                  options={CORE_COMPETITIVENESS.map((value) => ({ label: value, value }))}
                />
              </Grid>

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  How Would You Describe Your Business Decline/Growth(-10 ~ +10):
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="2020"
                  name="businessGrowth.2020"
                  options={new Array(21).fill(0)
                    .map((_, index) => ({ label: index - 10, value: index - 10 }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="2021"
                  name="businessGrowth.2021"
                  options={new Array(21).fill(0)
                    .map((_, index) => ({ label: index - 10, value: index - 10 }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="2022"
                  name="businessGrowth.2022"
                  options={new Array(21).fill(0)
                    .map((_, index) => ({ label: index - 10, value: index - 10 }))}
                />
              </Grid>

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Your Top 3 Biggest Risk(s) & Concern(s) Are:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Top Risk 1"
                  name="risks[0]"
                  options={TOP_RISKS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Top Risk 2"
                  name="risks[1]"
                  options={TOP_RISKS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Top Risk 3"
                  name="risks[2]"
                  options={TOP_RISKS.map((value) => ({ label: value, value }))}
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <Typography className={classes.spacing} variant="body1">
                  Name a Rivalry Sector Against Your Business:
                </Typography>
                <InputField
                  formik={formik}
                  type="select"
                  label="Rivalry Sector"
                  name="rivalrySector"
                  options={RIVALRY_SECTORS.map((value) => ({ label: value, value }))}
                  l
                />
              </Grid>
              <Grid item sm={8} />

              <Box width="100%" marginLeft="12px" marginBottom="-4px">
                <Typography variant="body1">
                  Name Your Top 3 Competitors:
                </Typography>
              </Box>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  label="Competitor 1"
                  name="competitors[0]"
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  label="Competitor 2"
                  name="competitors[1]"
                />
              </Grid>
              <Grid item xs={12} sm={4}>
                <InputField
                  formik={formik}
                  label="Competitor 2"
                  name="competitors[2]"
                />
              </Grid>
              <Grid item xs={12}>
                <Typography className={classes.spacing} variant="body1">
                  Supply Chain & Procurement Risks:
                </Typography>
                <InputField
                  formik={formik}
                  label="Supply Chain & Procurement Risks"
                  name="supplyChainRisk"
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

export default BusinessCondition;
