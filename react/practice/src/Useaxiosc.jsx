import React from 'react'
import Useaxios from './Useaxios'

export default function Useaxiosc() {
  const { loading,data,error,refetch } = Useaxios({url:"https://yts.mx/api/v2/list_movies.json"})
  console.log(`loading:${loading}\ndata:${data}\nerror:${JSON.stringify(error)}`)
  return (
    <div>
      <div>useaxios-client</div>
      <h1>{data && data.status}</h1>
      <h2>{loading && "loading"}</h2>
      <button onClick={refetch}>Refetch</button>
    </div>
  )
}
