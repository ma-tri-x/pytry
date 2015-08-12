import numpy as np
import time
import copy

class SensorDummy(object):
    def __init__(self):
        self._data = []
        self._id = 12345
        self._temp = float(np.random.uniform(-10, 50))
        self._humidity = float(np.random.uniform(20, 100))

    def _take_measurement(self):
        self._temp+= float(np.random.rand(1))
        self._humidity+= float(np.random.rand(1))

        m = {
                "sensor_id"   : self._id,
                "temperature" : self._temp,
                "humidity"    : self._humidity,
                "time"        : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }

        self._data.append(m)

    def record_time_series(self, N=10, sleep=5):
        for i in range(N):
            self._take_measurement()
            time.sleep(sleep)
        output = copy.deepcopy(self._data)
        self._data = []
        return output


