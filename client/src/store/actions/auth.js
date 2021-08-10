import { push } from 'connected-react-router';
import jwtDecode from 'jwt-decode';

import { IS_FIRST_LOG_IN, LAST_PATH } from 'src/constants/localStorageKeys';
import authService from 'src/services/authService';
import { requestFail, requestPending, requestSuccess } from 'src/utils/api';
import {
  LOGIN_REQUEST,
  LOGOUT_REQUEST,
  SET_PROFILE,
} from '../types';

export function login(data) {
  return async (dispatch) => {
    try {
      dispatch({ type: requestPending(LOGIN_REQUEST) });

      const response = await authService.login({
        username: data.username,
        password: data.password,
      });
      const { refresh, access } = response.data;
      localStorage.setItem('token', access);
      localStorage.setItem('refreshToken', refresh);

      const user = jwtDecode(access);

      dispatch({
        type: requestSuccess(LOGIN_REQUEST),
        payload: { user },
      });

      // Check session storage if the last visited session saved or not
      // If not saved, go to dashboard, or go to last visited page and delete it
      let lastPath = null;
      // Check if user first time or not
      let isFirstTime = true;
      if (window !== undefined || window !== null) {
        lastPath = window.sessionStorage.getItem(LAST_PATH, null);
        window.sessionStorage.setItem(LAST_PATH, null);

        // For now just check local storage
        isFirstTime = window.localStorage.getItem(IS_FIRST_LOG_IN);
      }

      if (lastPath !== null) {
        dispatch(push(lastPath));
      } else if (isFirstTime) { // If user first login, go to basic information input page
        dispatch(push('/business/basic-info'));
      } else {
        dispatch(push('/main/dashboard'));
      }
    } catch (error) {
      dispatch({
        type: requestFail(LOGIN_REQUEST),
        payload: error.response?.data?.message || 'Invalid credentials',
      });
    }
  };
}

export function logout() {
  return async (dispatch) => {
    try {
      localStorage.clear();
      dispatch({ type: LOGOUT_REQUEST });
      dispatch(push('/login'));
    } catch (error) {
      dispatch({
        type: requestFail(LOGOUT_REQUEST),
        payload: error.response.data,
      });
    }
  };
}

export function setProfile(payload) {
  return (dispatch) => {
    dispatch({
      type: SET_PROFILE,
      payload,
    });
  };
}
