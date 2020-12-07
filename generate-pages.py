import random
import string
import csv
import os
import shutil
import fileinput

outputPath = "./outputFiles/"

htmltemplate = '<html><head><link rel="stylesheet" href="css/style.css"></head><body><div class="wrapper"><div class="container"><h1>{}</h1><h2>{}</h2><form class="form" action="submit.php"><input type="text" placeholder="Answer" id="solution" name="solution"><input type="hidden" id="puzzle" name="puzzle" value="{}"> <button type="submit" id="login-button">Submit</button></form></div><ul class="bg-bubbles"><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul></div></body></html>'
resumetemplate = 'elseif($_COOKIE[$cookie] == "{}")\n\tredirectToPuzzle("{}");\n'
formatSubmit = 'if($_POST["puzzle"] == "{}")\n\tif($_POST["solution"] == "{}")\n\t\tredirectToPuzzle("{}", "{}");\n\n'

# A function we use often
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

print("This is the generator for the puzzle site")

# Remove the output directory so there aren't any left over files
try:
    shutil.rmtree(outputPath)
except OSError:
    print ("Deletion of the directory %s failed" % outputPath)
else:
    print ("Successfully deleted the directory %s" % outputPath)

# Create the folder
os.mkdir(outputPath)

# Copy some essentials
shutil.copy("./base-files/resume.php", "{}resume.php".format(outputPath))
shutil.copy("./base-files/submit.php", "{}submit.php".format(outputPath))

output = [["id", "solution","filename"]]

# Open the CSV file
with open('input.csv', newline='') as csvfile:
    # Read it
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # Do it for every row in the CSV file
    for row in csvreader:

        # Create a random filename
        name = get_random_string(12)
        # And a random ID, for reference, and cookie things
        id = get_random_string(4)

        # Add this line to output file
        output.append([id, row[3] ,"{}.html".format(name)])

        # Generate the file
        puzzleOutput = open("{}{}.html".format(outputPath, name), "a")
        puzzleOutput.write(htmltemplate.format(row[0], row[1], id))            

        # Add file to the resume file
        with open('{}resumes.txt'.format(outputPath), 'a') as file:
            file.write(resumetemplate.format(id, name))
     
        with open("{}resume.php".format(outputPath), 'a') as file:
            file.write(resumetemplate.format(id, name))



# Write to resume the cheater case
with open('{}resumes.txt'.format(outputPath), 'a') as file:
    file.write('else\n\tredirectToPuzzle("404");')

with open('{}resumes.php'.format(outputPath), 'a') as file:
    file.write('else\n\tredirectToPuzzle("404");')

# Write everything to a output file for later reference
with open('{}output.csv'.format(outputPath), 'w') as outputfile: 
    write = csv.writer(outputfile) 
    write.writerows(output) 

# Generate the submit file
amountPuzzles = len(output)

# Do stuff for the finish page
finishPageName = get_random_string(15)

output.append([0, 0 ,"{}.php".format(finishPageName)])

# Copy and rename the file
shutil.copy("./base-files/index.html", "{}{}.html".format(outputPath,finishPageName))

print("finish file: {}".format(finishPageName))

# For every line in the output
for i in range(amountPuzzles):

    ## Do some strange logic to do some stuff
    if(i == 1):
        continue
    if(i == 0):
        i = 1

    # Write the code to a file
    with open('{}submit.txt'.format(outputPath), 'a') as file:
        file.write(formatSubmit.format(output[i][0], output[i][1], output[i+1][2], output[i+1][0]))

    with open('{}submit.php'.format(outputPath), 'a') as file:
        file.write(formatSubmit.format(output[i][0], output[i][1], output[i+1][2], output[i+1][0]))


# Going to move the rest of the files

# Create the CSS folder
os.mkdir("{}css/".format(outputPath))
shutil.copy("./base-files/css/style.css", "{}css/style.css".format(outputPath))
shutil.copy("./base-files/about.html", "{}about.html".format(outputPath))
shutil.copy("./base-files/contact.html", "{}contact.html".format(outputPath))
shutil.copy("./base-files/index.html", "{}index.html".format(outputPath))

with open("{}resume.php".format(outputPath), 'a') as file:
    file.write('}\n')
    file.write('redirectToPuzzle("{}");\n?>'.format(output[1][2]))

with open("{}submit.php".format(outputPath), 'a') as file:
    file.write("wrongAnswer();\n?>")


# Mention you are done with it all
print("I'm done! You just need to copy the outputFiles folder and the other files to the server using FTP")