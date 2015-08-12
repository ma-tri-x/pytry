from spy.sensor import SensorDummy
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://192.168.1.121:27017/')
    sensor = SensorDummy()
    db = client.test
    sdata = db.sensordata

    for i in range(10):
        print "Take Measurement"
        data = sensor.record_time_series(10, 1)
        print "Send data to mongodb .."
        sdata.insert_many(data)

if __name__=='__main__':
    main()
