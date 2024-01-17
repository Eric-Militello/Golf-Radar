import requests
from bs4 import BeautifulSoup as bs


def scrape_weather(weather_url, min_threshold, max_threshold, bad_condition_words):

    html_text = requests.get(weather_url).text
    soup = bs(html_text, 'lxml')
    
    # Find all div elements with the specified classes
    forecast_divs = soup.find_all('div', class_='DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF')

    # Initialize a list to store weather data for each day
    weather_data_list = []

    # Loop through each forecast div
    for forecast_div in forecast_divs:
        # Extract temperature and condition information for each day
        high_temperature_str = forecast_div.find('span', class_='DetailsSummary--highTempValue--3PjlX').text.strip()
        low_temperature_str = forecast_div.find('span', class_='DetailsSummary--lowTempValue--2tesQ').text.strip()
        condition = forecast_div.find('span', class_='DetailsSummary--extendedData--307Ax').text.strip()
        day = forecast_div.find('h3', class_="DetailsSummary--daypartName--kbngc").text.strip()

        # Check if the temperature strings are not '--' before converting to integers
        if high_temperature_str != '--' and low_temperature_str != '--':
            high_temperature = int(high_temperature_str.rstrip('°'))
            low_temperature = int(low_temperature_str.rstrip('°'))

            # Add the data to the list if condition isn't rainy & max temp above threshold
            if int(high_temperature) >= int(min_threshold) and int(high_temperature) <= int(max_threshold)  and not any(word.lower() in condition.lower() for word in bad_condition_words):
                weather_data_list.append({
                    'day': day,
                    'low temperature': low_temperature,
                    'high temperature': high_temperature,
                    'condition': condition
                })

    return weather_data_list