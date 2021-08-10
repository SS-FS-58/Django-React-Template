import { createReducer } from '@reduxjs/toolkit';

import { requestSuccess, requestPending, requestFail } from 'src/utils/api';
import {
  BASIC_INFO_REQUEST, CONDITION_REQUEST, FINANCE_REQUEST, PREFERENCE_REQUEST, SET_PREFERENCE_1,
} from '../types';

/**
 * Initial state
 */
const initialState = {
  basicInfo: null,
  businessCondition: null,
  businessFinance: null,
  businessPreference1: null,
  cashFlow: [],
  balanceSheet: [],
  incomeStatement: [],
  status: 'INIT',
  error: null,
};

/**
 * Create reducers
 */

export default createReducer(initialState, {
  [requestSuccess(BASIC_INFO_REQUEST)]: (state, { payload }) => ({
    ...state,
    basicInfo: payload,
    status: requestSuccess(BASIC_INFO_REQUEST),
  }),

  [requestFail(BASIC_INFO_REQUEST)]: (state, { payload }) => ({
    ...state,
    basicInfo: null,
    error: payload,
    status: requestFail(BASIC_INFO_REQUEST),
  }),

  [requestPending(BASIC_INFO_REQUEST)]: (state) => ({
    ...state,
    basicInfo: null,
    error: null,
    status: requestPending(BASIC_INFO_REQUEST),
  }),

  // Handleing Business Condition Request
  [requestSuccess(CONDITION_REQUEST)]: (state, { payload }) => ({
    ...state,
    businessCondition: payload,
    status: requestSuccess(CONDITION_REQUEST),
  }),

  [requestFail(CONDITION_REQUEST)]: (state, { payload }) => ({
    ...state,
    businessCondition: null,
    error: payload,
    status: requestFail(CONDITION_REQUEST),
  }),

  [requestPending(CONDITION_REQUEST)]: (state) => ({
    ...state,
    businessCondition: null,
    error: null,
    status: requestPending(CONDITION_REQUEST),
  }),

  // Handleing Business Finance Request
  [requestSuccess(FINANCE_REQUEST)]: (state, { payload }) => ({
    ...state,
    businessFinance: payload,
    status: requestSuccess(FINANCE_REQUEST),
  }),

  [requestFail(FINANCE_REQUEST)]: (state, { payload }) => ({
    ...state,
    businessFinance: null,
    error: payload,
    status: requestFail(FINANCE_REQUEST),
  }),

  [requestPending(FINANCE_REQUEST)]: (state) => ({
    ...state,
    businessFinance: null,
    error: null,
    status: requestPending(FINANCE_REQUEST),
  }),

  // Handleing Business Preference1 Data
  [SET_PREFERENCE_1]: (state, { payload }) => ({
    ...state,
    businessPreference1: payload,
    status: SET_PREFERENCE_1,
  }),
  // Handleing Business Preference Request
  [requestSuccess(PREFERENCE_REQUEST)]: (state, { payload }) => ({
    ...state,
    businessCondition: payload,
    status: requestSuccess(PREFERENCE_REQUEST),
  }),

  [requestFail(PREFERENCE_REQUEST)]: (state, { payload }) => ({
    ...state,
    businessCondition: null,
    error: payload,
    status: requestFail(PREFERENCE_REQUEST),
  }),

  [requestPending(PREFERENCE_REQUEST)]: (state) => ({
    ...state,
    businessCondition: null,
    error: null,
    status: requestPending(PREFERENCE_REQUEST),
  }),
});
