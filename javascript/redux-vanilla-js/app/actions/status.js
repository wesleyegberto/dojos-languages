import { actionTypes } from '../constants/action-types.js';

export const changeStatus = userName => {
	return dispatch => {
		setTimeout(() => dispatch({
			type: actionTypes.CHANGE_STATUS,
			payload: `${userName} is typing`
		}), 500);
	};
};