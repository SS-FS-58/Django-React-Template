import * as Yup from 'yup';

export default Yup.object().shape({
  business_name: Yup.string().max(255).required('Business Name is required'),
  address_1: Yup.string().required('Address is required'),
  city: Yup.string().required('City is required'),
  state: Yup.string().required('State is required'),
  zipcode: Yup.string().required('Zipcode is required'),
  phone_number: Yup.string().required('Phone number is required'),
  email: Yup.string().email().required('Email is required'),
  sector: Yup.array().required('Sector(s) is required'),
  industry: Yup.string().required('Industry is required'),
});
