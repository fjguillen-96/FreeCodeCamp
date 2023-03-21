def time_calculator(time, add, day=None):
    # List of days of the week
    list_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split the input time string into hours and minutes, and extract the meridiem
    time_h, time_m = time.split(':')
    mer = time_m[3:]
    time_h = int(time_h) + 12 if mer == 'PM' else int(time_h)
    time_m = int(time_m[:2])

    # Split the time to add into hours and minutes
    add_h, add_m = add.split(':')

    # Calculate the new minutes and any extra hours
    new_min = time_m + int(add_m)
    extra_h = 1 if new_min >= 60 else 0
    new_min = new_min % 60

    # Calculate the new hours and number of days
    new_h = time_h + int(add_h) + extra_h
    n = new_h // 24 if new_h >= 24 else 0
    new_h = new_h % 24

    # Calculate the new day if applicable
    new_day = list_days[(list_days.index(day.lower().capitalize()) + n) % 8] if day is not None else ''
    
    # Prepare the output string components
    sentence = ['', '']
    if n == 1:
        sentence[1] = f'(next day)'
    elif n > 1:
        sentence[1] = f'({n} days later)'
    sentence[0] = 'PM' if new_h >= 12 else 'AM'
    new_h = new_h % 13
    new_day = ', ' + new_day if day is not None else ''

    # Print the result
    print(f'Returns: {new_h}:{new_min:02d} {sentence[0]}{new_day} {sentence[1]}')
