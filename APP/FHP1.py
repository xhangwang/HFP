import os
os.getcwd()
#print(os.getcwd())
data = open('1.txt')

for each_line in data:
    if not each_line.find(':') == -1:
        (role,line_spoken) = each_line.split(':',1)
        print(role)
        print'said:'
        print(line_spoken)
    else:
        print("test Error")
data.close()




'''
cast = ["wxh","wxb","wxd",["pxm",[1992,"qidong"]]]
for cast_item in cast:
    if isinstance(cast_item,list):
        for cast_item2 in cast_item:
            if isinstance(cast_item2,list):
                for cast_item3 in cast_item2:
                    print(cast_item3)
            else:
                print(cast_item2)
    else:
        print(cast_item)
'''

        
def print_list(the_list,indent=False,level=0):
    for new_list in the_list:
        if isinstance(new_list,list):
                print_list(new_list,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t,end=")
                print(new_list)
            else:
                print(new_list)
            
#print_list(cast,True,2)