import React, { useRef, useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import PropTypes from 'prop-types';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';

// Register Chart.js components (required for Chart.js v4)
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

const Bar = ({ labelData = [], bmiData = [] }) => {
  const chartRef = useRef(null);
  const [chartData, setChartData] = useState({
    labels: [],
    datasets: []
  });

  useEffect(() => {
    const chart = chartRef.current;
    if (!chart) return;

    const ctx = chart.ctx;
    // Create a beautiful linear gradient for the fill
    const gradientFill = ctx.createLinearGradient(0, 0, 0, 300);
    gradientFill.addColorStop(0, 'rgba(99, 102, 241, 0.45)');
    gradientFill.addColorStop(1, 'rgba(99, 102, 241, 0.00)');

    setChartData({
      labels: labelData,
      datasets: [
        {
          label: 'BMI Trend',
          data: bmiData,
          fill: true,
          backgroundColor: gradientFill,
          borderColor: '#6366f1',
          borderWidth: 3,
          pointBackgroundColor: '#818cf8',
          pointBorderColor: '#fff',
          pointBorderWidth: 2,
          pointRadius: 5,
          pointHoverRadius: 7,
          pointHoverBackgroundColor: '#4f46e5',
          pointHoverBorderColor: '#fff',
          pointHoverBorderWidth: 3,
          tension: 0.35 // Curved line for a premium modern look
        }
      ]
    });
  }, [labelData, bmiData]);

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(15, 23, 42, 0.9)',
        titleColor: '#fff',
        bodyColor: '#e2e8f0',
        borderColor: 'rgba(255, 255, 255, 0.1)',
        borderWidth: 1,
        padding: 12,
        boxPadding: 4,
        usePointStyle: true,
        titleFont: {
          family: "'Outfit', sans-serif",
          size: 13,
          weight: '600'
        },
        bodyFont: {
          family: "'Inter', sans-serif",
          size: 13
        }
      }
    },
    scales: {
      x: {
        grid: {
          display: false
        },
        title: {
          display: true,
          text: 'Date',
          color: '#94a3b8',
          font: {
            family: "'Outfit', sans-serif",
            size: 12,
            weight: '600'
          }
        },
        ticks: {
          color: '#64748b',
          font: {
            family: "'Inter', sans-serif",
            size: 11
          }
        }
      },
      y: {
        beginAtZero: true,
        grid: {
          color: 'rgba(255, 255, 255, 0.04)',
          drawBorder: false
        },
        title: {
          display: true,
          text: 'BMI Value',
          color: '#94a3b8',
          font: {
            family: "'Outfit', sans-serif",
            size: 12,
            weight: '600'
          }
        },
        ticks: {
          color: '#64748b',
          font: {
            family: "'Inter', sans-serif",
            size: 11
          }
        }
      }
    }
  };

  return (
    <div className="chart-container" style={{ position: 'relative', height: '300px', width: '100%', margin: '1.5rem 0' }}>
      <Line ref={chartRef} data={chartData} options={options} />
    </div>
  );
};

Bar.propTypes = {
  labelData: PropTypes.arrayOf(PropTypes.string),
  bmiData: PropTypes.arrayOf(PropTypes.string)
};

export default Bar;
