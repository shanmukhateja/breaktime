def format_time(seconds):
    print(seconds, seconds <= 60, seconds <= 60*60, seconds <= 60*60*60)
    if seconds <= 60:
        return str(seconds) + ' seconds'                # seconds
    elif seconds >= 60*60 and seconds <= 60*60*60:
        return str(seconds / 60) + ' hour(s)'           # hours
    elif seconds >= 60*60*60:
        return str(seconds / (60*60*60)) + ' day(s)'    # days