from flask import Flask, render_template, redirect, url_for,request
from hotels import Hotel
import xml.etree.ElementTree as ET

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

def load_hotels():
    tree = ET.parse('data/hotels.xml')
    root = tree.getroot()
    hotels = []
    for hotel_elem in root.findall('hotel'):
        hotel = Hotel(
            name=hotel_elem.find('nom').text,
            rating=int(hotel_elem.find('etoiles').text),
            description=hotel_elem.find('description').text,
            location=hotel_elem.find('localisation').text,
            image=hotel_elem.find('image_url').text
        )
        hotels.append(hotel)
    return hotels

@app.route("/")
def base():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/hebergement")
def hebergement():
    hotels = load_hotels()
    return render_template("hebergements.html", hotels=hotels)

