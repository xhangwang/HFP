def sanitise(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

    
def get_coach_data(filename):
    try:
        with open (filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print ("File Error"+str(ioerr))
        return (None)

"""
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')
"""
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

#append TirmDate in List
james = get_coach_data('james.txt')
for each_t in james:
    clean_james.append(sanitise(each_t))
    """
for each_t in julie:
    clean_julie.append(sanitise(each_t))
for each_t in mikey:
    clean_mikey.append(sanitise(each_t))
for each_t in sarah:
    clean_sarah.append(sanitise(each_t))
"""


#clean_james = sorted([sanitise(t) for t in james])
#clean_julie = sorted([sanitise(t) for t in julie])
#clean_mikey = sorted([sanitise(t) for t in mikey])
#clean_sarah = sorted([sanitise(t) for t in sarah])

print (clean_james[0:3])
"""
unique_james = []
for each_t in clean_james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print (unique_james[0:3])

unique_julie = []
for each_t in clean_julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print (unique_julie[0:3])

unique_mikey = []
for each_t in clean_mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print (unique_mikey[0:3])

unique_sarah = []
for each_t in clean_sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print (unique_sarah[0:3])
"""
        
        



