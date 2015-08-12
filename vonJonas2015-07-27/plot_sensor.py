import datetime
import matplotlib.pyplot as plt
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://192.168.1.121:27017/')
    db = client.test
    sdata = db.sensordata

    output = list(sdata.find())

    temp = [x['temperature'] for x in output]

    get_time = lambda x: datetime.datetime.strptime(x['time'], '%Y-%m-%d %H:%M:%S')
    time = [get_time(x) for x in output]

    humidity = [x['humidity'] for x in output]

    plt.plot(time, temp)
    plt.plot(time, humidity)
    plt.show()




if __name__=='__main__':
    main()
