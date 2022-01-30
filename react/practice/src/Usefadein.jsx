import React,{useState,useEffect,useRef} from 'react'

const useFadeIn = (duration = 1,delay = 0) => {
  const element = useRef();
  useEffect(() => {
    if(element.current){
      const { current } = element;
      current.style.transition = `opacity ${duration}s ease-in-out ${delay}s`
      current.style.opacity=1;
    }
  },[])
  return {ref:element,style:{opacity:0}};
}

export default function Usefadein() {
  const fadeInH1 = useFadeIn(1,3);
  return (
    <div>
      <div>Usefadein</div>
      <h1 {...fadeInH1}>Hello</h1>
    </div>
  )
}
