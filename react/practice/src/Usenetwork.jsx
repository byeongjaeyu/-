import React,{useState,useEffect,useRef} from 'react'

const useNetwork = onChange => {
  const [status,setStatus] = useState(navigator.onLine);
  console.log(status)
  const handleChange = () => {
    setStatus(navigator.onLine);
  }
  useEffect(()=>{
    window.addEventListener("online",handleChange);
    window.addEventListener("offline",handleChange);
    return () => {
      window.removeEventListener("online",handleChange);
      window.removeEventListener("offline",handleChange);
    };
  },[])
  return status;
}

export default function Usenetwork() {
  const onLine = useNetwork();
  return (
    <div>
      <div>usenetwork</div>
      <h1>{onLine? "Online":"Offline"}</h1>
    </div>
  )
}
