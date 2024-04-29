import Image from "next/image";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

// src/App.js
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div className="App">
      {data ? <p>{data.Hello}</p> : <p>Loading...</p>}
    </div>
  );
}

export default App;
  