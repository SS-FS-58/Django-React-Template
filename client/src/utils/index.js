import { cloneDeep } from 'lodash';
import moment from 'moment';

export const capitalize = (str) => str.replace(/\w\S*/g, (w) => (w.replace(/^\w/, (c) => c.toUpperCase())));

export const currencyFormat = (number = 0, fractions = 2) => Number(number).toLocaleString('en-US', {
  style: 'currency',
  currency: 'USD',
  minimumFractionDigits: fractions,
  maximumFractionDigits: fractions,
});

export const percentageFormat = (number = 0, fractions = 2) => Number(number).toLocaleString('en-US', {
  style: 'percent',
  minimumFractionDigits: fractions,
  maximumFractionDigits: fractions,
});

export const dateFormat = (date) => {
  if (!date) return date;
  return moment(date).format('MM/DD/YYYY');
};

export const formatPhoneNumber = (str) => {
  const cleaned = (`${str}`).replace(/\D/g, '');
  const match = cleaned.match(/^(1|)?(\d{3})(\d{3})(\d{4})$/);
  if (match) {
    const intlCode = (match[1] ? '+1 ' : '');
    return [intlCode, '(', match[2], ') ', match[3], '-', match[4]].join('');
  }
  return null;
};

export const snakeToCamel = (key) => key.replace(/_([a-z])/g, (group) => group[1].toUpperCase());

export const camelToSnake = (key) => key.replace(/([a-z])([A-Z])/g, '$1_$2').toLowerCase();

/**
 * Convert snakecase to camelcase
 * @param {Object} data
 */
export const serializeKeys = (data) => {
  if (typeof data !== 'object' || data == null) return data;

  if (Array.isArray(data)) {
    data.forEach((_, index) => {
      data[index] = serializeKeys(data[index]);
    });
  } else {
    Object.keys(data).forEach((key) => {
      data[snakeToCamel(key)] = serializeKeys(data[key]);
      if (/_([a-z])/.test(key)) delete data[key];
    });
  }

  return data;
};

/**
 * Convert camelcase to snakecase
 * @param {Object} data
 */
export const deserializeKeys = (data) => {
  if (typeof data !== 'object' || data == null) return data;

  const newData = cloneDeep(data);
  if (Array.isArray(newData)) {
    newData.forEach((_, index) => {
      newData[index] = deserializeKeys(newData[index]);
    });
  } else {
    Object.keys(newData).forEach((key) => {
      newData[camelToSnake(key)] = deserializeKeys(newData[key]);
      if (/([a-z])([A-Z])/.test(key)) delete newData[key];
    });
  }

  return newData;
};

export const isValidDate = (d) => {
  if (Object.prototype.toString.call(d) === '[object Date]') {
    // it is a date
    if (Number.isNaN(d.getTime())) {
      return false;
    }
    return true;
  }
  return false;
};
