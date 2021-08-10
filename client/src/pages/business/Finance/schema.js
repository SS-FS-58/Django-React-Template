/* eslint-disable max-len */
import * as Yup from 'yup';

const schema = Yup.object().shape({
  annual_gross_revenue: Yup.number().required('Annual Revenue Required'),
  annual_gross_profit: Yup.number().required('Annual Profit Required'),
  cash_ratio: Yup.number().required('Cash Ratio Required'),
  quick_ratio: Yup.number().required('Quick Ratio Required'),
  cash_position: Yup.number().required('Cash Position Required'),
  total_debt: Yup.number().required('Total Debt Required'),
  annual_free_cashflow: Yup.number().required('Annual Free Cashflow Required'),
  month_of_fiscal_year_end: Yup.number().required('Month of Fiscal Year-end Required'),
  total_business_worth: Yup.number().required('Total Worth Required'),
  // combined: Yup.object().shape({
  //   2021: Yup.mixed().test('fileRequired', 'Combined 2021 doc is required', (value) => {
  //     if (!value) return false;
  //     return true;
  //   }),
  //   2020: Yup.mixed().test('fileRequired', 'Combined 2020 doc is required', (value) => {
  //     if (!value) return false;
  //     return true;
  //   }),
  //   2019: Yup.mixed().test('fileRequired', 'Combined 2019 doc is required', (value) => {
  //     if (!value) return false;
  //     return true;
  //   }),
  // }),
  income_statement: Yup.object().shape({
    2021: Yup.mixed().test('fileRequired', 'Income Statement 2021 doc is required', (value) => {
      if (!value) return false;
      return true;
    }),
    // 2020: Yup.mixed().test('fileRequired', 'Income Statement 2020 doc is required', (value) => {
    //   if (!value) return false;
    //   return true;
    // }),
    // 2019: Yup.mixed().test('fileRequired', 'Income Statement 2019 doc is required', (value) => {
    //   if (!value) return false;
    //   return true;
    // }),
  }),
  balance_sheet: Yup.object().shape({
    2021: Yup.mixed().test('fileRequired', 'Balance Sheet 2021 doc is required', (value) => {
      if (!value) return false;
      return true;
    }),
    // 2020: Yup.mixed().test('fileRequired', 'Balance Sheet 2020 doc is required', (value) => {
    //   if (!value) return false;
    //   return true;
    // }),
    // 2019: Yup.mixed().test('fileRequired', 'Balance Sheet 2019 doc is required', (value) => {
    //   if (!value) return false;
    //   return true;
    // }),
  }),
  cashflow: Yup.object().shape({
    2021: Yup.mixed().test('fileRequired', 'Cash Flow 2021 doc is required', (value) => {
      if (!value) return false;
      return true;
    }),
    // 2020: Yup.mixed().test('fileRequired', 'Cash Flow 2020 doc is required', (value) => {
    //   if (!value) return false;
    //   return true;
    // }),
    // 2019: Yup.mixed().test('fileRequired', 'Cash Flow 2019 doc is required', (value) => {
    //   if (!value) return false;
    //   return true;
    // }),
  }),
});

export default schema;
