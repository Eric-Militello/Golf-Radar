from weather import scrape_weather
from datetime import datetime, timedelta, date
import calendar
from golf import scrape_tee_times
from datetime import datetime
import re

# URLs
weather_url = "https://weather.com/weather/tenday/l/73feeffd5125f00310f1c1e3bc62cd01b936918f7d57b8df0efb48fe558e7b75"
golf_base_url = "https://www.golfnow.com/tee-times/search#qc=GeoLocation&q={}&sortby=Facilities.Distance.0&view=Course&date={}&holes={}&radius={}&timemax={}&timemin={}&players={}&pricemax=10000&pricemin=0&promotedcampaignsonly=false&hotdealsonly=false&longitude=-74.8223&latitude=39.8637"


def main(zip_code, range_value, early_time, late_time, min_temp, max_temp, conditions_blacklist, selected_players, selected_holes, no_days_to_check):
    # Scrape weather information
    days_to_check = scrape_weather(weather_url, min_temp, max_temp, conditions_blacklist)
    day_data_list = []  # New list to store day data

    days_to_check = days_to_check[0:convert_no_days(no_days_to_check)]

    for candidate in days_to_check:
        day = candidate['day']
        low_temp = candidate['low temperature']
        high_temp = candidate['high temperature']
        condition = candidate['condition']



        # Scrape tee time information for the day
        search_url = build_search_url(zip_code, convert_day_format(candidate['day']), convert_hole_format(selected_holes),
                             convert_range_format(range_value),
                             convert_late_time_format(late_time), convert_early_time_format(early_time),
                             convert_selected_players(selected_players))
        
        tee_time_info = scrape_tee_times(search_url)

        day_data_list.append({
            'day': day,
            'low_temp': low_temp,
            'high_temp' : high_temp,
            'condition' : condition,
            'tee_time_info': tee_time_info,
            'url' : search_url
        })

       

    return day_data_list
    
    

def convert_hole_format(selected_holes):
    if selected_holes[0] == '08':
        return 2
    elif selected_holes[0] == '9':
        return 1
    else:
         return 3

def convert_range_format(range_value):
     x = range_value.replace('m', '')
     return x.replace('i', '')

def convert_late_time_format(late_time):
    if  late_time == 'Any':
        return 42
    elif late_time == '8PM':
         return 40
    elif late_time == '7PM':
         return 38
    elif late_time == '6PM':
         return 36
    elif late_time == '5PM':
         return 34
    elif late_time == '4PM':
         return 32
    elif late_time == '3PM':
         return 30
    elif late_time == '2PM':
         return 28
    elif late_time == '1PM':
         return 26
    elif late_time == '12PM':
         return 24
    elif late_time == '11AM':
         return 22
    elif late_time == '10AM':
         return 20
    elif late_time == '9AM':
         return 18
    elif late_time == '8AM':
         return 16
    
def convert_early_time_format(early_time):
    if early_time == '6PM':
         return 36
    elif early_time == '5PM':
         return 34
    elif early_time == '4PM':
         return 32
    elif early_time == '3PM':
         return 30
    elif early_time == '2PM':
         return 28
    elif early_time == '1PM':
         return 26
    elif early_time == '12PM':
         return 24
    elif early_time == '11AM':
         return 22
    elif early_time == '10AM':
         return 20
    elif early_time == '9AM':
         return 18
    elif early_time == '8AM':
         return 16
    elif early_time == '7AM':
         return 14
    elif early_time == '6AM':
         return 12
    elif early_time == '5AM':
         return 10
    
def convert_selected_players(selected_players):
    if selected_players[0] == 'Any':
          return 0   
    elif selected_players[0] == '1':
        return 1 
    elif selected_players[0] == '2':
        return 2
    elif selected_players[0] == '3':
        return 3
    else:
         return 4   

def convert_day_format(candidate_day):
    # Map weekday abbreviations to weekday names
    weekday_mapping = {'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thu': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday'}

    # Split candidate_day into weekday and day_number
    split_result = candidate_day.split()

    # Check if the split operation was successful
    if len(split_result) == 2:
        weekday_abbrev, day_number = split_result
    else:
        # Handle the case when there are not enough values to unpack
        print(f"Invalid format for candidate day: {candidate_day}")
        return None  # or raise an exception, depending on your needs

    # Get the current date
    current_date = datetime.now()

    # Start a loop to generate the next ten days
    candidate_date = current_date + timedelta(days=int(day_number) - current_date.day)

    # Assemble the converted date format (MONTH+DAY+YEAR)
    converted_date = f"{calendar.month_abbr[candidate_date.month]}+{candidate_date.day:02d}+{candidate_date.year}"

    return converted_date

def build_search_url(zip_code, day, selected_holes, range_value, late_time, early_time, selected_players):
      golf_url = golf_base_url.format(zip_code, day, selected_holes, range_value, late_time, early_time, selected_players,)
      return golf_url

def convert_no_days(no_days_to_check):
     match = re.search(r'(\d+)', no_days_to_check)
     return int(match.group(1))





