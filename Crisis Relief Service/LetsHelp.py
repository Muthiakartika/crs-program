# Created by : Muthia Kartika Putri
# Student ID : E1800189
# Subject Code : BIT 100
# Date : 4 May 2021
# Assignment 2
# Editor : Pycharm
# Python Version : Python 3.9

# Import Trip class and CRS class from crsInfo.py to LetsHelp.py
from crsInfo import *

# Import library datetime
from datetime import datetime


# menu method for display menus available in this programme
def menu():
    print("1. Add a trip")
    print("2. Display all trips")
    print("3. Display summary information for all trips ")
    print("4. Display trips with criteria entered by user")
    print("5. Sort and display trips")
    print("6. Saving trips to file")
    print("7.  Loading trips from file\n\n")
    print("0. Exit\n\n")

    # Choosing the menu above and stored into choice variable
    choice = int(input("Your choice: "))

    # It will return choice variable
    return choice


# This is addDataTrip method for adding a new data
def addDataTrip():
    # Information for adding new data
    print("Adding trip: ")

    # Inputting description
    desc = input("Description: ")

    # Inputting crisis type
    crisisType = input(
        "Crisis type (Flood, Earthquake, WildFire): ")

    # Inputting date
    date = input("Date (dd-mm-yyyy): ")

    # This code will add the date data into the library
    dateObj = datetime.strptime(date, '%d-%m-%Y')

    # Inputting location
    location = input("Location: ")

    # Inputting number of volunteers
    numVolunteers = int(input("Number of volunteers: "))

    # Inputting status
    status = input("Status (Success, Pending, Failure): ")

    # Store the data that has been inputted into Trip class
    crsData = Trip(crisisType, desc, dateObj.strftime(
        '%Y-%m-%d'), location,
                   numVolunteers, status)

    # return crsData variable
    return crsData


# This is displayAllTrips method for displaying the information
def displayAllTrips(listCRS):
    # Storing crsList.noOfTrips into dataTrip variable
    dataTrip = listCRS.noOfTrips()

    # If the data that exist is the only one, than this
    # information will be shown
    if dataTrip == 1:
        print("The trip is")
        print(listCRS.__str__())

    # If the data that exist is more than one, than this
    # information will be shown
    elif dataTrip >= 1:
        print("The trip are")
        print(listCRS.__str__())

    # But, if there is no data that exist than this
    # information will be shown
    else:
        print("No trip in collection!")


# This is summaryInformation method for displaying the
# summary information
def summaryInformation(listCRS):
    # Storing crsList.noOfTrips into dataTrips variable
    dataTrip = listCRS.noOfTrips()

    # Storing crsList.highestVolunteersTrip into
    # highestData variable
    highestData = listCRS.highestVolunteersTrip()

    # Storing crsList.breakdownOfTrips into
    # breakDownData variable
    breakDownData = listCRS.breakdownOfTrips()

    # It will display Summary Information based on the
    # number of trips that exist, the highest number of
    # volunteers from the trips, and also the breakdown
    # list based on the crisis type
    print("Summary information:")
    print(20 * "~")
    print("Number of trips: " + str(dataTrip))
    print("Trip with highest number of volunteers: "
          "\n +" + str(highestData) + "\n\n")
    print("Breakdown of trips according to crisis "
          "type:\n" + breakDownData)


# This is displayTripwithCriteria method for displaying the
# information based on crisis type and status
def displayTripwithCriteria(listCRS):
    # Input the crisis type that want to display
    crisisType = input("Which type of trip (Flood, "
                       "Earthquake, WildFire)? ")

    # Input the status trip that want to display(optional)
    statusTrip = input("Status: Success, Pending, Failure, "
                       "or <Enter> for all: ")

    # Storing the data that has been inputted into getTrips
    # method in CRS class and it will be stored again into
    # resultTrip variable
    resultTrip = listCRS.getTrips(crisisType, statusTrip)

    # Return resultTrip variable
    return resultTrip


# This is sortingTrip method for displaying the
# information based on sorting criteria by Date or Crisis Type
# followed by location
def sortingTrip(listCRS):
    # Inputting criteria that want to be displayed
    sortingCriteria = input("Sorting criteria: Trip <D>ate or"
                            "<C>risis followed by location: ")

    # Storing the data that has been inputted into getAllTrips
    # method in CRS class and it will be stored again into
    # sortingData variable
    sortingData = listCRS.getAllTrips(sortingCriteria)

    # Return sortingData variable
    return sortingData


# This is savingTrip method for saving the data that has been
# inputted before.
def savingTrip():
    # Inputting the file name as a place for storing the data
    saveTrip = input("File name? ")

    # Return the saveTrip variable
    return saveTrip


# This is loadTrip method for loading the data that has been
# saved before.
def loadTrip():
    # Inputting the file name that has been saved before
    openTrip = input("File name? ")

    # Return the openTrip variable
    return openTrip


# This is the main method from LetsHelp.py
def helpTrips():
    # Assigning value to dataSave variable
    dataSave = False

    # Inputting the crs name by user
    CRSname = input("What's the name of Crisis relief Service: ")

    # The data that has been inputted will stored into array from
    # CRS class
    crsList = CRS(CRSname)

    # Print the crs name that has been inputted and stored before
    print(crsList.getName())

    # Print "~" 20 times
    print("~" * 20)

    # Calling menu method
    menuChoice = menu()

    # While loop for looping the programme
    while menuChoice != 0:

        # If user choose number 1, than the user will be order to
        # add a new data. Here in inputting the date data,
        # I use string as the variable type and use the date
        # library to set the date to match the problem.
        if menuChoice == 1:

            # Calling addDataTrip method and stored the data into
            # newDataTrip variable
            newDataTrip = addDataTrip()

            # This code is used to store the data that has been
            # inputted above and entered it into the add method in
            # the CRS class
            crsList.add(newDataTrip)

            # Notification message if the data has been saved
            print("Addition Success...")

        # If the user choose number 2, than the programme will
        # display all information
        elif menuChoice == 2:

            # Calling displayAllTrips method
            displayAllTrips(crsList)

        # But, if the user choose number 3, than the programme will
        # display all summary of the data exist
        elif menuChoice == 3:

            # Calling summaryInformation method
            summaryInformation(crsList)

        # If the user choose number 4, than the programme will
        # display the information based on the crisis type and the
        # status
        elif menuChoice == 4:

            # Calling summaryInformation method and stored the data
            # into displayWithCriteria method
            displayWithCriteria = displayTripwithCriteria(crsList)

            # If the data inputted is available, than it will
            # display the data based on the crisis type and status
            # trip(optional) that has been inputted above
            if displayWithCriteria != "":
                print("The trip (s): \n" + displayWithCriteria)

            # But if data inputted is unavailable, than it will
            # display this notification
            else:
                print("No trips satisfying the chosen condition.")

        # If user choose number 5, than this programme will display
        # the information based on the Date or Crisis type and it
        # will be followed by the location
        elif menuChoice == 5:

            # Calling sortingTrip method and stored the data into
            # sortingDataTrips variable
            sortingDataTrips = sortingTrip(crsList)

            # It will display the information based on the criteria
            # that has been inputted above
            print("Result: \n" + sortingDataTrips)

        # If the user choose number 6 than it will order the user
        # to save the data that has been inputted before
        elif menuChoice == 6:

            # Storing crsList.noOfTrips into dataTrips variable
            dataTrip = crsList.noOfTrips()

            # If dataTrip is not empty, that the user will be
            # ordered to input the file name as a place to store
            # the data that has been entered before. And it will be
            # stored into saveToFile method in CRS class and the
            # status of dataSave will be true that means the data
            # has been saved
            if dataTrip != 0:

                # Calling savingTrip method and store the data into
                # saveData variable
                saveData = savingTrip()
                crsList.saveToFile(saveData)
                print("Data successfully saved...")
                dataSave = True

            # But, if dataTrip is empty, than it will display this
            # notification
            else:
                print("No trip in collection!")

        # If user choose number 7, than the programme will load the
        # data that has been saved before
        elif menuChoice == 7:

            # Storing crsList.noOfTrips into dataTrips variable
            dataTrip = crsList.noOfTrips()

            # If dataTrip is not empty, and also dataSave is not
            # True that means no data has been save, than the
            # programme will give the user some choices for saving
            # the data or not
            if dataTrip != 0 and dataSave != True:
                choice = input("Do you want to save current trips? "
                               "(Y/N) ")

                # If the user choose to save the data, than they
                # will save their data and after that will load
                # another data based on the file name
                if choice == "y" or choice == "Y":

                    # Calling savingTrip method and
                    # store the data into saveData variable
                    saveData = savingTrip()
                    crsList.saveToFile(saveData)
                    print("Data successfully saved...\n")

                    # Calling loadTrip method and
                    # store the data into loadData variable
                    loadData = loadTrip()
                    crsList.loadFromFile(loadData)
                    print("Data has been successfully loaded...")
                    dataSave = False

                # But, if user choose to not save the data,
                # than the programme will order them to input the
                # file name to load the data. And the dataSave will
                # be False that means, the data that has been
                # inputted before is not being save in a file
                else:

                    # Calling loadTrip method and
                    # store the data into loadData variable
                    loadData = loadTrip()
                    crsList.loadFromFile(loadData)
                    print("Data has been successfully loaded...")
                    dataSave = False

            # But, if the data has been saved before, than the
            # programme will order them to input the file name that
            # want to be loaded without giving some choices
            else:

                # Calling loadTrip method and
                # store the data into loadData variable
                loadData = loadTrip()
                crsList.loadFromFile(loadData)
                print("Data has been successfully loaded...")

        # Display the crs name that has been inputted and stored
        # before
        print("\n" + crsList.getName())

        # Print "~" 20 times
        print(20 * "~")

        # Calling menu method
        menuChoice = menu()

    # If the user choose number 0, than it will exit from
    # this programme
    if menuChoice == 0:
        print("Thanks for using CRS application.....")


# Calling main method
helpTrips()
