import React,{useState,useEffect,useRef} from 'react'

const useScroll = () => {
  const [state,setState] = useState({
    x:0,
    y:0
  });
  const onScroll = () => {
    setState({y:window.scrollY,x:window.scrollX});
  }
  useEffect(()=>{
    window.addEventListener("scroll",onScroll)
    return () => window.removeEventListener("scroll",onScroll);
  },[])
  return state;
}

export default function Usescroll() {
  const {y} = useScroll();
  return (
    <div style={{height:"50vh"}}>
      <div> Usescroll</div>
      <h1 style={{color:y>100? "red":"blue"}}>Hi</h1>
    </div>
  )
}
