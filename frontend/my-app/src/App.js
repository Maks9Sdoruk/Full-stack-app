import React, { useEffect } from 'react';
import './App.css';

function App() {
  // Define the fetchData function
  const fetchData = async () => {
    try {
      // Use the FastAPI service name (backend) and its port inside Docker
      const response = await fetch("http://localhost:8000/");  // Use "http://backend:8000/" inside Docker network
      const data = await response.json();
      console.log(data); // Log the data received from FastAPI
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  // useEffect to call fetchData when the component mounts
  useEffect(() => {
    fetchData();
  }, []); // Empty dependency array ensures this runs only once when the component mounts

  return (
    <div className="App">
    </div>
  );
}

export default App;
