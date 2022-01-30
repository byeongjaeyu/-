import React from 'react'
import {useEffect, useState, useRef} from 'react'


const useClick = (onClick) => {
  // console.log('2')
  //3. element 선언.(useRef)
  const element = useRef();

  // console.log('3')
  //4. componentdidmount성격으로 useEffect 실행.
  useEffect(()=>{
    // console.log('5')
    //15~17 componentdidmount,componentdidupdate때 호출
    if(element.current){
      element.current.addEventListener("click",onClick);
    }
    // componentwillunmount일때 리턴 
    // 아래와 같은 코드를 추가하는 이유는 component가 mount되지 않았을때,
    // eventListner가 배치되게 하고 싶지 않기 위해..
    return ()=>{
      // console.log('????????????')
      if (element.current){
      element.current.removeEventListener("click",onClick);
      }
    }
  },[])
  // console.log('4')
  return element;
}


export default function UseClick() {
  
  // console.log('여기는?')
  // 2. useClick(sayHello)함수 실행
  const sayHello = () => console.log("sayHello")
  const title = useClick(sayHello);
  // console.log('title밑은?')
  const potato = useRef();
  setTimeout(()=> potato.current.focus(),3000)
  return (
    <div>
      <div>useClick</div>
      {/* 1. ref 선언 -> title함수 실행 */}
      <h1 ref = {title}>Hi</h1>
      <input placeholder='la' ref={potato}/>
    </div>
  )
}