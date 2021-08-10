import { createReducer } from '@reduxjs/toolkit';

import { requestSuccess, requestFail, requestPending } from 'src/utils/api';
import {
  USER_SETTING,
} from '../types';

/**
 * Initial state
 */
const initialState = {
  userSettings: null,
  status: 'INIT',
  error: null,
};

/**
 * Create reducers
 */
export default createReducer(initialState, {
  [requestSuccess(USER_SETTING)]: (state, { payload }) => ({
    ...state,
    userSettings: payload.user,
    status: requestSuccess(USER_SETTING),
  }),

  [requestFail(USER_SETTING)]: (state, { payload }) => ({
    ...state,
    userSettings: null,
    error: payload,
    status: requestFail(USER_SETTING),
  }),

  [requestPending(USER_SETTING)]: (state) => ({
    ...state,
    userSettings: null,
    error: null,
    status: requestPending(USER_SETTING),
  }),

});
