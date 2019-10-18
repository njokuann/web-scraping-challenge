from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of flask
app = Flask(__name__)

#Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route
@app.route("/")
def home():

    # Find one record of data
    mars_data = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", mars_data=mars_data)


#routes for scrape functions
@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars_data
    mars_data = scrape_mars_scrape

    #update mongo database
    mongo.db.collection.update({}, mars_data, upsert=True)

    # redirect to home
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

