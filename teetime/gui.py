import tkinter as tk
from tkinter import *
from main import main
import webbrowser


class GolfApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Golf Radar")


        
        # Variables to store user selections
        self.zip_code_var = StringVar()
        self.range_var = StringVar()
        self.early_time_var = StringVar()
        self.late_time_var = StringVar()
        self.min_temp_var = StringVar()
        self.max_temp_var = StringVar()
        self.conditions_blacklist_var = tk.StringVar()
        self.selected_players_var = tk.StringVar()
        self.selected_holes_var = tk.StringVar()
        self.no_days_to_check_var = tk.StringVar()

        #Font Styles used
        label_font = ('Arial', 20, 'bold')
        
       



        # Location Section
        self.location_frame = tk.Frame(self.root)
        self.location_frame.grid(column=0, row=0, padx=10, sticky=N)

        self.location_label = tk.Label(self.location_frame, text="Location:", font=label_font)
        self.location_label.grid(column=0, row=0, columnspan=2, padx=10, sticky=N)

        zip_label = tk.Label(self.location_frame, text='Zip Code')
        zip_label.grid(column=0, row=1, pady=10, sticky=W)

        self.zip_entry = tk.Entry(self.location_frame, textvariable=self.zip_code_var)
        self.zip_entry.grid(column=1, row=1, sticky=W, padx=10)

        self.range_label = tk.Label(self.location_frame, text="Range:")
        self.range_label.grid(column=0, row=2, sticky=W)

        range_options = [
            '25mi',
            '50mi',
            '75mi',
            '100mi'
        ]

        default_range_value = StringVar(self.location_frame)
        default_range_value.set(range_options[1])

        self.range_drop = tk.OptionMenu(self.location_frame, self.range_var, *range_options)
        self.range_drop.grid(column=1, row=2, sticky=W)


        # Time Section
        self.time_frame = tk.Frame(self.root)
        self.time_frame.grid(column=1, row=0, padx=10, pady=(0,20))

        self.time_label = tk.Label(self.time_frame, text="Time:", font=label_font)
        self.time_label.grid(column=0, row=0, columnspan=2, padx=10, sticky=N)

        self.early_label = tk.Label(self.time_frame, text='Earliest Start')
        self.early_label.grid(column=0, row=1, sticky=W)

        self.late_label = tk.Label(self.time_frame, text='Latest Start')
        self.late_label.grid(column=0, row=2, sticky=W)

        #dropdown menu options
        early_time_options = [
            '5AM',
            '6AM',
            '7AM',
            '8AM',
            '9AM',
            '10AM',
            '11AM',
            '12PM',
            '1PM',
            '2PM',
            '3PM',
            '4PM',
            '5PM',
            '6PM',
        ]

        late_time_options = [
            '8AM',
            '9AM',
            '10AM',
            '11AM',
            '12PM',
            '1PM',
            '2PM',
            '3PM',
            '4PM',
            '5PM',
            '6PM',
            '7PM',
            '8PM',
            'Any',
        ]

        default_early_time_value = StringVar(self.time_frame)
        default_early_time_value.set(early_time_options[0])

        default_late_time_value = StringVar(self.time_frame)
        default_late_time_value.set(late_time_options[0])

        self.early_time_drop = tk.OptionMenu(self.time_frame, self.early_time_var, *early_time_options)
        self.early_time_drop.grid(column=1, row=1)

        self.late_time_drop = tk.OptionMenu(self.time_frame, self.late_time_var, *late_time_options)
        self.late_time_drop.grid(column=1, row=2)

        no_days_options = [
            '1 day',
            '2 days',
            '3 days',
            '4 days',
            '5 days',
            '6 days',
            '7 days',
            '8 days',
            '9 days',
            '10 days',
            '11 days',
            '12 days',
            '13 days',
            '14 days',
        ]

        self.no_days_label = tk.Label(self.time_frame, text='# of days to check')
        self.no_days_label.grid(column=0, row=3, sticky=W)
        self.no_days_selections = tk.OptionMenu(self.time_frame, self.no_days_to_check_var, *no_days_options)
        self.no_days_selections.grid(column=1, row=3)
   
        # WeatherSection
        self.weatherFrame = tk.Frame(self.root)
        self.weatherFrame.grid(column=0, row=1, padx=10, sticky=N)

        self.weather_label = tk.Label(self.weatherFrame, text="Weather:", font=label_font)
        self.weather_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        self.min_temp_label = tk.Label(self.weatherFrame, text='Min Temp (°F)')
        self.min_temp_label.grid(column=0, row=1)

        self.min_temp_entry = tk.Entry(self.weatherFrame, textvariable=self.min_temp_var)
        self.min_temp_entry.grid(column=1, row=1, padx=10)

        self.max_temp_label = tk.Label(self.weatherFrame, text="Max Temp (°F)")
        self.max_temp_label.grid(column=0, row=2, sticky=tk.W)

        self.max_temp_entry = tk.Entry(self.weatherFrame, textvariable=self.max_temp_var)
        self.max_temp_entry.grid(column=1, row=2, padx=10)

        self.blacklist_label = tk.Label(self.weatherFrame, text='Conditions Blacklist')
        self.blacklist_label.grid(column=0, columnspan=2, row=3, sticky=NSEW,)

        self.blacklist_list = tk.Listbox(self.weatherFrame, selectmode = "multiple", exportselection=False)
        self.blacklist_list.grid(column=0, columnspan=2, row=4, sticky=NSEW, padx= 10)
        
        list_elements = ['Rain', 'Snow', 'Showers', 'Wind']

        for element in list_elements:
            self.blacklist_list.insert(END, element)


        #Golf Section
        self.golf_frame = tk.Frame(self.root)
        self.golf_frame.grid(column=1, row=1, sticky=N, padx=10)

        self.golf_label = tk.Label(self.golf_frame, text='Golf:', font=label_font)
        self.golf_label.grid(row=0, column=0, columnspan=2)

        self.player_label = tk.Label(self.golf_frame, text='# of Golfers')
        self.player_label.grid(column=0, row=1)

        self.player_group_list = tk.Listbox(self.golf_frame, selectmode=SINGLE, exportselection=False)
        self.player_group_list.grid(column=0, row=2)

        self.player_group_list.insert(0, "1")
        self.player_group_list.insert(1, "2")
        self.player_group_list.insert(2, "3")
        self.player_group_list.insert(3, "4")
        self.player_group_list.insert(4, "Any")

        self.holes_label = tk.Label(self.golf_frame, text='# of Holes')
        self.holes_label.grid(column=1, row=1)

        self.hole_group_list = tk.Listbox(self.golf_frame, selectmode=SINGLE, exportselection=False)
        self.hole_group_list.grid(column=1, row=2, padx=5)

        self.hole_group_list.insert(0, '9')
        self.hole_group_list.insert(1, '18')
        self.hole_group_list.insert(2, 'Any')
  
        #Go Button
        self.find_tee_times_button = tk.Button(self.root, text='Find Tee Times!', command=self.submit_selections, font=label_font, bg='lime green')
        self.find_tee_times_button.grid(column=0, columnspan=2, row=2, sticky=NSEW, padx=10,pady=10)

   
    def selected_items(self, listbox):
        selected_items = [listbox.get(i) for i in listbox.curselection()]
        return selected_items
              
         
    def submit_selections(self):
        # This is where you get the values from the variables and pass them to your backend logic
        zip_code = self.zip_code_var.get()
        range_value = self.range_var.get()
        early_time = self.early_time_var.get()
        late_time = self.late_time_var.get()
        min_temp = self.min_temp_var.get()
        max_temp = self.max_temp_var.get()
        conditions_blacklist = self.selected_items(self.blacklist_list)
        selected_players = self.selected_items(self.player_group_list)
        selected_holes = self.selected_items(self.hole_group_list)
        no_days_to_check = self.no_days_to_check_var.get()

        # Now, you can use these variables in your backend logic to perform further actions.
        # For now, I'm just printing them as an example.
        print("Zip Code:", zip_code)
        print("Range:", range_value)
        print("Early Time:", early_time)
        print("Late Time:", late_time)
        print("Min Temp:", min_temp)
        print("Max Temp:", max_temp)
        print("Conditions Blacklist:", conditions_blacklist)
        print("Selected Players:", selected_players) 
        print("Selected Holes:", selected_holes)
        print('Days', no_days_to_check)


        day_data_list = main(zip_code, range_value, early_time, late_time,min_temp, max_temp, conditions_blacklist, selected_players, selected_holes, no_days_to_check)

        # Create a new window to display the information
       

        self.result_window = tk.Toplevel(self.root)
        self.result_window.title("Results")

        self.window_frame = tk.Frame(self.result_window)
        self.window_frame.pack()


        top_label_font = ('Arial', 12, 'bold')
        day_summary_font = ('Arial', 8, 'bold')

        self.top_text_label = tk.Label(self.window_frame, text=f"Matches found for courses within a {range_value} radius of {zip_code}", font=top_label_font)
        self.top_text_label.grid(column=0, columnspan=2, row=0)

        self.second_text_label = tk.Label(self.window_frame, text=f"# of golfers: {selected_players[0]} | # of holes: {selected_holes[0]}", font=top_label_font)
        self.second_text_label.grid(column=0, row=1, columnspan=2)

        day_frame_row_index = 2
        count = 0
        for day in day_data_list:
            
            if count % 2 == 0:
                day_frame_col_index = 0
            else:
                day_frame_col_index = 1
            row_index = 0

            self.day_frame = tk.Frame(self.window_frame)
            self.day_frame.grid(column=day_frame_col_index, row=day_frame_row_index, pady=10,padx=10)
           
            day_summary_text = f"{day['day']} | {day['low_temp']}°F - {day['high_temp']}°F | {day['condition']}"
            self.new_day_label = tk.Label(self.day_frame, text=day_summary_text, font=day_summary_font)
            self.new_day_label.grid(column=0, columnspan=2, row=row_index)
            row_index = row_index + 1

            self.no_matches_label = tk.Label(self.day_frame, text=f"{len(day['tee_time_info'])} matches found")
            self.no_matches_label.grid(column=0, columnspan=2, row=row_index)
            row_index = row_index + 1

            self.button_frame = tk.Frame(self.day_frame)
            self.button_frame.grid(column=0, row=row_index)

            self.view_courses_button = tk.Button(self.button_frame, text='View Course List', command=lambda day=day: self.show_courses(day), bg='lime green')
            self.view_courses_button.grid(column=0, row=0, padx=5)

            self.open_url_button = tk.Button(self.button_frame, text="Book Tee Time", command=lambda url=day['url']: webbrowser.open_new(url), bg='lime green')
            self.open_url_button.grid(column=1, row=0)

            if count % 2 != 0:
                day_frame_row_index = day_frame_row_index + 1
            count = count + 1

            

           
            


    def show_courses(self, day):
        self.course_result_window = tk.Toplevel(self.result_window)
        for course in day['tee_time_info']:
            self.new_course_label = tk.Label(self.course_result_window, text=course)
            self.new_course_label.pack()
        


    def run(self):
        self.root.mainloop()

# Create an instance of GolfApp and run the GUI
golf_app = GolfApp()
golf_app.run()
