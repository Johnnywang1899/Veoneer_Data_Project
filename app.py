from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo 
import sys
import json
import process_mongo_data
import plotly
import plotly.graph_objects as go

# Use Flask to create app
app = Flask(__name__)

# Set mongo connection 
app.config["MONGO_URI"] = "mongodb://localhost:27017/Veoneer_Data_Project"

# Create an instance
mongo = PyMongo(app)

@app.route("/")
def ini():
    RDR6_Txcal_Prod = mongo.db.RDR6_Txcal_Prod.find_one()
    return render_template("Data_Dashboard.html", RDR6_Txcal_Prod = RDR6_Txcal_Prod)

@app.route("/update_RDR6")
def update_RDR6():
    RDR6_plot = mongo.db.RDR6_Txcal_Prod
    Avg_test_time, Pass_rate, Uni_date, Antennal1_tx_power, Antenna2_tx_power = process_mongo_data.process()
    gauge_fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y':[0, 1]},
        value = Avg_test_time,
        mode = "gauge+number",
        title = {'text' : "Average Test Time"},
        gauge = {'axis' : {'range' : [None, 100]},
                'steps' : [
                    {'range' : [0, 25], 'color' : 'lightgray'},
                    {'range' : [25, 40], 'color' : 'gray'}],
                'threshold' : {'line' : {'color' : 'red', 'width' : 4}, 'thickness' : 0.75, 'value': 45}}
                ))
    gaugeJSON = json.dumps(gauge_fig, cls=plotly.utils.PlotlyJSONEncoder)

    return gaugeJSON
                

if __name__ == "__main__":
    app.run()