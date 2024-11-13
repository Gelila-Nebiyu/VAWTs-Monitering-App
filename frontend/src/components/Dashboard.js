import React, { useState, useEffect } from 'react';

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/api/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div>
      <h2>Wind Turbine Statistics</h2>
      <ul>
        {data.map(item => (
          <li key={item.id}>
            Wind Speed: {item.wind_speed} m/s, Energy Output: {item.energy_output} kWh, Efficiency: {item.efficiency}%
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
