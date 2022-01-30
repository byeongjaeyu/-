import React from 'react'
import {useEffect, useState} from 'react'

export default function UseTitle() {

  // 1. 키는순간 componentunmount로 useEffect의 updateTitle RUN
  // 2. settimeout으로 componentwillupdate로 useEffect의 updateTitle RUN
  const useTitle = initialTitle => {
    const [title,setTitle] = useState(initialTitle);
    const updateTitle = () => {
      const htmlTitle = document.querySelector("title")
      htmlTitle.innerText = title
    };
    useEffect(()=>{
      updateTitle()
      console.log('useeffect run!')
    }, [title]);
    return setTitle;
  }

  const titleUpdater = useTitle("Loading...")
  setTimeout(()=> titleUpdater("Home"),3000)
  return (
    <div>
      <div>usetitle</div>

    </div>
  )
}
