import React,{useState,useEffect,useRef} from 'react'

const useNotification = (title, options) => {
  if(!("Notification" in window)) {
    return;
  }

  const fireNotif = () => {
    if(Notification.permission !== "granted"){
      Notification.requestPermission().then(permission => {
        if(permission==="granted"){
          new Notification(title,options)
        } else{
          return;
        }
      })
    } else {
      new Notification(title,options)
    }
  };
  return fireNotif;
}

export default function Usenotification() {
  const triggerNotif = useNotification("알림이다.",{body:"알림 처음보냐"});
  return (
    <div>
      <div>usenotification</div>
      <button onClick={triggerNotif}>hello</button>
    </div>
  )
}
