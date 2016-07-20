import os
os.getcwd()
print(os.getcwd())

def sanitise(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

    
class AthleteList(list):
    def __init__(self,a_name,a_dob = None,a_times=[]):
        list.__init__([ ])
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
        
    def top3(self):
        return (sorted(set([sanitise(t) for t in self.times]))[0:3])
              
def get_coach_data(filename):
    try:
        with open (filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (AthleteList(templ.pop(0),templ.pop(0),templ))    
    except IOError as ioerr:
        print ("File Error"+str(ioerr))
        return (None)


james2 = get_coach_data('D:\GitHub\FHP\HFP\Date\james2.txt')
julie2 = get_coach_data('D:\GitHub\FHP\HFP\Date\julie2.txt')
mikey2 = get_coach_data('D:\GitHub\FHP\HFP\Date\mikey2.txt')
sarah2 = get_coach_data('D:\GitHub\FHP\HFP\Date\sarah2.txt')


print (james2.name + " 's fastest times are:" +str(james2.top3()))
print (julie2.name + " 's fastest times are:" +str(julie2.top3()))
print (mikey2.name + " 's fastest times are:" +str(mikey2.top3()))
print (sarah2.name + " 's fastest times are:" +str(sarah2.top3()))
