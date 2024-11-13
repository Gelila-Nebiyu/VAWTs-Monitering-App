import React, { useState } from 'react';

const SimulateConditions = () => {
  const [windSpeed, setWindSpeed] = useState(0);
  const [energyOutput, setEnergyOutput] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('/api/simulate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ wind_speed: windSpeed }),
    });
    const result = await response.json();
    setEnergyOutput(result.energy_output);
  };

  return (
    <div>
      <h2>Simulate Conditions</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Wind Speed (m/s):
          <input type="number" value={windSpeed} onChange={(e) => setWindSpeed(e.target.value)} />
        </label>
        <button type="submit">Simulate</button>
      </form>
      {energyOutput && <p>Simulated Energy Output: {energyOutput} kWh</p>}
    </div>
  );
};

export default SimulateConditions;
