import os
os.getcwd()
print(os.getcwd())
M = []
H = []
try:
    data = open('1.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == "m":
                M.append(line_spoken)
            elif role == "h":
                H.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("The txt is missing!")
  
try:
    m_file = open('m_data.txt','w')
    h_file = open('h_data.txt','w')
    print (M,file == m_file)
    print (H,file == h_file)
    m_file.close()
    h_file.close()
except IOError:
    print("file Error")




