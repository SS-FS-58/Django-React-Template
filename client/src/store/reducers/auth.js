import { createReducer } from '@reduxjs/toolkit';

import { requestSuccess, requestFail } from 'src/utils/api';
import {
  LOGIN_REQUEST,
  LOGOUT_REQUEST,
  SET_PROFILE,
} from '../types';

/**
 * Initial state
 */
const initialState = {
  profile: null,
  status: 'INIT',
  error: null,
};

/**
 * Create reducers
 */
export default createReducer(initialState, {
  [requestSuccess(LOGIN_REQUEST)]: (state, { payload }) => ({
    ...state,
    profile: payload.user,
    status: requestSuccess(LOGIN_REQUEST),
  }),

  [requestFail(LOGIN_REQUEST)]: (state, { payload }) => ({
    ...state,
    profile: null,
    error: payload,
    status: requestFail(LOGIN_REQUEST),
  }),

  [requestSuccess(LOGOUT_REQUEST)]: (state) => ({
    ...state,
    profile: null,
    error: null,
    status: requestSuccess(LOGOUT_REQUEST),
  }),

  [SET_PROFILE]: (state, { payload }) => ({
    ...state,
    profile: payload,
    status: SET_PROFILE,
  }),
});
