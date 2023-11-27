import datetime
import glob
import os

def remove_all_output(files):
    for file in files:
        os.remove(file)

def ascii_to_code(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w"):
            pass  # Create an empty file if it doesn't exist

    if not os.path.exists(file_name):
        print("File '{}' does not exist.".format(file_name))
        return

    with open(file_name, "r") as file:
        text = file.read()
        if not text.strip():  # Check if the file is empty
            print("File '{}' is empty.".format(file_name))
            return

        text_arr = text.split("\n")

    new_text = ""

    for txt in text_arr:
        if txt == "":
            continue

        txt = txt.replace("\\", "\\\\") 
        txt = txt.replace("\"", "\\\"") 
        txt = txt.replace("\'", "\\\'") 

        new_text += "\"" + txt + "\",\n"

    output_dir = os.path.join(os.getcwd(), "outputs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_time = datetime.datetime.now().strftime("[%H:%M:%S]")
    output_file_name = os.path.join(output_dir, "output_" + current_time + ".txt")

    with open(output_file_name, "w") as output_file:
        output_file.write(new_text)

    print("File [{}] created successfully.".format(output_file_name))

output_files = glob.glob(os.path.join(os.getcwd(), "outputs", "output*"))
# Uncomment the following code if you want to remove existing output files
# remove_all_output(output_files)

# This will convert normal ASCII to ASCII codes
ascii_to_code("ascii.txt")

