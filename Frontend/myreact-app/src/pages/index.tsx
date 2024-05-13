import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:8000');
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const createUser = async () => {
    try {
      const response = await fetch(`http://localhost:8000/user?name=${name}&email=${email}`, {
        method: 'POST',
      });
      if (!response.ok) {
        throw new Error('Failed to create user');
      }
      alert('User created successfully');
    } catch (error) {
      console.error('Error creating user:', error);
      alert('Failed to create user');
    }
  };

  return (
    <div className="App" id="Appfunc">
      {data ? <p>{data.Hello}</p> : <p>Loading...</p>}
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button onClick={createUser}>Create User</button>
    </div>
  );
}

export default App;
