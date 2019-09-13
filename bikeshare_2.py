# log 13/09/2019
# Ali Tassiou Abass

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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York City, or Washington ? \n')
            if city.lower() in ('chicago', 'new york city', 'washington'):
                city = city.lower()
                break
            else:
                print('Please choose between these cities : Chicago, New York City, Washington \n')
        except ValueError:
            print('wrong value \n')
    while True:
        try:
            time = input('Would you like to filter data by month, day, both, or not at all ? Type "none" for no time filter \n')
            if time.lower() == 'both':
                while True:
                    month = input('Which month? January, February, March, April, May, June \n')
                    if month.lower() in ('january', 'february', 'march', 'april', 'may', 'june'):
                        month = month.lower()
                        while True:
                            day = input('Which day? Please between these days : all, Monday, Tuesday, Wednesday, Thursday, Saturday, Sunday \n')
                            if day.lower() in ('all','monday','tuesday','wednesday','thursday','saturday','sunday'):
                                day = day.lower()
                                break
                            else:
                                print('Please choose day like this : 0= all, 1=Sunday,2=monday,3=tuesday,... \n')
                                
                        break
                    else:
                        print('Please choose month between January, February, March, April, May, June \n')
                break
            elif time.lower() == 'month':
                while True:
                    month = input('Which month? January, February, March, April, May, June \n')
                    if month.lower() in ('january', 'february', 'march', 'april', 'may', 'june'):
                        month = month.lower()
                        day = 'all'
                        break
                    else:
                        print('Please choose month between January, February, March, April, May, June \n')			
                break
        except:
            print('error')
    print('-'*40)
    return city, month, day


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

	# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
	
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
	
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
	
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print(most_common_month)

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    most_common_day = df['day'].mode()[0]
    print(most_common_day)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def union(List1,List2):
    List = []
    for word in List1:
        List.append(word)
    for word in List2:
        List.append(word)
    return List

def most_frequent(List):
	word_counter = {}
	for word in List:
		if word not in word_counter:
			word_counter[word] = 1
		else:
			word_counter[word] += 1
	return word_counter[max(word_counter)]

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = most_frequent(df['Start Station'])
    print(most_commonly_used_start_station)

    # display most commonly used end station
    most_commonly_used_start_station = most_frequent(df['End Station']) 
    print(most_commonly_used_start_station)

    # display most frequent combination of start station and end station trip
    most_frequent_combination_start_end_station_trip = most_frequent(union(df['Start Station'],df['End Station']))
    print(most_frequent_combination_start_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    genders = df['Gender'].value_counts()
    print(genders)

    # Display earliest, most recent, and most common year of birth

	#df['year'] = df['Birth Year'].dt.year
	#earliest_year_of_birth = df['year'].mode()[0]
	
	# find the earliest year of birth
    earliest_year_of_birth = df['Birth Year'].max();
    print('Earliest year of birth:', earliest_year_of_birth)
	
	# find the most recent year of birth
    most_recent_year_of_birth = df['Birth Year'].min();
    print('Most recent year of birth:', most_recent_year_of_birth)
	
	#find most common year of birth
    most_common_year_of_birth = df['Birth Year'].mean();
    print('Most common year of birth:', most_common_year_of_birth)
	

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
