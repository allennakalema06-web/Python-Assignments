#assignment
# using dynamic classes identify atleast 7 classes with atleast 7 properties and create atleast 4 objects for each class 
class Book():
    def __init__(self, title, author, pages, genre, price, publisher, year):
        # Assigning book properties
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.price = price
        self.publisher = publisher
        self.year = year
# Creating Book objects
book1 = Book("Think and grow rich", "Napoleon Hill", 238, "personal success", 25000, "The Raltson Society", 1937)
book2 = Book("Python Basics", "Jane Smith", 250, "Education", 18000, "Cod,ePub", 2021)
book3 = Book("Life Hacks", "Mark Lee", 180, "Lifestyle", 12000, "LifePub", 2018)
book4 = Book("The hidden codex of reality", "Taren Veyra", 208, "Metaphysical",  32000, "Amazon", 2025)      


class Movie:
    def __init__(self, title, director, duration, genre, rating, year, language):
        # assigning movie attributes
        self.title = title
        self.director = director
        self.genre = genre
        self.rating = rating
        self.year = year
        self.language = language
# Creating the movie objects
movie1 = Movie("Inception", "Nolan", "Sci-Fi", 8.8, 2010, "English")
movie2 = Movie("The Avatar", "Cameron", "Fantasy", 7.9, 2009, "English")
movie3 = Movie("Parasite", "Bong", "Drama", 8.6, 2019, "Korean")
movie4 = Movie("Titanic", "Cameron", "Romance", 7.8, 1997, "English")
movie5 = Movie("The 3 Body problem", "David Benioff", 7.5, 2024, "English and Mandarin")

class Employee:
    def __init__(self, name, position, salary, department, age, email, id_no):
        # Assigning employee attributes
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department
        self.age = age
        self.email = email
        self.id_no = id_no
# Creating the employee objects
employee1 = Employee("Alice Acen", "Manager", 5000000, "HR", 30, "alice@gmail.com", "E01")
employee2 = Employee("Kasolo Bob", "Developer", 4000000, "IT", 28, "bob@gmail.com", "E02")
employee3 = Employee("Chris Matovu", "Analyst", 3500000, "Finance", 27, "chris@gmail.com", "E03")
employee4 = Employee("Diana Nassazi", "Designer", 3000000, "Creative", 25, "diana@gmail.com", "E04")


class House:
    def __init__(self, location, price, rooms, size, owner, color, type):
        # Assigning values to the object's attributes
        self.location = location
        self.price = price
        self.rooms = rooms
        self.size = size
        self.owner = owner
        self.color = color
        self.type = type
# Creating the House objects using the House class 
house1 = House("Kampala", 50000, 3, "120sqm", "John Kasule", "White", "Bungalow")
house2 = House("Entebbe", 80000, 4, "200sqm", "Mary Nanozi", "Blue", "Villa")
house3 = House("Jinja", 40000, 2, "100sqm", "Paul Ssevume", "Green", "Apartment")
house4 = House("Gulu", 30000, 3, "110sqm", "Sarah Ndubandule", "Yellow", "Bungalow")

class Hospital:
    def __init__(self, name, location, beds, doctors, nurses, departments, rating):
        #Assigning hospital attributes
        self.name = name
        self.location = location
        self.beds = beds
        self.doctors = doctors
        self.nurses = nurses
        self.departments = departments
        self.rating = rating
# Creating hospital objects
hospital1 = Hospital("CityCare", "Kampala", 100, 20, 40, "General", 4.5)
hospital2 = Hospital("LifePlus", "Entebbe", 80, 15, 30, "Surgery", 4.2)
hospital3 = Hospital("HopeMed", "Jinja", 60, 10, 25, "Pediatrics", 4.0)
hospital4 = Hospital("Wellness", "Gulu", 70, 12, 28, "Maternity", 4.3)

class Gym:
    def __init__(self, name, location, trainers, equipment, members, fees, open_hours):
        # Assigning gym attributes
        self.name = name
        self.location = location
        self.trainers = trainers
        self.equipment = equipment
        self.members = members
        self.fees = fees
        self.open_hours = open_hours
# Creating the gym objects
gym1 = Gym("FitZone", "Kampala", 5, "Modern", 100, 50, "6am-10pm")
gym2 = Gym("PowerHouse", "Entebbe", 4, "Advanced", 80, 40, "5am-9pm")
gym3 = Gym("IronClub", "Jinja", 3, "Basic", 60, 30, "6am-8pm")
gym4 = Gym("FlexGym", "Gulu", 6, "Premium", 120, 60, "5am-11pm")


class FashionItem:
    def __init__(self, name, brand, size, color, price, material, category):
        # Assigning FashionItem attributes
        self.name = name
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.material = material
        self.category = category
# Creating fashion item objects
item1 = FashionItem("Sneakers", "Nike", 42, "White", 120, "Leather", "Footwear")
item2 = FashionItem("Jacket", "Adidas", "L", "Black", 80, "Cotton", "Clothing")
item3 = FashionItem("Watch", "Rolex", "M", "Gold", 500, "Metal", "Accessory")
item4 = FashionItem("Bag", "Gucci", "Medium", "Brown", 300, "Leather", "Accessory")