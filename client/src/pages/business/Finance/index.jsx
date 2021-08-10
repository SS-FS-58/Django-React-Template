/* eslint-disable no-unused-vars */
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
import {
  businessBalance, businessCash, businessFinance, businessIncome,
} from 'src/store/actions/business';

import { parseCSV } from 'src/utils/csvUtil';
import { InputField } from 'src/components';
import { MONTHS } from 'src/constants';

import validationSchema from './schema';

function readFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const result = parseCSV(e.target.result);
      resolve(result);
    };
    reader.onerror = () => {
      reject(new Error('Error on file read!!!'));
    };
    reader.readAsText(file);
  });
}

function Finance() {
  const dispatch = useDispatch();

  const processFiles = (files, type) => {
    const promises = Object.entries(files)
      .filter(([, value]) => !!value)
      .map(async ([year, value]) => {
        try {
          const content = await readFile(value);
          let promise;
          if (type === 'balance_sheet') {
            promise = dispatch(
              businessBalance({ ...content[0], year }),
            );
          } else if (type === 'income_statement') {
            promise = dispatch(
              businessIncome({ ...content[0], year }),
            );
          } else if (type === 'cashflow') {
            promise = dispatch(
              businessCash({ ...content[0], year }),
            );
          } else {
            throw new Error('Unsupported type');
          }
          const { id } = await promise;
          return {
            result: true,
            type,
            year,
            id,
          };
        } catch (error) {
          return { result: false, type, year };
        }
      });

    return Promise.all(promises);
  };

  const handleSubmit = (values) => {
    console.log(values);
    Promise.all([
      // processFiles(values.combined, 'combined'),
      processFiles(values.income_statement, 'income_statement'),
      processFiles(values.cashflow, 'cashflow'),
      processFiles(values.balance_sheet, 'balance_sheet'),
    ]).then((res) => res.flat(1)).then((results) => {
      results.forEach((result) => {
        if (result.result) {
          values[`${result.type}_${result.year}_id`] = result.id;
        }
      });
      dispatch(
        businessFinance(values),
      );
    });
  };

  const formik = useFormik({
    initialValues: {
      annual_gross_revenue: 0,
      annual_gross_profit: 0,
      cash_ratio: 0,
      quick_ratio: 0,
      cash_position: 0,
      total_debt: 0,
      annual_free_cashflow: 0,
      month_of_fiscal_year_end: 1,
      total_business_worth: 0,
      combined: {
        2021: null,
        2020: null,
        2019: null,
      },
      income_statement: {
        2021: null,
        2020: null,
        2019: null,
      },
      balance_sheet: {
        2021: null,
        2020: null,
        2019: null,
      },
      cashflow: {
        2021: null,
        2020: null,
        2019: null,
      },
    },
    validationSchema,
    onSubmit: handleSubmit,
  });

  return (
    <Container maxWidth="lg">
      <form onSubmit={formik.handleSubmit}>
        <Typography variant="h4">Finance</Typography>
        <Divider />
        <Card elevation={1}>
          <CardContent>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Annual Gross Revenue K"
                  name="annual_gross_revenue"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Annual Gross Proft(+)/Loss(-) K"
                  name="annual_gross_profit"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Cash Ratio(Approximate) %"
                  name="cash_ratio"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Quick Ratio(Approximate) %"
                  name="quick_ratio"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Cash Position(Approximate) K"
                  name="cash_position"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Total Debt K"
                  name="total_debt"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Annual Free Cashflow K"
                  name="annual_free_cashflow"
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <InputField
                  formik={formik}
                  type="select"
                  label="Month of Fiscal Year-end"
                  name="month_of_fiscal_year_end"
                  options={MONTHS}
                />
              </Grid>
              <Grid item xs={12}>
                <InputField
                  type="number"
                  formik={formik}
                  label="Total (Approx) Worth (Tangible & Non-Tangible) of Your Business"
                  name="total_business_worth"
                />
              </Grid>
              <Grid item xs={12}>
                <Typography>Upload Finalcial Statement(s) 2021</Typography>
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Combined"
                  name="combined.2021"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Income Statement"
                  name="income_statement.2021"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Balance Sheet"
                  name="balance_sheet.2021"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Cash Flow"
                  name="cashflow.2021"
                />
              </Grid>
              <Grid item xs={12}>
                <Typography>Upload Finalcial Statement(s) 2020</Typography>
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Combined"
                  name="combined.2020"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Income Statement"
                  name="income_statement.2020"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Balance Sheet"
                  name="balance_sheet.2020"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Cash Flow"
                  name="cashflow.2020"
                />
              </Grid>

              <Grid item xs={12}>
                <Typography>Upload Finalcial Statement(s) 2019</Typography>
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Combined"
                  name="combined.2019"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Income Statement"
                  name="income_statement.2019"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Balance Sheet"
                  name="balance_sheet.2019"
                />
              </Grid>
              <Grid item xs={12} sm={3}>
                <InputField
                  type="file"
                  variant="contained"
                  formik={formik}
                  label="Cash Flow"
                  name="cashflow.2019"
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

export default Finance;
