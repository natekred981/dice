// frontend/src/App.js

import React, { useState, useEffect } from "react";

function App() {
  const [result, setResult] = useState(null);
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/");
      const data = await response.json();
      console.log(data);
      setResult(data.result);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Backend JSON Response:</h1>
        {result !== null ? <p>{JSON.stringify(result)}</p> : <p>Loading...</p>}
      </header>
    </div>
  );
}

export default App;
