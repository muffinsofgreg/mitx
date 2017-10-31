import datetime


class Person(object):

    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthday(self, month, day, year):
        """set's self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """return self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def __lt__(self, other):
        """returns True is self's name is lexicographically less than
        the other's name, and False otherwise"""
        if self.lastName == other.lastName:
                return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name


class MITPerson(Person):

    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + ' says: ' + utterance)


class UG(MITPerson):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, ' Dude, ' + utterance)


class Grad(MITPerson):
    pass
