import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'

response = urllib.request.urlopen(url)

text = response.read()

print(text)

result = json.loads(text)


print(result)


screen = turtle.Screen()
screen.setup(1280,640)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.gif")

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(10.0, 60.0)
location.dot(5)
location.hideturtle()
