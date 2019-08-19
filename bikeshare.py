import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello there! Let\'s explore some US bikeshare data! This guided program will give you data from bikeshares in the 1st semester of 2017, around 3 major US cities!\n')
    time.sleep(7)
    print('Please choose the city, month and day parameters for your analysis.')
    time.sleep(3)
    print('\n'"First, input either 'Chicago', 'New York City' or 'Washington'."'\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("name of the city to analize: ")).title()
    available_cities = ["Chicago", "New York City", "Washington"]
    
    while True:
        if city not in available_cities:
            print("\n""wrong city input! Please choose a valid city name.""\n")
            city = str(input("name of the city to analize: ")).title()
        else:
            break
    time.sleep(1)    
    # TO DO: get user input for month (all, january, february, ... , june)
    print('\n'"Great! Now, you need to choose the month between 'january' to 'june', or input 'all' to dismiss the month filter."'\n')
    
    month = str(input("name of the month to analize: ")).title()
    available_months = ["All", "January", "February", "March", "April", "May", "June"]  
    
    while True:
        if month not in available_months:
            print("\n""wrong month input! Please choose a valid month name between January to June, or select 'all' to reference to all months.""\n")
            month = str(input("name of the month to analize: ")).title()
        else:
            break
    
    time.sleep(1)       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\n'"Nice! Now, you need to choose the day of the week, or input 'all' to include all days."'\n')
    day = str(input("day of the week to analize: ")).title()
    available_days = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  
    
    while True:
        if day not in available_days:
            print("\n""wrong day input! Please choose a valid day name or select 'all' to reference to all days of the week.""\n")
            day = str(input("day of the week to analize: ")).title()
        else:
            break
    time.sleep(1)
    print('\n''Good! all inputs were done correctly! Loading data...''\n')
    print('-'*80)
    return city, month, day
    time.sleep(4)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # will convert the 'Start Time' column, currently with string values, to datetime, enabling us to access the month and day of the week:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
        
    # will create a new 'month' column in df, using the dt.month function:
    df['month'] = df['Start Time'].dt.month
    
    # will create a new 'day_of_week' column in df, using the dt.weekday_name function:
    df['day_of_week'] = df['Start Time'].dt.weekday_name
        
    # in case of a month input, this condition will attribute an index for each month from 1 to 6 consecutively:
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # Will use the applied 'month' filter to create a new month-filtered df
        df = df[df['month'] == month]
        
        # Will use the applied 'month' filter to create a new day-filtered df
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    time.sleep(3)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()
    
    time.sleep(4)
    # TO DO: display the most common month
    # Will display the most common month, based on the 'dt.month' and 'mode' functions applied to the datetime column:
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['Start Time'].dt.month.mode())
    most_common_month = months[index - 1]
    
    print('The most common month for bike travelling is {}'.format(most_common_month))
    print("(PS: if any particular month input was made, the result will be equal)")
    
    time.sleep(6)
    # TO DO: display the most common day of week
    # Will display the most common day, based on the 'dt.dayofweek' and 'mode' functions applied to the datetime column:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df['Start Time'].dt.dayofweek.mode())
    most_common_day = days[index]
    print('\n''The most common day of the week for bike travelling is {}.'.format(most_common_day))
    print("(PS: if any particular day of the week input was made, the result will be equal)")
    
    time.sleep(6)
    # TO DO: display the most common start hour
    # Will display the most common start hour, based on the 'dt.hour' and 'mode' functions applied to the datetime column:
    most_common_hour = int(df['Start Time'].dt.hour.mode())
    if most_common_hour == 0:
        convert_ampm = 12
        am_pm = "AM"
    elif 1 <= most_common_hour < 12:
        convert_ampm = most_common_hour
        ampm_define = "AM"
    elif 12 <= most_common_hour <= 23:
        convert_ampm = most_common_hour - 12
        ampm_define = "PM"
        
    print("\nThe most common hour for bike travelling is at {} {}.".format(convert_ampm, ampm_define))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    
    time.sleep(5)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip info...\n')
    
    
    start_time = time.time()
    
    time.sleep(4)
    # TO DO: display most commonly used start station
    # Will display the most common start station, based on the 'mode' function applied to 'Start Station', followed by a 'to_string' function to provide a console-friendly tabular output:
    most_common_startstation = str(df['Start Station'].mode().to_string(index = False))
    print("The most commonly used start station is the {}".format(most_common_startstation))
    
    time.sleep(5)
    # TO DO: display most commonly used end station
    # Will display the most common start station, based on the 'mode' function applied to 'End Station', followed by a 'to_string' function to provide a console-friendly tabular output:
    most_common_endstation = str(df['End Station'].mode().to_string(index = False))
    print("\nThe most commonly used end station is the {}".format(most_common_endstation))
    
    time.sleep(5)
    # TO DO: display most frequent combination of start station and end station trip
    # Will display the most common start-end station combination, based on the concatenated value of both, the 'mode' function applied to said concatenation, followed by a 'to_string' function to provide a console-friendly tabular output:
    most_freq_stationcombo = (df['Start Station'] + " with " + df['End Station']).mode().to_string(index = False)
    print("\nStart-to-end most frequent combination:")
    print("{}".format(most_freq_stationcombo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

    time.sleep(6)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    time.sleep(4)
    # TO DO: display total travel time
    # Will convert the sum from "Trip Duration", expressed in seconds, into hours and days:
    totalhours_travel = int(df['Trip Duration'].sum() / 60 / 60)
    totaldays_travel = int(df['Trip Duration'].sum() / 60 / 60 / 24)
    print("The total trip duration from 2017 is equivalent to {} hours, or {} days!".format(totalhours_travel, totaldays_travel))
    
    time.sleep(5)
    # TO DO: display mean travel time
    # Will discover the average travel time, with the 'mean function, expressed in minutes:
    hours_traveltime_avg = int(df['Trip Duration'].mean() / 60)
    print("\nThe average bike travelling time is approximately {} minutes".format(hours_traveltime_avg))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    time.sleep(5)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nNow, some data concerning our user features!')
    time.sleep(3)
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    time.sleep(4)
    # TO DO: Display counts of user types
    # Will display the count for each of the user types, 'subscribers' and 'customers':
    usertype_count = df['User Type'].value_counts()
    print("the total count of each type of user is:")
    print(usertype_count.to_string())
    
    time.sleep(6)
    # TO DO: Display counts of gender
    # Will display the count for each of the user genders, except from 'washington' wich doesn't contain this info:
    if 'Gender' in df.columns:
        gendertype_count = df['Gender'].value_counts()
        print("\nThe total count of each user gender is:")
        print(gendertype_count.to_string())
        print("PS: result based on users that provided this info")
   
    time.sleep(6)
    # TO DO: Display earliest, most recent, and most common year of birth
    # Will display the oldest birth year, with the 'min' function:    
    if 'Birth Year' in df.columns:
        earliest_birthyear = (df['Birth Year']).min()
        print("\nThe earliest birth year ever registered is {}".format(int(earliest_birthyear)))
    
    time.sleep(5)
    # Will display the most recent birth year, with the 'min' function:    
    if 'Birth Year' in df.columns:
        recent_birthyear = (df['Birth Year']).max()
        print("\nThe most recent birth year ever registered is {}".format(int(recent_birthyear)))
    
    time.sleep(5)
    # Will display the most common birth year, with the 'mode' function:    
    if 'Birth Year' in df.columns:
        common_birthyear = (df['Birth Year']).mode()
        print("\nThe most common birth year is {}".format(int(common_birthyear)))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    time.sleep(5)
    
    # Will verify whether the user desires to see the raw data:    
    i_row = 0
    db_raw_values = ["yes", "no"]
    db_raw = input("\nNow it is your chance to look at the bikeshare database! would you like to see it? (please input 'yes or 'no'):\n").lower()
    
    while True:
        if db_raw not in db_raw_values:
            db_raw = input("\nwrong input! Please input 'yes' or 'no'.\n")
        else:
            break
    while True:
        if db_raw == 'no':
            break
        if db_raw == 'yes':
            print(df[i_row: i_row + 5])
            i_row = i_row + 5
        db_raw = input("\n If want to see 5 more rows, please input 'yes', otherwise input 'no'\n")
    
    print('-'*80)
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # Will provide the suer with the option to restart the program:    
        restart_values = ["yes", "no"]
        
        print('\nThis is all for now! If you wish, you can redo the inputs to result in different outcomes!')
        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n").lower()
        
        while True:
            if restart not in restart_values:
                restart = input("\nwrong input! Please input 'yes' or 'no'.\n")
            else:
                break
        
        if restart != 'yes':
            break
    time.sleep(1)
    print('¨'*80)
    print('¨'*80)
    print('\n===== KEEP CYCLING!!! ==========================================================\n')
    print('¨'*80)
    print('¨'*80)

if __name__ == "__main__":
	main()

# Project submitted to "https://github.com/DanielOnGitHub1/pdsnd_github" repository
