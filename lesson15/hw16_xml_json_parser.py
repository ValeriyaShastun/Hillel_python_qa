# Implement provided methods. You need to convert the class instance to JSON or XML.
# When the user provides the command json to cli, the program should call convert_to_json,
# when providing xml to cli program should convert the class instance to xml string.
# And print it, or even better write it to a separate file.
#
# You can use third parties libraries for this.
# If you use such a library please add it to requirenment.txt
import json
from argparse import ArgumentParser
from dict2xml import dict2xml

parser = ArgumentParser(description='Our custom cli parser for Human creation')

parser.add_argument('-name', help='Name from our cli command')
parser.add_argument('-age', help='Age from our cli command')
parser.add_argument('-gender', help='Gender from our cli command')
parser.add_argument('-birth_year', help='Birth year from our cli command')
parser.add_argument('-data_type', help='Data type from our cli command you want to get Human info in')

args = parser.parse_args()
arguments = {key: value for key, value in args.__dict__.items()}


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def get_attr_dict(self):
        return self.__dict__

    def convert_to_json(self):
        with open('human.json', 'w') as file:
            file.write(json.dumps(self.get_attr_dict()))

    def convert_to_xml(self):
        with open('human.xml', 'w') as file:
            file.write(dict2xml(self.get_attr_dict(), wrap ='root', indent ="   "))


if __name__ == "__main__":
    human = Human(arguments["name"], arguments["age"], arguments["gender"], arguments["birth_year"])
    if arguments["data_type"] == "json":
        human.convert_to_json()
    elif arguments["data_type"] == "xml":
        human.convert_to_xml()

# parameters to launch the file:
# to get json file:
# -name=Alina -age=33 -gender=female -birth_year=1992 -data_type=json

# to get xml file:
# -name=Alina -age=33 -gender=female -birth_year=1992 -data_type=xml
