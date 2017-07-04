from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb
from colorize import *
import Image


class analyzer(object):
    def __init__(self):
        self.username = raw_input("mySQL login ID: ")
        self.password = raw_input("mySQL login password: ")

    def retrieveFromDB(self):
        DB = MySQLdb.connect("localhost", self.username, self.password, "Restaurants")
        ##retrieve Data from mySQL server then stores into resData
        self.resData = pd.read_sql('SELECT * FROM Restaurants.restaurantTable', con=DB)
        #for index, a in self.resData.iterrows():
        #    if a['price'] == '$$':
        #        print "hello"


    def CountPriceRange(self):
        # columns: name(varchar(255)), rating(decimal), price(varchar(6)), area(varchar(255)), addr(varchar(255))
        self.priceRangeCount = pd.DataFrame(self.resData.groupby('price').size().rename('count')).sort_values(by=['count'], ascending=False)
        print self.priceRangeCount
        #self.ranges = self.priceRangeCount.set_index("price")
        #store the priceRangeCount in a pandas data frame format; else it'll print with all the column names as well
        WantToPrint = raw_input("would you like to see the Pie Chart?(Y/N) ")
        if WantToPrint == 'Y' or WantToPrint == 'y':
            #plt.figure(figsize=(8,8))
            #self.resData.groupby('price').count().plot(kind='pie', y = 'count', startangle = 90, shadow = False, labels = self.resData['price'], legend = False, fontsize=14)
            #plt.show()
            labels = self.priceRangeCount.index.values.tolist()
            for i,e in enumerate(labels):
                if e == '$':
                    labels[i] = "\$"
                if e == '$$':
                    labels[i] = "\$\$"
                if e == '$$$':
                    labels[i] = "\$\$\$"
                if e == '$$$$':
                    labels[i] = "\$\$\$\$"
            size = self.priceRangeCount['count'].values.tolist()
            fig1, ax1 = plt.subplots(figsize=(16, 8))
            ax1.pie(size, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
            plt.legend(size, loc='upper right')
            ax1.axis('equal')
            plt.savefig('piechart.png')
            plt.show()
        else:
            pass


    def AreaPriceRange(self):
        ## store DISTINCT(AREA) into a list
        DB = MySQLdb.connect("localhost", self.username, self.password, "Restaurants")
        self.AreaList = pd.read_sql('SELECT DISTINCT(Restaurants.restaurantTable.area) FROM Restaurants.restaurantTable', con=DB)
        self.Areas = self.AreaList['area'].values.tolist()

        ## get a count of each price range from each area and put it into a dictionary
        ## iterate through the entire database, if DB.area entry matches the ones in the list, look at the price range
        ## then add the price range to the dictionary? maybe also calculate the average
        ## convert each $ to a number 1-to-4. sum / size of the array = average
        """
        ##counts the number of times each area appears
        SELECT distinct(COUNT(Restaurants.restaurantTable.area)) as p1, Restaurants.restaurantTable.area
        FROM Restaurants.restaurantTable
        GROUP by Restaurants.restaurantTable.area
        """
        ## create a dictionary that'll store the area name and the average
        self.AreaAverages = dict()
        for a in self.Areas:
            ## for each element in areas list
            ## find it in the resData by way of 'area'
            sum = 0
            counter = 0
            for index, e in self.resData.iterrows():
                if a == e['area']:
                    if e['price'] == '$':
                        sum += 1
                    if e['price'] == '$$':
                        sum += 2
                    if e['price'] == '$$$':
                        sum += 3
                    if e['price'] == '$$$$':
                        sum += 4
                    counter += 1
            avg = (sum/counter)
            self.AreaAverages.update({a: avg})
        print self.AreaAverages

    def heat_map(self):
        for key, avg in self.AreaAverages.iteritems():
            colorize(key, avg)
        try:
            image = Image.open('map/NYC.png')
            image.show()
        except Exception, e:
            print str(e)



if __name__ == "__main__":
    a = analyzer()
    a.retrieveFromDB()
    a.AreaPriceRange()
    ##a.CountPriceRange()
    a.heat_map()
