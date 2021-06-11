import React from 'react'
import { Todoinput, Todolist } from 'todos/components/index'
import { Provider } from 'react-redux'
import { store } from 'store/index'


const Schedule = () => {
    return(<>
    <Provider store={store}>
        <Todoinput/>
        <Todolist/>
    </Provider>
    </>)
}

export default Schedule