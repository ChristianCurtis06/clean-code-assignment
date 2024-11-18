# Defining a class with a function to parse weather data
class DataParser:
    def parse_detailed_data(data):
        if not data:
            return f"Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
    def parse_basic_data(data):
        if not data:
            return f"Weather data not available"
        city = data["city"]
        condition = data["condition"]
        return f"Weather in {city}: {condition}"