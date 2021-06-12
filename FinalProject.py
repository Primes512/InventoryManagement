# Cruz Lopez
# PSID: 1443590
# Date: December 2, 2020
# Final Project

import csv
from operator import itemgetter
import copy
import datetime

# creating empty list for inputs
manufacturer = []
price = []
serviceDates = []

# reading data from csv files and inputting them into manufacturer lists
with open('ManufacturerList.csv', 'r') as manufacturerList:
    manufacturerReader = csv.reader(manufacturerList)
    for row in manufacturerReader:
        manufacturer.append(row)

# sorting manufacturer list
manufacturer.sort()

# reading data from csv files and inputting them into price list
with open('PriceList.csv', 'r') as priceList:
    priceListReader = csv.reader(priceList)
    for row in priceListReader:
        price.append(row)

# sorting price list
price.sort()

# reading data from csv files and inputting them into service dates list
with open('ServiceDatesList.csv', 'r') as serviceDatesList:
    serviceDatesListReader = csv.reader(serviceDatesList)
    for row in serviceDatesListReader:
        serviceDates.append(row)

# sorting service dates list
serviceDates.sort()

# combine all list into one final list
finalList = manufacturer

# adding price list into final list
for items in range(len(finalList)):
    finalList[items].append(price[items][1])

# adding service dates list into final list
for items in range(len(finalList)):
    finalList[items].append(serviceDates[items][1])

# to move 'damaged' column to the end
for items in finalList:
    temp = items[3]
    items[3] = items[4]
    items[4] = items[5]
    items[5] = temp

# copy final list as inventory List and sort inventory list
inventoryList = copy.deepcopy(finalList)
inventoryList.sort(key=itemgetter(1, 2))

# writing the full inventory list into csv file
with open('FullInventory.csv', 'w') as newFile:
    fullInventoryWrite = csv.writer(newFile)

    for items in range(len(inventoryList)):
        fullInventoryWrite.writerow(inventoryList[items])

# copy final list as items list and sort items list by itemID
itemsList = copy.deepcopy(finalList)
itemsList.sort(key=itemgetter(0))

# opening csv files and writing the item type inventory lists
with open('LaptopInventory.csv', 'w') as newFile:
    laptopInventoryWrite = csv.writer(newFile)

    # creating empty list
    laptopInventory = []

    # adding items with laptop item type into list
    for laptop in range(len(itemsList)):
        if itemsList[laptop][2] == 'laptop':
            laptopInventory.append(itemsList[laptop])

    # removing item type from list
    for laptop in laptopInventory:
        for element in laptop:
            if element == 'laptop':
                laptop.remove(element)

    # sorting list by itemID
    laptopInventory.sort(key=itemgetter(0))

    # writing list into csv file
    for laptop in range(len(laptopInventory)):
        laptopInventoryWrite.writerow(laptopInventory[laptop])

# opening csv files and writing the item type inventory lists
with open('PhoneInventory.csv', 'w') as newFile:
    phoneInventoryWrite = csv.writer(newFile)

    # creating empty list
    phoneInventory = []

    # adding items with phone item type into list
    for phone in range(len(itemsList)):
        if itemsList[phone][2] == 'phone':
            phoneInventory.append(itemsList[phone])

    # removing item type from list
    for phone in phoneInventory:
        for element in phone:
            if element == 'phone':
                phone.remove(element)

    # sorting list by itemID
    phoneInventory.sort(key=itemgetter(0))

    # writing list into csv file
    for phone in range(len(phoneInventory)):
        phoneInventoryWrite.writerow(phoneInventory[phone])

# opening csv files and writing the item type inventory lists
with open('TowerInventory.csv', 'w') as newFile:
    towerInventoryWrite = csv.writer(newFile)

    # creating empty list
    towerInventory = []

    # adding items with phone item type into list
    for tower in range(len(itemsList)):
        if itemsList[tower][2] == 'tower':
            towerInventory.append(itemsList[tower])

    # removing item type from list
    for tower in towerInventory:
        for element in tower:
            if element == 'tower':
                tower.remove(element)

    # sorting list by itemID
    towerInventory.sort(key=itemgetter(0))

    # writing list into csv file
    for tower in range(len(towerInventory)):
        towerInventoryWrite.writerow(towerInventory[tower])

# coping final list as service list and sorting service list
serviceList = copy.deepcopy(finalList)
serviceList.sort(key=itemgetter(4))

# opening csv file and writing the past service date list
with open('PastServiceDateInventory.csv', 'w') as newFile:
    serviceDatesWrite = csv.writer(newFile)

    # creating empty list for service dates
    serviceDates = []
    newServiceDates = []

    for dates in range(len(serviceList)):

        # changing dates format from month/day/year to yearmonthday and adding them to service dates list
        serviceList[dates][4] = datetime.datetime.strptime(serviceList[dates][4], '%m/%d/%Y').strftime('%Y%m%d')
        serviceDates.append(serviceList[dates])

    for date in range(len(serviceDates)):

        # getting todays date
        currentDate = datetime.date.today()
        currentDate = currentDate.strftime('%Y%m%d')

        # comparing service dates to todays date and adding past dates to new service dates list
        if serviceDates[date][4] < currentDate:
            newServiceDates.append(serviceDates[date])

    # sorting new service dates list by oldest service date to most recent
    newServiceDates.sort(key=itemgetter(4))

    # writing list into csv file
    for date in range(len(newServiceDates)):
        newServiceDates[date][4] = datetime.datetime.strptime(newServiceDates[date][4], '%Y%m%d').strftime('%m/%d/%Y')
        serviceDatesWrite.writerow(newServiceDates[date])

# coping final list as damaged items list and sorting damaged items list
damagedItems = copy.deepcopy(finalList)
damagedItems.sort(key=itemgetter(0))

# opening csv file and writing in damaged list
with open('DamagedInventory.csv', 'w') as newFile:
    damagedInventoryWrite = csv.writer(newFile)

    # creating empty list
    damagedList = []

    # adding all damaged items into damaged list
    for damaged in range(len(damagedItems)):
        if damagedItems[damaged][5] == 'damaged':
            damagedList.append(damagedItems[damaged])

    # removing 'damaged' from damaged list
    for damage in damagedList:
        for element in damage:
            if element == 'damaged':
                damage.remove(element)

    # sorting damaged list from most expensive to least expensive
    damagedList.sort(key=itemgetter(3), reverse=True)

    # writing damaged list into csv file
    for items in range(len(damagedList)):
        damagedInventoryWrite.writerow(damagedList[items])

# creating emtpy list
itemID = []
manufacturer = []
itemType = []
price = []

# adding columns into list from final list
for item in range(len(finalList)):
  itemID.append(finalList[item][0])
  manufacturer.append(finalList[item][1])
  itemType.append(finalList[item][2])
  price.append(finalList[item][3])

# creating dictionary
itemIDDic = {'id': itemID}
manufacturerDic = {'manufacturer': manufacturer}
itemTypeDic = {'type': itemType}
priceDic = {'price': price}

# creating final dictionary
finalDic = {}
finalDic.update(itemIDDic)
finalDic.update(manufacturerDic)
finalDic.update(itemTypeDic)
finalDic.update(priceDic)

while True:
    # getting user input
    userInfo = input('Enter manufacturer and item type or "q" to quit: ')

    # if user input is 'q' then break
    if (userInfo=='q'):
        break

    # creating empty variables
    itemManu = ''
    itemTypes = ''

    # matching user info manufacturer with dictionary
    for item in finalDic['manufacturer']:
        if item in userInfo:
            itemManu = item

    # matching user info type with dictionary
    for item in finalDic['type']:
        if item in userInfo:
            itemTypes = item


    # check if manufacturer or type doesn't match dictionary
    if (itemManu == '' or itemTypes == ''):
        print('No such item in inventory')
    else:
        # creating empty list
        item = ["", "", "", 0]

        # going through dictionary
        for items in range(len(finalDic["id"])):

            # check if manufacturer and type are in the dictionary
            if (finalDic['manufacturer'][items] == itemManu and finalDic['type'][items] == itemTypes):

                # check if price is the most expensive
                if (item[3] < int(finalDic['price'][items])):

                    # store the details in the list
                    item[0] = finalDic['id'][items]
                    item[1] = finalDic['manufacturer'][items]
                    item[2] = finalDic['type'][items]
                    item[3] = finalDic['price'][items]

        # print the item
        print('Your item is: {} {} {} {}'.format(item[0], item[1], item[2], item[3]))

        # create a list to store the recommended items
        recommend = []

        # go through dictionary
        for items in range(len(finalDic['id'])):

            # check for items with same type and different manufacturer and add to recommend list
            if (finalDic['type'][items] == itemTypes and finalDic['manufacturer'][items] != itemManu):
                recommend.append([finalDic['id'][items], finalDic['manufacturer'][items], finalDic['type'][items], finalDic['price'][items]])

        # check if other items to recommend
        if (len(recommend) != 0):

            print('You may, also, consider: ')

            # go through recommend list
            for items in range(len(recommend)):

                # print the recommended items
                print('{} {} {} {}'.format(recommend[items][0], recommend[items][1], recommend[items][2], recommend[items][3]))