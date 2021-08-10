export const requestSuccess = (type) => `${type}/success`;

export const requestPending = (type) => `${type}/pending`;

export const requestFail = (type) => `${type}/fail`;

export const isActionTypeFail = (actionType) => {
  if (actionType && typeof actionType === 'string') {
    return actionType.endsWith('/fail');
  }
  return true;
};
