import * as Yup from 'yup';

export default Yup.object().shape({
  // name: Yup.string().max(255).required('Name is required'),
  // phone_number: Yup.string().required('Phone number is required'),
  // email: Yup.string().email().required('Email is required'),
  // password: Yup.string().max(255).required('Password is required'),
});
