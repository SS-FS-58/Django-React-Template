import * as Yup from 'yup';

export default Yup.object().shape({
  username: Yup.string().max(255).required('User Name is required'),
  password: Yup.string().max(255).required('Password is required'),
});
