import React from 'react'
import { Route } from "react-router-dom"
import { Counter, Todo } from 'components/index'


function App() {
  return (
    <div>
      <Route exact path='/' component={Counter}/>
      <Route exact path='/' component={Todo}/>                 
    </div>
  );
}

export default App;
