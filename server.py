from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def title_card():
    return ('<h1 style = "text-align : center" =>WELCOME</h1>'
            "<h2>guess a number between 0 to 9 </h2> "
            "<img src ='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTZ3MndiZnM4Y3BtdDVzZ2QxbWY2emhsZ3c5OTFkdXRkdWhvbzNnOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LfbDxyQIWtzLTtMnc0/giphy.webp' width = 200>")

integer = random.randint(0 ,9)
print(integer)

@app.route("/<num>")
def random_num(num):
    if int(num) > integer:
        return ('<h3 style="color: blue;" > the number you entered is too high </h3>'
                '<img src ="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm1uczJhZ3lnNDFtcWpueXVjNGhoNTB0YWtoemlhMnI1ZmV2a3I3diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2cei8MJiL2OWga5XoC/200.webp" width =200>')
    if int(num) < integer:
        return ('<h3 style="color: red;"> the number you entered is too low  </h3>'
                '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmY2M3N5bGg5Y3J2OGl1aGQ0ejJjaTh2em9kaWgwZHR3dDU3OXcwZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/6SxOvHZbP7eqaUtTy2/200.webp" width = 200 >')
    if int(num) == integer:
        return ('<h3 style="color: green;">  yes you got it </h3>'
                '<img src = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHV1eW1vMjB4ZGk5emo5cGZwdGZzYnV3YWY0c25maWo0NHBrZGNkeCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ohzdIuqJoo8QdKlnW/100.webp" width=200>')

if __name__ == "__main__":
    app.run(debug =True)

