###time difference calc###

#new 1-d array
lentime = []

#function for user-based input calculation
def user():

    #asks for inp and stores in array
    lentime.append(int(input("Please enter day (1)")))
    lentime.append(int(input("Please enter day (2)")))
    lentime.append(int(input("Please enter hrs (1)")))
    lentime.append(int(input("Please enter hrs (2)")))
    lentime.append(int(input("Please enter mins (1)")))
    lentime.append(int(input("Please enter mins (2)")))
    lentime.append(int(input("Please enter secs (1)")))
    lentime.append(int(input("Please enter nsecs (2)")))
    
    output(lentime)
    
#function for moedal-specific calculations
def moedal():
    
    #moedal data entered into array
    lentime = [13, 14, 4, 6, 38, 5, 18, 48]

    output(lentime)

#function for output
def output(lentime):

    #values for d/h/m/s calculated, -ve input allowed for h/m/s
    timed = abs(((lentime[0]-lentime[1])))
    timeh = ((lentime[2]-lentime[3]))
    timem = ((lentime[4]-lentime[5]))
    times = ((lentime[6]-lentime[7]))
    
    #conversion to secs and output, absolute value taken for time to ensure +ve output
    print("Time is: ",((timed * (24*(60**2)))+ abs(((timeh * (60**2)) + (timem *60) + times))) ," seconds")

###

    
