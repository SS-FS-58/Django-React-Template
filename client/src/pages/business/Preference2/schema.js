import * as Yup from 'yup';

export default Yup.object().shape({
  majorSpending: Yup.string().required('Spending is required'),
  amountSpending: Yup.number().required('Amount ($) is required'),
  amountAssets: Yup.number().required('Amount ($) is required'),
  choice1: Yup.string().required('Choice is required'),
  choice2: Yup.string().required('Choice is required'),
  choice3: Yup.string().required('Choice is required'),
  time: Yup.string().required('Time is required'),
});
