import axios from 'src/utils/axios';

class MarketService {
  yahooAutoComplete = async (data) => {
    try {
      const response = await axios.post('/market/yahoo/auto-complete/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  yahooMarketSummary = async (data) => {
    try {
      const response = await axios.post('/market/yahoo/market/get-summary/', data);
      if (response && response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  yahooMarketAutoComplete = async (data) => {
    try {
      const response = await axios.post('/market/yahoo/market/auto-complete/', data);
      if (response && response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  yahooStockSummary = async (data) => {
    try {
      const response = await axios.post('/market/yahoo/stock/get-summary/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };
}

const marketService = new MarketService();

export default marketService;
