import pandas as pd
from datetime import timedelta


# define a function to see if a user logged in on 3 separate days in a 7-day period.
def adopted_user(df, days=7, logins=3):
    """

    :param df: dataframe
    :param days: int, length of period
    :param logins: int, numbers of logins
    :return:
    """
    # first drop duplicate days and sort by day
    df['date'] = df['time_stamp'].dt.date
    df = df.drop_duplicates(subset='date').sort_values('date')

    # calculate how many days has passed for every 3 logins
    passed_days = df['date'].diff(periods=logins-1)

    # check if any passed time is less than 7 days
    return any(passed_days <= timedelta(days=days))
