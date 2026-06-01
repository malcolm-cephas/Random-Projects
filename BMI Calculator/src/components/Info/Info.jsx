import React from 'react';
import PropTypes from 'prop-types';
import './Info.css';

const getBmiCategory = (bmiVal) => {
  const val = parseFloat(bmiVal);
  if (isNaN(val)) {
    return { label: 'Unknown', color: 'var(--text-muted)' };
  }
  if (val < 18.5) {
    return { label: 'Underweight', color: 'var(--bmi-underweight)' };
  }
  if (val < 25) {
    return { label: 'Normal', color: 'var(--bmi-normal)' };
  }
  if (val < 30) {
    return { label: 'Overweight', color: 'var(--bmi-overweight)' };
  }
  return { label: 'Obese', color: 'var(--bmi-obese)' };
};

const Info = ({ weight, height, id, date, bmi, deleteCard }) => {
  const category = getBmiCategory(bmi);

  const handleDelete = () => {
    deleteCard(id);
  };

  return (
    <div className="col m6 s12 card-wrapper">
      <div 
        className="bmi-card" 
        style={{ '--card-accent-color': category.color }}
      >
        <div className="card-header">
          <div className="bmi-display">
            <span className="bmi-val" data-test="bmi">
              {bmi}
            </span>
            <span className="bmi-badge">
              {category.label}
            </span>
          </div>
          
          <button 
            className="delete-card-btn" 
            onClick={handleDelete}
            aria-label="Delete log entry"
          >
            ✕
          </button>
        </div>

        <div className="card-data-grid">
          <div className="data-item">
            <span className="data-label">Weight</span>
            <span className="data-value" data-test="weight">
              {weight} kg
            </span>
          </div>
          
          <div className="data-item">
            <span className="data-label">Height</span>
            <span className="data-value" data-test="height">
              {height} cm
            </span>
          </div>
          
          <div className="data-item">
            <span className="data-label">Date</span>
            <span className="data-value" data-test="date">
              {date}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

Info.propTypes = {
  weight: PropTypes.string.isRequired,
  height: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired,
  date: PropTypes.string.isRequired,
  bmi: PropTypes.string.isRequired,
  deleteCard: PropTypes.func.isRequired
};

export default Info;
