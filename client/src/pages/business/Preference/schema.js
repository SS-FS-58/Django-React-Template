import * as Yup from 'yup';

export default Yup.object().shape({
  riskTolerance: Yup.string().required('Risk Tolerance is required'),
  expectedDuration: Yup.string().required('Expired Duration is required'),
  preferredSector0: Yup.string().required('Preferred Sector is required'),
});
