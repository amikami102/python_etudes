# sum_timestamps.py
"""
A script defining `sum_timestamps()` function that returns the sum of all listed timestamps.
Timestamp strings are given in the format MM:SS or "HH:MM:SS.
"""
import re

SECONDS_PER_MINUTE = MINUTES_PER_HOUR = 60
TIME_RE = re.compile('\d+')


def sum_timestamps(timestamps: list[str]) -> str:
    """ Return the timestamp representing the sum of `timestamps`. """
    hours, minutes, seconds = [], [], []
    
    for timestamp in timestamps:
        components = reversed(TIME_RE.findall(timestamp))
        seconds.append(int(next(components)))
        minutes.append(int(next(components)))
        hours.append(int(next(components, 0)))
        
    m, seconds = divmod(sum(seconds), SECONDS_PER_MINUTE)
    h, minutes = divmod(sum(minutes) + m, MINUTES_PER_HOUR)
    
    return f'{h + sum(hours)}:{minutes:02d}:{seconds:02d}' if h or sum(hours) else f'{minutes}:{seconds:02d}'


# base problem
assert sum_timestamps(['5:32', '4:48']) == '10:20'
assert sum_timestamps(['03:10', '01:00']) == '4:10'
assert sum_timestamps(['2:10', '1:59']) == '4:09'

# bonus 1, allow hours in the output timestamp
assert sum_timestamps(['15:32', '45:48']) == '1:01:20'

# bonus 2, accepts timestamps that include the hour
assert sum_timestamps(['6:15:32', '2:45:48']) == '9:01:20'
assert sum_timestamps(['6:35:32', '2:45:48', '40:10']) == '10:01:30'