# HawaiiVibes Climate Explorer API

## Overview
This project establishes a Flask API to offer climate-related data for Hawaii through a SQLite database. The API comprises various routes that provide information about precipitation, weather stations, temperature observations, and temperature statistics within specified date ranges. Additionally, exploratory data analysis is performed, including precipitation trends and station statistics.

## Setup
- **Tools Used:** Flask, SQLAlchemy, SQLite, matplotlib, pandas, datetime
- **Database:** [hawaii.sqlite](Resources/hawaii.sqlite)

## Flask API
### 1. Routes

- **`/` - Home Route**
  - Displays all available API routes with usage instructions.
  - Example: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

- **`/api/v1.0/precipitation`**
  - Returns precipitation data for the last 12 months.
  - Example: [http://127.0.0.1:5000/api/v1.0/precipitation](http://127.0.0.1:5000/api/v1.0/precipitation)

- **`/api/v1.0/stations`**
  - Provides information about weather stations in Hawaii.
  - Example: [http://127.0.0.1:5000/api/v1.0/stations](http://127.0.0.1:5000/api/v1.0/stations)

- **`/api/v1.0/tobs`**
  - Returns temperature observations for the last 12 months from the most active station.
  - Example: [http://127.0.0.1:5000/api/v1.0/tobs](http://127.0.0.1:5000/api/v1.0/tobs)

- **`/api/v1.0/<start_value>`**
  - Returns minimum, average, and maximum temperatures from a specified start date.
  - Example: [http://127.0.0.1:5000/api/v1.0/2017-01-01](http://127.0.0.1:5000/api/v1.0/2017-01-01)

- **`/api/v1.0/<start_value>/<end_value>`**
  - Returns temperature statistics for a specified date range.
  - Example: [http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31](http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31)

### 2. How to Use
1. Run the provided Python script to start the Flask server.
2. Access the desired API routes using a web browser or API testing tool.

### 3. API Responses
- Precipitation, Stations, and Temperature Observations return JSON-formatted data.
- Temperature Statistics return a JSON object with minimum, average, and maximum temperatures.

### 4. Exploratory Data Analysis
- The code includes exploratory data analysis, such as querying and plotting precipitation trends, calculating station statistics, and visualizing temperature histograms.

## Usage Examples
1. **Precipitation Data:**
   - [/api/v1.0/precipitation](http://127.0.0.1:5000/api/v1.0/precipitation)

2. **Stations Information:**
   - [/api/v1.0/stations](http://127.0.0.1:5000/api/v1.0/stations)

3. **Temperature Observations:**
   - [/api/v1.0/tobs](http://127.0.0.1:5000/api/v1.0/tobs)

4. **Temperature Statistics (From a Start Date):**
   - [/api/v1.0/2017-01-01](http://127.0.0.1:5000/api/v1.0/2017-01-01)

5. **Temperature Statistics (Date Range):**
   - [/api/v1.0/2017-01-01/2017-12-31](http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31)
