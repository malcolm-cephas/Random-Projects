import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './BmiForm.css';

const initialValues = {
  weight: '',
  height: '',
  date: ''
};

const BmiForm = ({ change }) => {
  const [state, setState] = useState(initialValues);

  const handleChange = (e) => {
    let { value, name } = e.target;
    
    // Parse value to ensure correct number checks, limit at 999
    if (value !== '') {
      const numVal = parseFloat(value);
      if (numVal > 999) {
        value = '999';
      }
    }

    const date = new Date().toLocaleString().split(',')[0];
    setState((prevState) => ({
      ...prevState,
      [name]: value,
      date
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (state.weight === '' || state.height === '') return;
    change(state);
    setState(initialValues);
  };

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      <div className="row">
        <div className="col m6 s12 input-group">
          <label htmlFor="weight">Weight</label>
          <div className="input-field-wrapper">
            <input
              id="weight"
              name="weight"
              type="number"
              min="1"
              max="999"
              placeholder="e.g. 70"
              value={state.weight}
              onChange={handleChange}
              required
            />
            <span className="unit-badge">kg</span>
          </div>
        </div>

        <div className="col m6 s12 input-group">
          <label htmlFor="height">Height</label>
          <div className="input-field-wrapper">
            <input
              id="height"
              name="height"
              type="number"
              min="1"
              max="999"
              placeholder="e.g. 175"
              value={state.height}
              onChange={handleChange}
              required
            />
            <span className="unit-badge">cm</span>
          </div>
        </div>
      </div>
      
      <div className="center">
        <button
          id="bmi-btn"
          className="calculate-btn"
          type="submit"
          disabled={state.weight === '' || state.height === ''}
        >
          Calculate BMI
        </button>
      </div>
    </form>
  );
};

BmiForm.propTypes = {
  change: PropTypes.func.isRequired
};

export default BmiForm;
