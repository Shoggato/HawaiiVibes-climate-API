# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# set new engine to sqlite file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurements = Base.classes.measurement

station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f'<br>'
        f'Insert a starting date ex) 2012-04-15<br>'
        f'If you want to search between two dates then Insert a start date followed by a / and the end date<br>'
        f'<br>'
        f"/api/v1.0/<br/>"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    precipitation_data = session.query(measurements.date, measurements.prcp)\
                                .filter(measurements.date >= '2016-08-23')\
                                .filter(measurements.date <= '2017-08-23').all()

    session.close()

    precipitation = []
    for date, prcp in precipitation_data:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

    active_stations = session.query(station.station,
                                    station.name,
                                    station.latitude,
                                    station.longitude,
                                    station.elevation).group_by(station.station).all()

    session.close()

    # my attempt at list comprehesion for a dictionary :3
    stations_list = [{'Station': row[0],
                 'Name': row[1],
                 'Latitude': row[2],
                 'longitude':row[3],
                 'elevation':row[4]} for row in active_stations]

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():

    temperature_data = session.query(measurements.station, measurements.tobs, measurements.date)\
                                    .filter(measurements.date >= '2016-08-23')\
                                    .filter(measurements.date <= '2017-08-23')\
                                    .filter(measurements.station == 'USC00519523').all()

    session.close()

    temperature = [{'Date': row.date,
                    'Station': row.station,
                    'Temperature':row.tobs} for row in temperature_data]

    return jsonify(temperature)

@app.route("/api/v1.0/<start_value>")
@app.route("/api/v1.0/<start_value>/<end_value>")
def started(start_value, end_value = None):

    start_date = start_value
    end_date = end_value
    if end_date:
        temps = session.query(func.min(measurements.tobs),
                                         func.avg(measurements.tobs), 
                                         func.max(measurements.tobs))\
                                        .filter(measurements.date >= start_date)\
                                        .filter(measurements.date <= end_date).all()

    elif start_date:
        temps = session.query(func.min(measurements.tobs),
                                         func.avg(measurements.tobs), 
                                         func.max(measurements.tobs))\
                                        .filter(measurements.date >= start_date).all()
    else:
        f"The date doesn't exist in the database."

    session.close()

    # Another attempt at List comprehension, trying to get better at this
    temperature = [{'Minimum Temperature': row[0],
                    'Average Temperature': row[1],
                    'Maximum Temperature': row[2]} for row in temps]

    return jsonify(temperature)
    

if __name__ == '__main__':
    app.run(debug=True)