from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo 
import process_mongo_data

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
    RDR6_plot_new = process_mongo_data.process()

if __name__ == "__main__":
    app.run()