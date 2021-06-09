import { Route } from 'react-router-dom'
import { Todoinput } from './components/index'



const App = () => {
  return(
  <div>
    <Route exact path='/' component={Todoinput}/>   
  </div>)
}

export default App