import re


def replace_string(template, string_to_be_replaced, replacing_string):
    return template.replace(string_to_be_replaced, replacing_string)

def gen_text_from_template(template, replaced_to_replacing_map):
    for replaced, replacing in replaced_to_replacing_map.items():
        template = replace_string(template, replaced, replacing)
    return template

def get_string_from_file_external_dep(filename):
    f = open(filename, "r")
    cont = f.read()
    f.close()
    return cont

def find_triple_angular_markers_from_template(template):
    # use regex to find the angular brackets
    angular_re = re.compile(r"<<<.*?>>>")
    matched_triple_angular_markers = angular_re.findall(template)
    result_map = {}
    for item in matched_triple_angular_markers:
        result_map[item] = None
    return result_map

class FileIO:
    def __init__(self):
        self.user_inputs = {}
    def get_user_input_for_list_external_dep(self, list):
        for item in list:
            user_input = input("Please enter the value for " + item + ":")
            self.user_inputs[item]=user_input
        return self.user_inputs

def main(filename):
    file_content = get_string_from_file_external_dep(filename)
    triple_angular_markers = find_triple_angular_markers_from_template(file_content).keys()
    fileIO = FileIO()
    user_inputs = fileIO.get_user_input_for_list_external_dep(triple_angular_markers)
    gen_text = gen_text_from_template(file_content, user_inputs)
    return gen_text

if(__name__ == "__main__"):
    gen_text = main("template.txt")
    print("************************************************************************************************")
    print(gen_text)
    print("************************************************************************************************")