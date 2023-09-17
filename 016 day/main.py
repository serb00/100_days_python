# from turtle import Screen, Turtle
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('DarkSeaGreen')
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Mi", "Unknown"])
table.align = 'l'

print(table)