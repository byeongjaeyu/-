import React from 'react'

const usePreventLeave = (onLeaving) => {
  const listener = (event) => {
    event.preventDefault();
    event.returnValue = "";
  }
  const enablePrevent = () => window.addEventListener("beforeunload",listener);
  const disablePrevent = () => window.removeEventListener("beforeunload",listener);
  return {enablePrevent,disablePrevent}
}

export default function UseprevnetLeave() {
  const {enablePrevent,disablePrevent} = usePreventLeave();
  return (
    <div>
      <div>UseprevnetLeave</div>
      <button onClick={enablePrevent}>Protect</button>
      <button onClick={disablePrevent}>Unprotect</button>
    </div>
  )
}
