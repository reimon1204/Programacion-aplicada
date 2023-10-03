###Dict Comprehensions
#Digamos que tenemos dos listas que queremos combinar en una
#diccionario, como una lista de estudiantes y una lista de sus alturas,
#en pulgadas:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#Python te permite crear un diccionario usando
# un dictado de comprensión, con esta sintaxis:

zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)

students = {key:value for key, value in zip(names, heights)}
#students es ahora {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)

# #zip() combina dos listas en un iterador de tuplas con los elementos de la lista emparejados. Este dictado de comprensión:

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
#Ejemplo 2
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)