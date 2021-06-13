import { createStore } from 'redux'
import TodoReducer from 'store/TodoReducer'
export { default as TodoReducer } from 'store/TodoReducer'
export const store = createStore(TodoReducer)
