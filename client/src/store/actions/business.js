import { push } from 'connected-react-router';
import businessService from 'src/services/businessService';
import { requestFail, requestPending, requestSuccess } from 'src/utils/api';
import {
  BASIC_INFO_REQUEST, CONDITION_REQUEST,
  FINANCE_REQUEST, PREFERENCE_REQUEST, SET_PREFERENCE_1,
} from '../types';

// eslint-disable-next-line import/prefer-default-export
export function basicInfo(data) {
  return async (dispatch) => {
    try {
      dispatch({ type: requestPending(BASIC_INFO_REQUEST) });
      const response = await businessService.basicInfo(data);
      dispatch({
        type: requestSuccess(BASIC_INFO_REQUEST),
        payload: response.data,
      });
      dispatch(push('/business/condition'));
    } catch (error) {
      dispatch({
        type: requestFail(BASIC_INFO_REQUEST),
        payload: error.response?.data || 'Invalid basic info',
      });
    }
  };
}

export function businessCondition(data) {
  return async (dispatch, getState) => {
    const { business } = getState();
    try {
      dispatch({ type: requestPending(CONDITION_REQUEST) });
      const response = await businessService.businessCondition({
        // Change request data fiedls to backend acceptable fields
        company_formation: data.companyFormation,
        business_model: data.businessModel,
        leverage_on_tech: data.technologyLeverage,
        competitiveness_1: data.competitiveness[0],
        competitiveness_2: data.competitiveness[1],
        competitiveness_3: data.competitiveness[2],
        growth_1: data.businessGrowth['2020'],
        growth_2: data.businessGrowth['2021'],
        growth_3: data.businessGrowth['2022'],
        top_risk_1: data.risks[0],
        top_risk_2: data.risks[1],
        top_risk_3: data.risks[2],
        rival_sector: data.rivalrySector,
        competitor_1: data.competitors[0],
        competitor_2: data.competitors[1],
        competitor_3: data.competitors[2],
        supplychain_risk: data.supplyChainRisk,
        business_basic_info_id: business.basicInfo?.id,
      });
      dispatch({
        type: requestSuccess(CONDITION_REQUEST),
        payload: response.data,
      });
      dispatch(push('/business/finance'));
    } catch (error) {
      dispatch({
        type: requestFail(CONDITION_REQUEST),
        payload: error.response?.data || 'Invalid business condition info',
      });
    }
  };
}

export function businessIncome(data) {
  return async () => {
    try {
      const response = await businessService.businessIncome(data);
      return response.data;
    } catch (error) {
      throw error;
    }
  };
}

export function businessCash(data) {
  return async () => {
    try {
      const response = await businessService.busienssCashflow(data);
      return response.data;
    } catch (error) {
      throw error;
    }
  };
}

export function businessBalance(data) {
  return async () => {
    try {
      const response = await businessService.businessBalancesheet(data);
      return response.data;
    } catch (error) {
      throw error;
    }
  };
}

export function businessFinance(data) {
  return async (dispatch, getState) => {
    const { business } = getState();
    try {
      dispatch({ type: requestPending(FINANCE_REQUEST) });
      const response = await businessService.businessFinance({
        // Change request data fiedls to backend acceptable fields
        ...data,
        business_basic_info_id: business.basicInfo?.id,
      });
      dispatch({
        type: requestSuccess(FINANCE_REQUEST),
        payload: response.data,
      });
      dispatch(push('/business/preference'));
    } catch (error) {
      dispatch({
        type: requestFail(FINANCE_REQUEST),
        payload: error.response?.data || 'Invalid business finance info',
      });
    }
  };
}

export function businessPreference1(data) {
  return (dispatch) => {
    // Save preference1 fiedls values for preference2 page api call
    dispatch({
      type: SET_PREFERENCE_1,
      payload: {
        risk_tolerance: data.riskTolerance,
        expected_duration: data.expectedDuration,
        investor_type: data.investorType,
        preferred_sector_1: data.preferredSector0,
        preferred_sector_2: data.preferredSector1,
        preferred_sector_3: data.preferredSector2,
        target_cash_balance: data.targetCashBalance,
        disliked_asset_class_1: data.dislikedAssetClass[0],
        disliked_asset_class_2: data.dislikedAssetClass[1],
        disliked_asset_class_3: data.dislikedAssetClass[2],
        interested_asset_class_1: data.interestedAssetClass[0],
        interested_asset_class_2: data.interestedAssetClass[1],
        interested_asset_class_3: data.interestedAssetClass[2],
        country_refused_1: data.countryRefused[0],
        country_refused_2: data.countryRefused[1],
        country_refused_3: data.countryRefused[2],
        country_interested_1: data.countryInterested[0],
        country_interested_2: data.countryInterested[1],
        country_interested_3: data.countryInterested[2],
      },
    });
    dispatch(push('/business/preference2'));
  };
}

export function businessPreference2(data) {
  return async (dispatch, getState) => {
    const { business } = getState();
    try {
      dispatch({ type: requestPending(PREFERENCE_REQUEST) });
      const response = await businessService.businessCondition({
        ...business?.businessPreference1,
        business_basic_info_id: business.basicInfo?.id,
        projected_major_spending: data.majorSpending,
        projected_spending_amt: data.amountSpending,
        cash_set_aside: data.amountAssets,
        _100k_1m_50percent: data.choice1,
        _100k_500k_50percen: data.choice2,
        _100k_1m_30percent: data.choice3,
        how_often_availability: data.time,
      });
      dispatch({
        type: requestSuccess(PREFERENCE_REQUEST),
        payload: response.data,
      });
      dispatch(push('/risk-analysis/financial-forecast'));
    } catch (error) {
      dispatch({
        type: requestFail(PREFERENCE_REQUEST),
        payload: error.response?.data || 'Invalid business preference info',
      });
    }
  };
}
