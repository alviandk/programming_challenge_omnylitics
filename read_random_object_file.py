from argparse import ArgumentParser

from custom_random.random_object import MyDefineObject




def main():
    print("================= Start read file random object ================= \n\n")

    parser = ArgumentParser()
    parser.add_argument("file_name", help="file name to be read")
    args = parser.parse_args()
    file_name = args.file_name
    
    file_open = open(file_name, "r", encoding = 'utf-8')
    random_string_objects = file_open.read()
    for random_object in random_string_objects.split(","):
        print(
            random_object.strip(), 
            "-", 
            MyDefineObject(random_object).define_object_type()
        )
    file_open.close()
    print("\n\n================= Finish read file random object ================= ")
    

if __name__=="__main__":
    main()