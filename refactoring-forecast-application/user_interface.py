from display_forecast import DisplayForecast

# Defining a main function for the Weather Forecast Application interface
class UserInterface:    
    def main():
        print("Weather Forecast Application")
        while True:
            city_input = input("\nEnter the city to get the weather forecast or 'exit' to quit: ").title()
            if city_input.lower() == 'exit':
                print("Quitting the application...")
                break
            detailed_input = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed_input == 'yes':
                forecast = DisplayForecast.display_detailed_forecast(city_input)
            else:
                forecast = DisplayForecast.display_basic_forecast(city_input)
            print(forecast)