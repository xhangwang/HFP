import athletemodel
import yate
import glob

date_files = glob.glob("data/*txt")
athletes = athletemodel.put_to_store(date_files)

print (yate.start_response())
print (yate.include_header("Coach Keylly's List of Athletes"))
print (yate.start_form("generate_timing_date.py"))
print (yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    print (yate.radio_button("which_athlete",athletes[each_athlete].name))
    
print (yate.end_form("Select"))
print (yate.include_footer({"Home":"/index.html"}))