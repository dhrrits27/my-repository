import random
import time

def getRandomDate(startDate,endDate):
    print("get random date between,",startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'

    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate,dateFormat))

    randomTime= startTime + randomGenerator * (endTime-startTime)
    randomDate= time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("random date= ",getRandomDate("7/7/2016","12/5/2025"))