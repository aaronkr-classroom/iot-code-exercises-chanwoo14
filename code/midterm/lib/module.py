class RoomSensor:
    def __init__(self, name, temperature, humidity, light):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light =light

    name = str(input("name: "))
    temperature = int(input("temperature: "))
    humidity = int(input("humidity: "))
    light = int(input("light: "))
    

    def	show_info():
        print(name, temperature, humidity, light)
    def comfort_level(self):
        temperature = self.temperature
        if temperature <=26 and temperature >=26 and humidity <=60 and humidity >=40:
            print("Comfortable")
        else temperature >=30 or humidity >=70:
            print("Warning")
        else:
            print("Normal")

        
    def light_status(self):
        light = self.light
        if light >= 200:
            print("Bright")
        else:
            print("Dark")

        
