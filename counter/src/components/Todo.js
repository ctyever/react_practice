import React, { useState } from 'react'


const Todo = () => {

    
    const [ item, setItem ] = useState('')

   

    return(<>
    <h1>할일목록</h1>
    <h4>{ item }</h4>         
    <input onChange={ (e) => { setItem(e.target.value) } }/>
    <button onClick={ () => setItem('')}>할일완료</button>
    </>)
}

export default Todo