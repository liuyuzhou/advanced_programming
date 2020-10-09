class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print(f'Setting name to {value}')
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


sub_person = SubPerson('Guido')
print(f'name is: {sub_person.name}')
sub_person.name = 'Bill'
sub_person.name = 30
print('-' * 60)


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


class SubPerson(Person):
    @Person.name.setter
    def name(self, value):
        print(f'Setting name to {value}')
        super(SubPerson, SubPerson).name.__set__(self, value)


class SubPerson(Person):
    @property  # Doesn't work
    def name(self):
        print('Getting name')
        return super().name


sub_p = SubPerson('Bill')


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


sub_person = SubPerson('Guido')
print(f'name is: {sub_person.name}')
sub_person.name = 'Bill'
print(f'After change,name is: {sub_person.name}')
sub_person.name = 30


# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

# A class with a descriptor
class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name

# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print(f'Setting name to {value}')
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)