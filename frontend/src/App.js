import React from 'react';
import Dashboard from './components/Dashboard';
import SimulateConditions from './components/SimulateConditions';
import Navbar from './components/Navbar';

const App = () => {
  return (
    <div>
      <Navbar />
      <h1>VAWT Dashboard</h1>
      <Dashboard />
      <SimulateConditions />
    </div>
  );
};

export default App;
