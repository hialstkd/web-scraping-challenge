# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)


# Use flask_pymongo to set up mongo connection locally 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
@app.route("/")
def index(): 

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_news = scrape_mars.scrape_mars_news()
    mars_image = scrape_mars.scrape_mars_image()
    mars_facts = scrape_mars.scrape_mars_facts()
    mars_hemi = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
