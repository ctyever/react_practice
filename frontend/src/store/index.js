import { createStore } from 'redux'
export { todoReducer } from 'store/todoreducer'
export const store = createStore(todoReducer)
