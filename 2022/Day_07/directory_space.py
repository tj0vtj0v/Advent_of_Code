import string
import os
inputfile = open(os.path.join(os.path.dirname(__file__), 'input_paths.txt'), "r")
inputcommands = inputfile.readlines()

found_dir = []
def clear_ident_dir(direct, found_dir):
    if direct in found_dir:
        direct = direct + "a"
        return clear_ident_dir(direct, found_dir)
    else:
        return direct

used_diskspace = 0
structure = ""
tree = []
direct = ""
for command in inputcommands:
    command = command.replace("\n", "")
    if "$" in command:
        if "cd" in command and ".." not in command:
            if direct != "":
                structure = structure + direct + ", " + str(tree) + "\n"
                found_dir.append(direct)            
            direct = command.split(" ")[2]
            direct = clear_ident_dir(direct, found_dir)
            tree = []
    else:
        if "dir" in command:
            direct_f = command.split(" ")[1]
            direct_f = clear_ident_dir(direct_f, found_dir)
            tree.append("dir " + direct_f)
        else:
            tree.append(command)
            used_diskspace+= int(command.split(" ")[0])

structure = structure + direct + ", " + str(tree)

def get_format(line:str):
    direct = line.split(", ['")[0]
    help_content = line.split(", ['")[1].replace("']", "")
    content = help_content.split("', '")
    return direct, content

def get_size(content, done:list):
    total_size = 0
    for element in content:
        element = str(element)
        if "dir" in element:
            direct = element.split(" ")[1]
            for line in structure.split("\n"):
                if direct in line.split(", [")[0] and direct not in done:
                    done.append(direct)
                    direct, content = get_format(line)
                    total_size +=  get_size(content, done)[0]
        else:
            total_size += int(element.split( )[0])
    return total_size, done

structured_p_info = ""
for line in structure.split("\n"):
    direct, content = get_format(line)
    done = []
    structured_p_info = structured_p_info + line + ", " + str(get_size(content, done)[0]) + "\n"

complete_sum = 0
for line in structured_p_info.split("\n"):
    save = 0
    for char in line:
        if char in string.ascii_lowercase:
            save = 1
    if save == 1:
      if int(line.split("], ")[1]) <= 100000:
          complete_sum += int(line.split("], ")[1])
print("storage size sum = " + str(complete_sum))

free_diskspace = 70000000-used_diskspace
additional_needed_diskspace = 30000000-free_diskspace
min_overdelete = 70000000
for line in structured_p_info.split("\n"):
    save = 0
    for char in line:
        if char in string.ascii_lowercase:
            save = 1
    if save == 1:
        direction_size = int(line.split("], ")[1])
        if direction_size >= additional_needed_diskspace:
            if int(line.split("], ")[1]) < min_overdelete:
                min_overdelete = int(line.split("], ")[1])
print("minimum to delete = " + str(min_overdelete))