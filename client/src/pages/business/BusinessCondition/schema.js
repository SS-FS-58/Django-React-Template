import * as Yup from 'yup';

export default Yup.object().shape({
  companyFormation: Yup.string().required('Company Formation is required'),
  businessModel: Yup.string().required('Business Model is required'),
  technologyLeverage: Yup.number().required('New technologies Leverage is required'),
  competitiveness: Yup.array().required('Core Competitiveness are required'),
  businessGrowth: Yup.object().shape({
    2020: Yup.number().required('Business Decline/Growth is required'),
  }),
  risks: Yup.array().required('Biggest Risk(s) & Concern(s) are required'),
  rivalrySector: Yup.string().required('Rivalry Sector is required'),
  competitors: Yup.array().required('Competitors are required'),
  supplyChainRisk: Yup.string().required('Supply Chain & Procurement Risk is required'),
});
