from argparse import ArgumentParser

from custom_random.random_generator import (
    get_random_alphabetical, 
    get_random_alphanumeric_between_space,
    get_random_int,
    get_random_real_number,
    generate_random_string_objects
)

from random import choice


def main():
    print("Start generate random object")
    random_objects = {
        "alphabetical": get_random_alphabetical,
        "integer": get_random_int,
        "alphanumeric": get_random_alphanumeric_between_space,
        "real": get_random_real_number
    }

    parser = ArgumentParser()
    parser.add_argument("--file_name", help="file name to be created")
    args = parser.parse_args()
    if args.file_name:
        file_name = args.file_name
    else:
        file_name = "random_object.txt"

    file_open = open(file_name, "w", encoding = 'utf-8')
    random_string_objects = generate_random_string_objects(random_objects, size=10*1024*1024)
    file_open.write(random_string_objects)
    file_open.close()
    print("Finish generate random object")
    
    
if __name__=="__main__":
    main()