# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def __str__(self):
        return f"Filmo pavadinimas - {self.title}, Prodiuseris - {self.director}, Biudžetas - {self.budget} USD."

    def wasExpensive(self):
        return self.budget > 100000000    

Movie1 = Movie("Interstellar", "Christopher Nolan", 165000000)
Movie2 = Movie("Arrival", "Denis Villeneuve", 47000000)
Movie3 = Movie("Contact", "Robert Zemeckis", 90000000)


print(Movie1)
print(Movie1.wasExpensive())

print(Movie2)
print(Movie2.wasExpensive())

print(Movie3)
print(Movie2.wasExpensive())


