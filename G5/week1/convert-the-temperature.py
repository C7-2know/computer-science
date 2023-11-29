class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius+273.15
        fahranite=celsius*1.80 +32
        return(kelvin, fahranite)
