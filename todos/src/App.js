import React from 'react'
import { Route } from 'react-router-dom'
import { Schedule } from 'containers/index'


function App() {
  return (
  <div>
    <Route exact path='/' component={ Schedule }/> 
  </div> 
  )
}

export default App;
