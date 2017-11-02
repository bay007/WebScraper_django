from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.


def index(request, name="Galicia"):
    return render(request, "index.html", {"name": name})


def characters(request, page=1):
    starwars_api = "https://swapi.co/api/{people}?page={page}"
    response = requests.get(starwars_api.format(people="people", page=page))
    star_wars_people = response.json()

    nombres_personajes = [nombre_personaje["name"] for nombre_personaje in star_wars_people["results"]]

    url_base = "http://starwars.wikia.com/wiki/{personaje}"
    imagenes_personajes = []
    urls_personajes = [url_base.format(personaje=personaje).replace(
        " ", "_") for personaje in nombres_personajes]

    for url_personaje in urls_personajes:
        r = requests.get(url_personaje)
        soup = BeautifulSoup(r.text, "html.parser")
        imagen_personaje = soup.find("img", class_= "pi-image-thumbnail")
        # imagen_personaje=soup.select('img.pi-image-thumbnail')
        
        if imagen_personaje:
            imagenes_personajes.append(imagen_personaje["src"])
        else:
            imagenes_personajes.append(None)
    
    star_wars_people=tuple(zip(nombres_personajes,imagenes_personajes,urls_personajes))

    return render(request, "character.html", {"characters": star_wars_people})
