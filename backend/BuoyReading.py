# Sample class with init method
import unittest
class BuoyReading:

    def __init__(self, data):
        self.data = data

    def getData(self):
        l = []
        for f in self.getters:
            l.append(f(self))
        return l

    
    def setData(self):
        for f, d in zip(self.setters, self.data):
            f(self, d)

    def printData(self):
        for f in self.getters:
            print(f(self), end=' ')
        print()

    def checkData(self):
        if(len(self.data) == len(self.setters)):
            print("are equal")
        else:
            print("not equal")

 
    def setYear(self, year): 
        self.year = year
    def setMonth(self, month): self.month = month
    def setDay(self, day): self.day = day
    def setHour(self, hour): self.hour = hour
    def setMinute(self, minute): self.minute = minute
    def setWaveHeight(self, wave_height): self.wave_height = wave_height
    def setSwellHeight(self, swell_height): self.swell_height = swell_height
    def setSwellPeriod(self, swell_period): self.swell_period = swell_period
    def setWindWaveHeight(self, wind_wave_height): self.wind_wave_height = wind_wave_height
    def setWindWavePeriod(self, wind_wave_period): self.wind_wave_period = wind_wave_period
    def setSwellDirection(self, swell_direction): self.swell_direction = swell_direction
    def setWindWaveDirection(self, wind_wave_direction): self.wind_wave_direction = wind_wave_direction
    def setSteepness(self, steepness): self.steepness = steepness
    def setAverageWavePeriod(self, average_wave_period): self.average_wave_period = average_wave_period
    def setMeanWaveDirection(self, mean_wave_direction): self.mean_wave_direction = mean_wave_direction

    setters = [
        setYear, 
        setMonth, 
        setDay, 
        setHour, 
        setMinute, 
        setWaveHeight, 
        setSwellHeight, 
        setSwellPeriod, 
        setWindWaveHeight, 
        setWindWavePeriod, 
        setSwellDirection,
        setWindWaveDirection,
        setSteepness,
        setAverageWavePeriod,
        setMeanWaveDirection
        ]

    def getYear(self): return self.year
    def getMonth(self): return self.month 
    def getDay(self): return self.day 
    def getHour(self): return self.hour 
    def getMinute(self): return self.minute 
    def getWaveHeight(self): return self.wave_height 
    def getSwellHeight(self): return self.swell_height 
    def getSwellPeriod(self): return self.swell_period 
    def getWindWaveHeight(self): return self.wind_wave_height 
    def getWindWavePeriod(self): return self.wind_wave_period 
    def getSwellDirection(self): return self.swell_direction 
    def getWindWaveDirection(self): return self.wind_wave_direction 
    def getSteepness(self): return self.steepness 
    def getAverageWavePeriod(self): return self.average_wave_period 
    def getMeanWaveDirection(self): return self.mean_wave_direction 

    getters = [
        getYear, 
        getMonth, 
        getDay, 
        getHour, 
        getMinute, 
        getWaveHeight, 
        getSwellHeight, 
        getSwellPeriod, 
        getWindWaveHeight, 
        getWindWavePeriod, 
        getSwellDirection,
        getWindWaveDirection,
        getSteepness,
        getAverageWavePeriod,
        getMeanWaveDirection
        ]
