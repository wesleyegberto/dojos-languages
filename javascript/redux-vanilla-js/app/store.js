import { createStore, applyMiddleware, compose } from 'redux';
import { createLogger  } from 'redux-logger';
import thunk from 'redux-thunk';

import { statusReducer } from './reducers/status-reducer';

const middlewares = compose(
	applyMiddleware(thunk, createLogger()),
	// enable time travel debugging
	window.devToolsExtension ? window.devToolsExtension() : f => f
);
export const store = createStore(statusReducer, middlewares);