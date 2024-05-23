# Weather Information Script

This Python script retrieves the current temperature of a specified city using the WeatherAPI and reads it aloud using the `pyttsx3` text-to-speech library.

## Features

- Fetches current weather data for a specified city.
- Uses the WeatherAPI to get accurate and up-to-date weather information.
- Converts the temperature data to speech and reads it aloud using the `pyttsx3` library.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3 installed on your computer.
- You have an internet connection to fetch weather data.

## Installation

1. Clone this repository or download the script file.

2. Install the required libraries. You can use pip to install them:

    ```bash
    pip install requests pyttsx3
    ```

3. Get your API key from [WeatherAPI](https://www.weatherapi.com/) by signing up. Replace the `YOUR_API_KEY` in the script with your actual API key.

## Usage

1. Run the script:

    ```bash
    python weather_script.py
    ```

2. Enter the name of the city when prompted:

    ```plaintext
    Enter the name of the city..
    ```

3. The script will print the current temperature of the specified city and read it aloud.

## Example

```plaintext
Enter the name of the city..
London
The current temperature of London is 15.0
