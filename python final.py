#priyanshi priyanshi
#200562506
#7 april,2024
#9:33 pm
#description-gives a list of food items according to the calorie count entered by the user.
import openpyxl #importing openpyxl module to open the python file
import random #importing random module to import random numbers
import re #for regex expressions
import os#for opening text file
import pyinputplus as pyip #for using pyinputplus module
import time  # Importing the time module

# Load the Excel file
#importing the excelfile
sampleworkBook = openpyxl.load_workbook("C:/python new/Book1 python project.xlsx") 
sheet = sampleworkBook.active 

# Ask user for input
userInput = input("""Enter your dream physique (lose weight / gain weight):
                     Enter calories you want to aim around:""")

# Define empty lists for storing food and selected rows
#list for the selected food items
food = []
#list for the row number
rows = []
#list for correspoding calories
caloriesList = []

# Define function to select food items until calories reach definedcalories
def selectFood(definedCalories):
    #making the calories global
    global calories 
    calories = 0
    #while not loop until the calories reach the defined calories
    while not calories > definedCalories: 
        randoRow = random.randint(1, 50)
        #getting random cell number using rendom function
        cell = 'E' + str(randoRow)
        #another while loop for the creating unique  cell
        while not cell not in rows:  
            randoRow = random.randint(1, 50)
            cell = 'E' + str(randoRow)
        #adding the selected cells to a list    
        rows.append(cell) 
        cellContent = sheet[cell]
        #get the cell content
        caloriesContent = cellContent.value
        #storing the calories(content) in the list
        caloriesList.append(caloriesContent)
        #adding up the calories
        calories += int(caloriesContent)
        #getting the cell for the food list
        cellContentFood2 = sheet['A' + str(randoRow)]
        #cell content value for the food list
        foodContent = cellContentFood2.value
        #adding to the food list
        food.append(foodContent)
#function for printing the food items
def printFunction():
    # Global variable to store the display statement
    global displayStatement  

    # Print the header for the list of food items
    print("The food items are:")  

    # Initialize the display statement with a descriptive string
    displayStatement = "the food items are \n"  

    # Loop through each food item and its corresponding calorie count
    for i in range(len(food)):  
        # Construct a string with the food item, its calorie count, and a newline character
        displayStatement += food[i] + "\t\t" + str(caloriesList[i]) + " calories\n"  

    # Print the total calorie count
    print("Total Calories:", calories)  

    # Print the display statement showing food items and their calorie counts
    print(displayStatement)  
    
# Define the calorie target based on user input
#pattern for the calories
pattern = r'\d+' 
regexObject = re.compile(pattern)
matchObject = regexObject.search(userInput)
#if the userinput is this
if userInput == 'gain weight': 
    definedCalories = 1700
#if the userinput is this
elif userInput == 'lose weight': 
    definedCalories = 2000
#if userinput matches the correspoding pattern
elif matchObject:  
    definedCalories = int(matchObject.group())  #caste to string
else:
    print("Invalid input. Please enter 'lose weight' or 'gain weight'.")

# Call the function with the defined calories
# Start measuring time
startTime = time.time()  

try:
    # Check if the defined calorie target exceeds 3000
    if definedCalories > 3000:  
        # Raise a ValueError if the calorie target is unrealistic
        raise ValueError("Calories should not exceed 1000.")  

    # Call the selectFood function to choose food items
    selectFood(definedCalories)  

    # Display the selected food items and their calorie counts
    printFunction()  

    # Prompt the user to decide whether to print the information to a text file
    textFileInput = pyip.inputYesNo("Do you want to print it into the text file (yes/no): ", limit=3, timeout=30)
    if textFileInput == 'yes':  
        # Ask the user to input the file path where the text file will be saved
        pathDirectory = pyip.inputFilepath("Enter the path you want to place the file: ", limit=3, timeout=30, default="sorry")
        
        # Write the selected food items and their calorie counts to the text file
        testFile= open(pathDirectory, "w") 
        testFile.write(displayStatement)  
        testFile.close()
        # Confirm successful printing to the text file
        print("Data printed to the text file successfully")  

except ValueError as error:  
    # Catch any ValueError raised in the try block
    print(error)  

# Stop measuring time
endTime = time.time()  

# Calculate the total execution time
executionTime = endTime - startTime  

# Display the total execution time
print("Execution time:", executionTime, "seconds")  

