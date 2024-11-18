from data_parser import DataParser
from data_fetcher import WeatherDataFetcher

# Defining a class with functions to display basic or detailed weather forecast for a city
class DisplayForecast:
    def display_detailed_forecast(city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        return DataParser.parse_detailed_data(data)

    def display_basic_forecast(city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        return DataParser.parse_basic_data(data)