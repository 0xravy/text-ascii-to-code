import datetime
import glob
import os

def removeAllOutput(files):
    for file in files:
        os.remove(file)

def ascii_to_code(fileName):
    if not os.path.exists(fileName):
        with open(fileName, "w") as ascii_file:
            ascii_file.write("")

    if not os.path.exists(fileName):
        print("File '{}' does not exist.".format(fileName))
        return

    with open(fileName, "r") as file:
        text = file.read()
        if ("".join(text.split())) == "":
            print("File '{}' is empty.".format(fileName))
            return

        textArr = text.split("\n")

    newText = ""

    for txt in textArr:
        if txt == "":
            continue

        txt = txt.replace("\\", "\\\\") 
        txt = txt.replace("\"", "\\\"") 
        txt = txt.replace("\'", "\\\'") 

        newText += "\"" + txt + "\",\n"

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    current_time = datetime.datetime.now().strftime("[%H:%M:%S]")
    output_file_name = "./outputs/output_" + current_time + ".txt"

    with open(output_file_name, "w") as output_file:
        output_file.write(newText)

    print("File [{}] created successfully.".format(output_file_name))

outputFiles = glob.glob("./outputs/output*")
# Uncomment the following code if you want to remove existing output files
# removeAllOutput(outputFiles)

# This will convert normal ASCII to ASCII codes
ascii_to_code("ascii.txt")
