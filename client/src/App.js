import React, {useState, useEffect} from "react" 
function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch(`/report/${51002}`).then(
      res => res.json()
    ).then (
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return(
    <div>
    <p>
    </p>
    </div>
  )
}
export default App
    /*
    <div>

      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ): (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}

    </div>
    */