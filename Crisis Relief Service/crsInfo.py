# Created by : Muthia Kartika Putri
# Student ID : E1800189
# Subject Code : BIT 100
# Date : 4 May 2021
# Assignment 2
# Editor : Pycharm
# Python Version : Python 3.9

# This is the Trip Class from crsInfo.py file
class Trip:

    # Constructor with parameter from Trip Class
    def __init__(crsTrip, crisisType, description, tripDate, location,
                 numVolunteers, status):
        # initializing value from crisisType attribute
        crsTrip.crisisType = crisisType

        # initializing value from description attribute
        crsTrip.description = description

        # initializing value from tripDate attribute
        crsTrip.tripDate = tripDate

        # initializing value from location attribute
        crsTrip.location = location

        # initializing value from numVolunteers attribute
        crsTrip.numVolunteers = numVolunteers

        # initializing value from status attribute
        crsTrip.status = status

    # Getter method for crisisType variable
    # It will return crsTrip.crisisType
    def getCrisisType(crsTrip):
        return crsTrip.crisisType

    # Getter method for description variable
    # It will return crsTrip.description
    def getDescription(crsTrip):
        return crsTrip.description

    # Getter method for tripDate variable
    # It will return crsTrip.tripDate
    def getTripDate(crsTrip):
        return crsTrip.tripDate

    # Getter method for location variable
    # It will return crsTrip.location
    def getLocation(crsTrip):
        return crsTrip.location

    # Getter method for numVolunteers variable
    # It will return crsTrip.numVolunteers
    def getNumVolunteers(crsTrip):
        return crsTrip.numVolunteers

    # Getter method for status variable
    # It will return crsTrip.status
    def getStatus(crsTrip):
        return crsTrip.status

    # Setter method for crisisType variable with accept crisisType
    # parameter. It will set new value from crisisType parameter
    # to crsTrip.crisisType
    def setCrisisType(crsTrip, crisisType):
        crsTrip.crisisType = crisisType

    # Setter method for description variable with accept description
    # parameter. It will set new value from description parameter
    # to crsTrip.description
    def setDescription(crsTrip, description):
        crsTrip.description = description

    # Setter method for tripDate variable with accept tripDate
    # parameter. It will set new value from tripDate parameter
    # to crsTrip.tripDate
    def setTripDate(crsTrip, tripDate):
        crsTrip.tripDate = tripDate

    # Setter method for location variable with accept location
    # parameter. It will set new value from location parameter
    # to crsTrip.location
    def setLocation(crsTrip, location):
        crsTrip.location = location

    # Setter method for numVolunteers variable with accept
    # numVolunteers parameter. It will set new value from
    # numVolunteers parameter to crsTrip.numVolunteers
    def setNumVolunteers(crsTrip, numVolunteers):
        crsTrip.numVolunteers = numVolunteers

    # Setter method for status variable with accept status
    # parameter. It will set new value from status parameter
    # to crsTrip.status
    def setStatus(crsTrip, status):
        crsTrip.status = status

    # __str__ method for returning information
    def __str__(crsTrip):
        return crsTrip.crisisType + " : " + crsTrip.description + " at " \
               + str(crsTrip.location) + " with " + \
               str(crsTrip.numVolunteers) + " volunteers on " + \
               crsTrip.tripDate + ", with status: " + crsTrip.status


# This is the CRS Class from crsInfo.py file
class CRS:

    # Constructor with parameter from CRS Class
    def __init__(crsTrip, name):

        # initializing value from name attribute
        crsTrip.name = name

        # initializing value into array
        crsTrip.tripObject = []

    # Getter method for name variable
    # It will return crsTrip.name
    def getName(crsTrip):
        return crsTrip.name

    # Getter method for tripObject variable
    # It will return crsTrip.tripObject
    def getTripObject(crsTrip):
        return crsTrip.tripObject

    # Setter method for name variable with accept name parameter.
    # It will set new value from name parameter
    # to crsTrip.name
    def setName(crsTrip, name):
        crsTrip.name = name

    # Setter method for trip object variable with accept tripObject
    # parameter. It will set new value from tripObject parameter
    # to crsTrip.tripObject
    def setTripObject(crsTrip, tripObject):
        crsTrip.tripObject = tripObject

    # add method that accepted a parameter for adding a new data that
    # has been inputted by user
    def add(crsTrip, CRSObject):
        crsTrip.tripObject.append(CRSObject)

    # highestVolunteersTrip method for searching the highest number
    # of volunteers from all data that has been inputted by user
    def highestVolunteersTrip(crsTrip):

        # Assigning value of crsTrip.tripObject[0]
        # into highestObjectData
        highestObjectData = crsTrip.tripObject[0]

        # Looping for searching the data one by one. If the data
        # from highestObjectData.getNumVolunteers() is smaller
        # than i.getNumVolunteers(), than the value of
        # highestObjectData will be change into m where it is the
        # highest data. And It will return the highestObjectData
        # variable
        for m in crsTrip.tripObject:
            if (highestObjectData.getNumVolunteers() <
                    m.getNumVolunteers()):
                highestObjectData = m
        return highestObjectData

    # noOfTrips method for counting the number of trips
    # that have been entered by the user. It will return the number
    # of trips
    def noOfTrips(crsTrip):
        return len(crsTrip.tripObject)

    # breakdownOfTrips method for displaying the amount of data
    # from each trip that has been entered by
    # the user (Flood, Earthquake, and WildFire)
    def breakdownOfTrips(crsTrip):

        # Assigning value for breakListdata
        breakListdata = ""

        # Assigning value for countFlood
        countFlood = 0

        # Assigning value for countEarthquake
        countEarthquake = 0

        # Assigning value for countWildFire
        countWildFire = 0

        # Flood Trip
        # Assigning value "FLOOD :" for breakListData variable
        breakListdata += "FLOOD  :"

        # looping to find the amount of data
        # available for the flood trip. If the data is found,
        # than countFlood variable will be incremented by 1. And
        # the data from the countFlood variable will be added to
        # the breakListdata variable
        for m in crsTrip.tripObject:
            if m.getCrisisType() == "Flood":
                countFlood += 1
        breakListdata += str(countFlood) + "\n"

        # #Earthquake Trip
        # Assigning value "EARTHQUAKE :" for breakListData variable
        breakListdata += "EARTHQUAKE :"

        # looping to find the amount of data
        # available for the earthquake trip. If the data is found,
        # than countEarthquake variable will be incremented by 1. And
        # the data from the countEarthquake variable will be added to
        # the breakListdata variable
        for k in crsTrip.tripObject:
            if k.getCrisisType() == "Earthquake":
                countEarthquake += 1
        breakListdata += str(countEarthquake) + "\n"

        # #Wildfire Trip
        # Assigning value "WILDFIRE  :" for breakListData variable
        breakListdata += "WILDFIRE  :"

        # Looping to find the amount of data
        # available for the wildfire trip. If the data is found,
        # than countWildFire variable will be incremented by 1. And
        # the data from the countWildFire variable will be added to
        # the breakListdata variable
        for p in crsTrip.tripObject:
            if p.getCrisisType() == "WildFire":
                countWildFire += 1
        breakListdata += str(countWildFire) + "\n"

        # It will return the breakListdata variable
        return breakListdata

    # __str__ method for displaying  available information that has
    # been inputted by user.
    def __str__(crsTrip):

        # Assigning value for crsData
        crsData = ""

        # Looping to find available information. If the information
        # is found, than the data will be added to the crsData
        # variable
        for m in crsTrip.tripObject:
            crsData += str(m) + "\n"

        # It will return the crsData variable
        return crsData

    # getAllTrips method that accept a parameter for sorting the data
    # based on trip date and crisis type followed by location
    def getAllTrips(crsTrip, allTripsData):

        # Assigning crsTrip.tripObject into dataTripList variable
        dataTripList = crsTrip.tripObject

        # If the user will input "D" or "d", than the data will be
        # sorted based on the trip date. Here I used bubble sort
        # for sorting the data.
        if allTripsData == "D" or allTripsData == "d":
            for m in range(len(dataTripList)):
                for k in range(len(dataTripList) - 1):
                    if (dataTripList[k].getTripDate() >
                            dataTripList[k + 1].getTripDate()):
                        temp = dataTripList[k]
                        dataTripList[k] = dataTripList[k + 1]
                        dataTripList[k + 1] = temp

        # If the user will input "c" or "C", than the data will be
        # sorted based on the crisis type. Here I used bubble sort
        # for sorting the data.
        elif allTripsData == "C" or allTripsData == "c":
            for p in range(len(dataTripList)):
                for i in range(len(dataTripList) - 1):

                    # If the crisis type data are different,
                    # than it will be sorted based on the first
                    # alphabet.
                    if (dataTripList[i].getCrisisType() >
                            dataTripList[i + 1].getCrisisType()):
                        temp = dataTripList[i]
                        dataTripList[i] = dataTripList[i + 1]
                        dataTripList[i + 1] = temp

                    # But, if the crisis type data are same,
                    # than it will be sorted based on the location.
                    elif (dataTripList[i].getCrisisType() ==
                          dataTripList[i + 1].getCrisisType() and
                          dataTripList[i].getLocation() >
                          dataTripList[i + 1].getLocation()):
                        temp = dataTripList[i]
                        dataTripList[i] = dataTripList[i + 1]
                        dataTripList[i + 1] = temp

        # Assigning value to tripResult variable
        tripResult = ""

        # Looping to find available information. If the information
        # is found, than the data will be added to the tripResult
        # variable
        for m in dataTripList:
            tripResult += str(m) + "\n"

        # It will return the tripResult
        return tripResult

    # getTrips method that accepted 2 parameters. It will search
    # the data based on the crisis type and the status
    def getTrips(crsTrip, crisisType, statusTrips):

        # Assigning value to dataTrips variable
        dataTrips = ""

        # If the statusTrip inputted by the user is not empty. Than
        # the data will be search based on the crisis type that has
        # been inputted and also the status
        if statusTrips != "":

            # Looping for searching the data
            for m in crsTrip.tripObject:
                if (crisisType == m.getCrisisType() and
                        statusTrips == m.getStatus()):

                    # If the data is found, it will be stored into
                    # dataTrips variable
                    dataTrips += str(m) + "\n"

        # But than, if the statusTrip inputted by the user is empty.
        # Than the data will be search based on the crisis type and
        # it will shown all the data with the currents available
        # status
        else:

            # Looping for searching the data
            for k in crsTrip.tripObject:
                if crisisType == k.getCrisisType():

                    # If the data is found, it will be stored into
                    # dataTrips variable
                    dataTrips += str(k) + "\n"

        # It will return dataTrips variable
        return dataTrips

    # savetoFile method that accepted a parameter for saving the data
    # that has been inputted by user
    def saveToFile(crsTrip, tripsName):

        # Assigning value from crsTrip.name into dataTrip variable
        dataTrip = crsTrip.name + "\n"

        # Looping for searching the data that will be saved. If it
        # is found it will be stored into dataTripItem variable
        # with the specified format
        for m in crsTrip.getTripObject():
            dataTripItem = str(m.getDescription()) + "," \
                           + str(m.getCrisisType()) + "," \
                           + str(m.getTripDate()) + "," \
                           + str(m.getLocation()) + "," \
                           + str(m.getNumVolunteers()) + "," \
                           + str(m.getStatus()) + "\n"

            # Add the TripItem data into the Trip variable data
            dataTrip += dataTripItem

        # Assigning value to fOpen variable, where it will open the
        # file that is used as a place to store
        # data and write the data inside it.
        fOpen = open(tripsName, "w")

        # If the data is saved successfully,
        # the data will be displayed in the file
        print(dataTrip.rstrip(), file=fOpen)

        # The last, the file will be closed
        fOpen.close()

    # loadFromFile method that accepted a parameter for loading the
    # data that has been saved before
    def loadFromFile(crsTrip, tripsName):

        # Assigning value to fOpen variable, where it will open the
        # file that is used as a place to store data and read it.
        fOpen = open(tripsName, "r")

        # Making crsTrip.tripObject as empty list for sorting a new
        # data if there is.
        crsTrip.tripObject = []

        # Assigning value to tripsCount variable
        tripsCount = 0

        # Looping for searching the data
        for m in fOpen:
            if tripsCount == 0:
                crsTrip.name = m.rstrip()
            else:
                dataSaveSplit = m.rstrip().split(",")
                description = dataSaveSplit[0]
                crisisType = dataSaveSplit[1]
                tripDate = dataSaveSplit[2]
                location = dataSaveSplit[3]
                numVolunteers = int(dataSaveSplit[4])
                status = dataSaveSplit[5]
                newData = Trip(crisisType, description, tripDate,
                               location,
                               numVolunteers, status)
                crsTrip.add(newData)
            tripsCount = tripsCount + 1

        # The last, the file will be closed
        fOpen.close()
