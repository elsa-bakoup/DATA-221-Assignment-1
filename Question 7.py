def time_conversion(seconds_input):

    if seconds_input < 0:    #validating the input
        return "Invalid input, seconds need to be positive integers."

    if seconds_input < 12*3600:    #defining the period based on the number of second
        period = "AM"
    else :
        period = "PM"

    hours = (seconds_input//3600) % 24      #expressing the hours on a 24 hours clock
    hours = hours % 12                      #Converting the 24 hours clock to a 12 hours one
    if hours == 0:           #handling the case for midnight and noon
        hours = 12

    minutes = (seconds_input % 3600) // 60
    seconds = seconds_input % 60

    return f"{hours} {minutes} {seconds} {period}"