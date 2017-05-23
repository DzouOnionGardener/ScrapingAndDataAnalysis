import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb

class analyzer(object):
    def __init__(self):
        pass

    def retrieveFromDB(self):
        username = raw_input("mySQL login ID: ")
        password = raw_input("mySQL login password: ")
        DB = MySQLdb.connect("localhost", username, password, "Restaurants")

        ##retrieve Data from mySQL server then stores into resData
        self.resData = pd.read_sql('SELECT * FROM Restaurants.restaurantTable', con=DB)

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
            ax1.axis('equal')
            plt.savefig('piechart.png')
            plt.show()
        else:
            pass


if __name__ == "__main__":
    a = analyzer()
    a.retrieveFromDB()
    a.CountPriceRange()
