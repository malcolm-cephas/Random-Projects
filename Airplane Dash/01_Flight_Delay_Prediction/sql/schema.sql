-- 01_Flight_Delay_Prediction/sql/schema.sql
-- Senior Airline Analytics Portfolio
-- Project 1: Flight Delay Prediction

-- Create the flights table with optimized data types
CREATE TABLE IF NOT EXISTS flights (
    flight_id SERIAL PRIMARY KEY,
    flight_date DATE NOT NULL,
    carrier VARCHAR(10) NOT NULL, -- e.g., 'AA', 'DL', 'UA'
    tail_number VARCHAR(20),
    flight_number INT,
    origin_airport CHAR(3) NOT NULL, -- IATA Code e.g., 'JFK'
    dest_airport CHAR(3) NOT NULL,
    scheduled_departure_time TIME NOT NULL,
    actual_departure_time TIME,
    departure_delay INT DEFAULT 0, -- Minutes
    taxi_out_time INT, -- Minutes from gate to takeoff
    scheduled_arrival_time TIME NOT NULL,
    actual_arrival_time TIME,
    arrival_delay INT DEFAULT 0, -- Minutes
    cancelled BOOLEAN DEFAULT FALSE,
    cancellation_code CHAR(1), -- A: Carrier, B: Weather, C: NAS, D: Security
    diverted BOOLEAN DEFAULT FALSE,
    distance INT, -- Miles
    carrier_delay INT DEFAULT 0,
    weather_delay INT DEFAULT 0,
    nas_delay INT DEFAULT 0,
    security_delay INT DEFAULT 0,
    late_aircraft_delay INT DEFAULT 0
);

-- Performance Optimization: Indexes for common reporting queries
CREATE INDEX IF NOT EXISTS idx_flights_date ON flights(flight_date);
CREATE INDEX IF NOT EXISTS idx_flights_carrier ON flights(carrier);
CREATE INDEX IF NOT EXISTS idx_flights_origin_dest ON flights(origin_airport, dest_airport);

-- View for OTP (On-Time Performance) KPI
CREATE OR REPLACE VIEW view_otp_summary AS
SELECT 
    carrier,
    COUNT(*) as total_flights,
    SUM(CASE WHEN arrival_delay <= 15 AND cancelled = FALSE THEN 1 ELSE 0 END) as on_time_flights,
    ROUND(CAST(SUM(CASE WHEN arrival_delay <= 15 AND cancelled = FALSE THEN 1 ELSE 0 END) AS NUMERIC) / COUNT(*) * 100, 2) as otp_percentage
FROM flights
GROUP BY carrier;
