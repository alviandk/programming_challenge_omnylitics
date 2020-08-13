'''
Programming Challenge
Important:
This challenge consists of two (2) parts. You are required to complete both parts. 
You can use your preferred programming language. We strongly advise you not to refer to answers on the internet.
Challenge A

Write a program that will generate four (4) types of printable random objects and store them in a single file, 
each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics. 
The alphanumerics should contain a random number of spaces before and after it (not exceeding 10 spaces). 
The output should be 10MB in size.

Sample extracted output:

hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....




Challenge B

Create a program that will read the generated file above and print to the console the object and its type. 
Spaces before and after the alphanumeric object must be stripped.

Sample output:

youruasdifafasd - alphabetical strings
127371237 - integer
asdfka12348fas - alphanumeric
13123.123 - real numbers
asjdfklasdjfklaasf - alphabetical strings
123192u3kjwekhf - alphanumeric

-END-
'''

import random
from string import ascii_lowercase


def get_alphabet():
    """
        return list of alphabet from a to z [a,b,...z]
    """
    return [character for character in ascii_lowercase]


def get_basic_number():
    """
        return list of number from 0 to 9 ["0","1",..."9"] as string
    """
    return [str(number) for number in range(10)]


def get_random_int(min_number=0, max_number=1000000):
    """
        return a random integer
    """
    return random.randint(min_number, max_number)


def get_random_length(max_length=10):
    """
        return a random length with minimum 1
    """
    return random.randint(1, max_length)


def get_random_string(char_choice, length=10):
    """
        return a random string
    """
    random_string = random.choices(char_choice, k=length)
    return "".join(random_string)


def get_random_alphabetical(length=10):
    """
        return a random string contains alphabetical a..z only
    """
    return get_random_string(get_alphabet())


def get_random_alphanumeric(length=10):
    """
        return a random string contains alphabetical a..z mixed with integer
    """
    return get_random_string(
        get_alphabet() + get_basic_number()
    )


def get_random_alphanumeric_between_space():
    """
        return a random string contains alphabetical a..z mixed with integer and between spaces
    """
    return get_random_space() + get_random_alphanumeric() + get_random_space()


def get_random_space(length=get_random_length()):
    """
        return random spaces with some length minimum 1
    """
    return " " * length


def get_random_real_number(min_number=0.0, max_number=1000000.0):
    """
        return a random float
    """
    return random.uniform(min_number, max_number)


def get_random_object(random_objects):
    """
        random object key and function correspondent value
    """
    random_object_key = random.choice(list(random_objects.keys()))

    random_object = random_objects[random_object_key]()

    return random_object


def generate_random_string_objects(random_objects, size=10):
    random_string_objects = ""
    size_random_string_objects = 0

    while size_random_string_objects < size:
        random_object = str(get_random_object(random_objects))
        random_string_objects += random_object
        if size_random_string_objects < size:
            random_string_objects += ","
        size_random_string_objects += len(random_object)

    return random_string_objects[:size]