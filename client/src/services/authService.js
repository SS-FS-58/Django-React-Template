import axios from 'src/utils/axios';

class AuthService {
  login = async ({ username, password }) => {
    try {
      const response = await axios.post('/pauth/login/', { username, password });
      if (response.status >= 200 && response.status < 500) {
        return response;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };

  logout = async () => {
    try {
      const response = await axios.post('/logout');
      if (response.status >= 200 && response.status < 300) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  }
}

const authService = new AuthService();

export default authService;
