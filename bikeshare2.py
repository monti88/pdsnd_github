import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Write a city name: chicago, new york city or washington!\n").lower()
        if city not in CITY_DATA:
            print("Please choose one of the above correct city names")

        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month from january to june, or type "all" to display all months:\n ').lower()
        months = ['january','february','march','april','may','june']
        if month != 'all' and month not in months:
            print('Please enter a correct month name')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day of the week, or type "all" to display all days:\n ').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and day not in days:
            print('Please enter the correct day name')
        else:
            break

    print('-'*40)
    return city, month, day

    # the load data definition helps collect user daata from the csv files that were given

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
    #load data fine into data frame
    df = pd.read_csv(CITY_DATA[city])

    #convert start time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #exrtract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

     #filter by day of the week
    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df

    #the time stats were the most difficult to create i am not sure it is all correct

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month =='None':
        pop_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June']
        pop_month= months[pop_month-1]
        print("The most Popular month is",pop_month)


    # display the most common day of week
    if day =='None':
        pop_day= df['day_of_week'].mode()[0]
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        print("The most Popular day is".format(pop_day))


    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    pop_hour=df['Start Hour'].mode()[0]
    print("The popular Start Hour is {}:00 hrs".format(pop_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nFinding out the most Popular stations and the trips with most people...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used Start Station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most commonly used End Station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most frequent combination of Start and End Stations:', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_time, ' seconds, or ', total_time/3600, ' hours')

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time:', avg_time, ' seconds, or ', avg_time/3600, ' hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # washington csv has the most missing columns in the database

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # washington has no gender coloumn
    if 'Gender' in df:
        print('\n Counts of Gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    # Washington has no birth year the statements below avoid errors
    if 'Birth Year' in df:
        early_byear = int(df['Birth Year'].min())
        print('\n Earliest Year of Birth:\n', early_byear)
        rec_byear = int(df['Birth Year'].max())
        print('\n Most Reecent Year of Birth:\n', rec_byear)
        common_byear = int(df['Birth Year'].mode()[0])
        print('\n Most Common Year of Birth:\n', common_byear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:
        response=['yes','no']
        choice= input("Would you like to view individual trip data (7 entries)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice=='yes':
                start=0
                end=7
                data = df.iloc[start:end,:7]
                print(data)
            break
        else:
            print("Please enter a valid response")
    if  choice=='yes':
            while True:
                choice_2= input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
                if choice_2 in response:
                    if choice_2=='yes':
                        start+=7
                        end+=7
                        data = df.iloc[start:end,:7]
                        print(data)
                    else:
                        break
                else:
                    print("Please enter a valid response")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
# this is my edit for documentation changes made on bikeshare2.py
