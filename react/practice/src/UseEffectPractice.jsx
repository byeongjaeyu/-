import React from 'react'
import {useEffect, useState} from 'react'

export default function UseEffectPractice() {
  const sayHello = () => console.log("hello");
  const [number,setNumber] = useState(0);
  const [aNumber,setAnumber] = useState(0);

  // componentdidmount
  useEffect(()=>{
    sayHello();
  },[])

  // componentwillupdate(number)
  useEffect(()=>{
    sayHello();
  },[number])

  return (
    <div>
      <div>useeffect</div>
      <button onClick={()=>setNumber(number+1)}>{number}</button>
      <button onClick={()=>setAnumber(aNumber+1)}>{aNumber}</button>
    </div>
  )
}

