import { push } from 'connected-react-router';
import userService from 'src/services/userService';
import { requestFail, requestPending, requestSuccess } from 'src/utils/api';
import {
  USER_SETTING,
} from '../types';

// eslint-disable-next-line import/prefer-default-export
export function userSettings(data) {
  return async (dispatch) => {
    try {
      dispatch({ type: requestPending(USER_SETTING) });
      const response = await userService.userSettings({
        ...data,
      });
      dispatch({
        type: requestSuccess(USER_SETTING),
        payload: response.data,
      });
      dispatch(push('/user/setting'));
    } catch (error) {
      dispatch({
        type: requestFail(USER_SETTING),
        payload: error.response?.data || 'Invalid User Setting info',
      });
    }
  };
}
