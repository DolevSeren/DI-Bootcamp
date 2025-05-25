import pyowm
import matplotlib.pyplot as plt
import pytz
import datetime
from pyowm.utils import config
from pyowm.utils import timestamps
import pkg_resources


# Initialize the OpenWeatherMap API with your API key
API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
owm = pyowm.OWM(API_KEY)  # Instantiate the OpenWeatherMap API object
mgr = owm.weather_manager()


def get_city_id(city_name):
    """Get the city ID for a given city name."""
    observation = mgr.weather_at_place(city_name)
    city = observation.location
    return city.id


def get_weather_data(city_id):
    """Retrieve weather forecast for the given city ID."""
    forecast = mgr.forecast_at_id(city_id, '3h')
    return forecast


def init_plot():
    """Initialize the plot with labels, title, and other settings."""
    plt.figure(figsize=(10, 5))
    plt.title("3-Day Humidity Forecast")
    plt.xlabel("Time of Day")
    plt.ylabel("Humidity (%)")


def plot_temperatures(forecast):
    """Plot temperatures and humidity data for the 3-day forecast."""
    humidity = []
    times = []
    for weather in forecast.forecast.weathers:
        # Extract the time and humidity
        time = datetime.datetime.utcfromtimestamp(weather.reference_time()).strftime('%H:%M')
        humidity.append(weather.humidity)
        times.append(time)

    # Plotting the humidity data
    plt.bar(times, humidity, color='skyblue')

    return times, humidity


def write_humidity_on_bar_chart(times, humidity):
    """Display the humidity value on each bar."""
    for i in range(len(times)):
        plt.text(i, humidity[i] + 2, f'{humidity[i]}%', ha='center', va='bottom', fontsize=10)


def display_weather(city_name):
    """Display weather and plot the humidity bar chart for a city."""
    city_id = get_city_id(city_name)
    forecast = get_weather_data(city_id)

    # Display the weather details
    print(f"Weather forecast for {city_name}:")
    for weather in forecast.forecast.weathers[:9]:  # Get the first 3 days (each has 3 intervals)
        dt = datetime.datetime.utcfromtimestamp(weather.reference_time()).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Time: {dt}, Temp: {weather.temperature('celsius')['temp']}°C, Humidity: {weather.humidity}%")

    # Initialize plot
    init_plot()

    # Plot temperature data
    times, humidity = plot_temperatures(forecast)

    # Write humidity values on the bars
    write_humidity_on_bar_chart(times, humidity)

    # Show the plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    city_name = input("Enter a city name (e.g., 'Tel Aviv'): ").strip()
    display_weather(city_name)
