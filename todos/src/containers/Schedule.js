import React from 'react'
import { Todoinput, Todolist } from 'components/index'
import { Provider } from 'react-redux'
import { store } from 'store'


const Schedule = () => {
    return(<>
    <Provider store={store}>
        <Todoinput/>
        <Todolist/>
    </Provider>
    </>)
}

export default Schedule