from flask import Flask, render_template, redirect, url_for,request
from hotels import Hotel
from restaurant import Restaurant
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

def load_restaurants():
    tree = ET.parse('data/food.xml')
    root = tree.getroot()
    restaurants = []
    for food_elem in root.findall('restaurant'):
        restaurant = Restaurant(
            name=food_elem.find('name').text,
            type=food_elem.find('type').text,
            location=food_elem.find('location').text,
            pricerange=food_elem.find('pricerange').text,
            image=food_elem.find('image').text
        )
        restaurants.append(restaurant)
    return restaurants

@app.route("/")
def base():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/hotels")
def hebergement():
    hotels = load_hotels()
    return render_template("hebergements.html", hotels=hotels)

@app.route("/food")
def food():
    restaurants=load_restaurants()
    return render_template("food.html",restaurants=restaurants)