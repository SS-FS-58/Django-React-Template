import axios from 'src/utils/axios';

class BusinessService {
  basicInfo = async (data) => {
    try {
      const response = await axios.post('/business/business_basic/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  businessCondition = async (data) => {
    try {
      const response = await axios.post('/business/business_condition/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  businessFinance = async (data) => {
    try {
      const response = await axios.post('/business/business_finance/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  businessIncome = async (data) => {
    try {
      const response = await axios.post('/business/income_statement/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  busienssCashflow = async (data) => {
    try {
      const response = await axios.post('/business/business_cashflow/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  businessBalancesheet = async (data) => {
    try {
      const response = await axios.post('/business/balance_sheet/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  businessPreference = async (data) => {
    try {
      const response = await axios.post('/business/business_preference/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };
}

const businessService = new BusinessService();

export default businessService;
