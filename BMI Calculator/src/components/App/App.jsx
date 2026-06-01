import React, { useState, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';
import './App.css';
import BmiForm from '../BmiForm/BmiForm';
import Info from '../Info/Info';
import Bar from '../Bar/Bar';
import { getData, storeData } from '../../helpers/localStorage';

const App = () => {
  const [state, setState] = useState(() => getData('data') || []);
  const [chartData, setChartData] = useState({ date: [], bmi: [] });
  const [hasUndo, setHasUndo] = useState(() => getData('lastState') !== null);

  useEffect(() => {
    storeData('data', state);
    const date = state.map((obj) => obj.date);
    const bmi = state.map((obj) => obj.bmi);
    setChartData({ date, bmi });
  }, [state]);

  const handleChange = (val) => {
    const heightInM = parseFloat(val.height) / 100;
    const weightVal = parseFloat(val.weight);
    val.bmi = (weightVal / (heightInM * heightInM)).toFixed(2);
    val.id = uuidv4();
    
    let newVal = [...state, val];
    const len = newVal.length;
    if (len > 7) {
      newVal = newVal.slice(1, len);
    }
    setState(newVal);
  };

  const handleDelete = (id) => {
    storeData('lastState', state);
    setHasUndo(true);
    const newState = state.filter((item) => item.id !== id);
    setState(newState);
  };

  const handleUndo = () => {
    const lastState = getData('lastState');
    if (lastState) {
      setState(lastState);
      // Remove undo state once used
      localStorage.removeItem('lastState');
      setHasUndo(false);
    }
  };

  return (
    <div className="container animate-fade-in">
      <div className="app-wrapper">
        <header className="center">
          <h1 className="dashboard-title">BMI Tracker</h1>
        </header>

        <main className="row">
          <div className="col m12 s12">
            <BmiForm change={handleChange} />
            
            {state.length > 0 && (
              <>
                <h2 className="section-title">BMI Trend</h2>
                <Bar labelData={chartData.date} bmiData={chartData.bmi} />
              </>
            )}

            <h2 className="section-title">7 Day History</h2>
            
            <div className="data-logs-container">
              <div className="row">
                {state.length > 0 ? (
                  state.map((info) => (
                    <Info
                      key={info.id}
                      id={info.id}
                      weight={info.weight}
                      height={info.height}
                      date={info.date}
                      bmi={info.bmi}
                      deleteCard={handleDelete}
                    />
                  ))
                ) : (
                  <div className="col s12 empty-state">
                    <span className="empty-state-icon">📊</span>
                    <p>No health logs recorded yet. Calculate above to get started!</p>
                  </div>
                )}
              </div>
            </div>

            {hasUndo && (
              <div className="undo-container">
                <button className="undo-btn" onClick={handleUndo}>
                  <span className="undo-btn-icon">↺</span> Undo Last Deletion
                </button>
              </div>
            )}
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;
