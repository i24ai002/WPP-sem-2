class Converter:
    conversion_factors = {
        'inches': 1,
        'feet': 1 / 12,
        'yards': 1 / 36,
        'miles': 1 / 63360,
        'millimeters': 25.4,
        'centimeters': 2.54,
        'meters': 0.0254,
        'kilometers': 0.0000254
    }

    def __init__(self, length, unit):
        self.length_in_inches = (length/self.conversion_factors[unit])

    def inches(self):
        return self.length_in_inches * self.conversion_factors['inches']
    
    def feet(self):
        return self.length_in_inches * self.conversion_factors['feet']
    
    def yards(self):
        return self.length_in_inches * self.conversion_factors['yards']
    
    def miles(self):
        return self.length_in_inches * self.conversion_factors['miles']
    
    def millimeters(self):
        return self.length_in_inches * self.conversion_factors['millimeters']
    
    def centimeters(self):
        return self.length_in_inches * self.conversion_factors['centimeters']
    
    def meters(self):
        return self.length_in_inches * self.conversion_factors['meters']
    
    def kilometers(self):
        return self.length_in_inches * self.conversion_factors['kilometers']


c = Converter(9, 'inches')
print(c.feet())     
print(c.yards())   
print(c.miles())   
print(c.millimeters())
print(c.centimeters())
print(c.meters())    
print(c.kilometers()) 