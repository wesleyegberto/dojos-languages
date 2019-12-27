import { actionTypes } from '../constants/action-types.js';

const initialState = { status: '' };

export const statusReducer = (state = initialState, action) => {
    switch (action.type) {
        case actionTypes.CHANGE_STATUS:
            return Object.assign({}, state, { status: action.payload });
        default:
            return state;
    }
};