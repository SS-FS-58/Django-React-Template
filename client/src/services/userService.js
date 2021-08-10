import axios from 'src/utils/axios';

class UserService {
  userSettings = async (data) => {
    try {
      const response = await axios.post('/user/user_settings/', data);
      if (response.status >= 200 && response.status < 500) {
        return response.data;
      }
      throw new Error(response.data);
    } catch (error) {
      throw error;
    }
  };
}

const userService = new UserService();

export default userService;
