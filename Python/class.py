class Dog(object):
    """docstring for Dog."""

    #Class Attribute
    species = "mammal"

    #Initializer / Instance Attributes
    def __init__(self, name, age):
        super(Dog, self).__init__()
        self.name = name
        self.age = age

    #Instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    #Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

#Child class (inherits from Dog class)
class RusselTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child classes inherit Attributes and behaviors from the parent classes
jim = Bulldog("Jim", 12)
print(jim.description())

#Child classes have specific Attributes and behaviors as well
print(jim.run("slowly"))

#Is jim an instance of Dog()
print(isinstance(jim, Dog))

#Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

#Is johny walker an instance of Bulldog()?
johnywalker = RusselTerrier("Johny Walker", 4)
print(isinstance(johnywalker, Bulldog))


#Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 7)
peter = Dog("Peter", 32)

def get_biggest_number(*args):
    return max(args)

#Access the instance Attributes
print("{0} is {1} and {2} is {3}.". format(philo.name, philo.age, mikey.name, mikey.age))

#Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))


print("The oldest dog is {} years old.".format(get_biggest_number(philo.age, mikey.age, peter.age)))

#Call our instance methods
print(mikey.description())
print(peter.speak("HI"))
