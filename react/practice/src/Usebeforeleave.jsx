import React,{useState, useEffect} from 'react'

const useBeforeLeave = (onBefore) => {
  useEffect(() => {
    document.addEventListener("mouseleave",handle)
    return () => {
      document.removeEventListener("mouseleave",handle)
    }
  },[]);

  if(typeof onBefore !== "function"){
    return;
  }
  const handle = (event) => {
    const {clientY} = event;
    if (clientY<=0){onBefore();}
  }
}

export default function Usebeforeleave() {
  const begForLife = () => console.log("plz dont leave");
  useBeforeLeave(begForLife);
  return (
    <div>
      <div>usebeforeleave</div>
      <h1>Hello</h1>
    </div>
  )
}
