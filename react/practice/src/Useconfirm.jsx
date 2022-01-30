import React from 'react'


const useConfirm = (message="",callback,rejection) => {
  if (callback && typeof callback !== "function") {
    return;
  }
  if (rejection && typeof callback !== "function") {
    return;
  }
  const confirmAction = () => {
    if(window.confirm(message)){
      callback();
    } else {
      rejection();
    }
  }
  return confirmAction;
}
export default function Useconfirm() {
  const deleteWorld = () => console.log("Deleting the world...");
  const abort = () => console.log("Aborted")
  const confirmDelete = useConfirm("Are you sure", deleteWorld,abort)
  return (
    <div>
      <div>Useconfirm</div>
      <button onClick={confirmDelete}>Delete the world</button>
    </div>
  )
}
