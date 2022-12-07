"""pdf_reader"""
import pandas as pd
import tabula
from tabula import read_pdf
from datetime import datetime
from datetime import time


def convert_pdf_to_csv(filename): 
        """Converts schedule pdf to a data frame"""
        data_frame = tabula.read_pdf(filename, pages='all')[0]
        tabula.convert_into(filename, "updated_df", output_format="csv", pages='all')
        return data_frame
        
def get_info(dates_times, i):
        """Gets unfiltered info of schedule"""
        return dates_times.at[i + 4 , 'date_time_prof_location']
        
def get_course(dates_times, i):
        """Gets course name"""
        return dates_times.at[i+4, 'course']

def get_crn(dates_times, i):
        """Gets CRN"""
        return dates_times.at[i+4,'id']
        
def clean_frame(dates_times):
        """Reorganizes frame into concise columns"""
        course_info = pd.DataFrame(columns = ['Course', 'CRN', 'Days', 'Time', 'Location'])
        for row in range(len(dates_times)):
                value = get_info(dates_times, row)
                arr = value.split("\r")
                if(len(arr) >= 5):
                        course = get_course(dates_times, row)
                        crn = get_crn(dates_times,row)
                        days = arr[1]
                        time = arr[2]
                        loc = arr[3]
                        if(loc[0:3] == "Urb"):
                                course_info = course_info.append({'Course' : course, 'CRN': crn, 'Days' : arr[1] , 'Time' : time, 'Location' : loc}, ignore_index = True)

        return course_info


def PDFtoDF_clean(filename):
        """Combines all other methods into one """
        unfiltered_frame = convert_pdf_to_csv(filename)[4:-1]
        info = unfiltered_frame.iloc[:,[0,3,4]]
        info = info.rename(columns={'Unnamed: 0':'course', 'mpaign':'id', 'Unnamed: 2':'date_time_prof_location'})
        cleaned = clean_frame(info)
        return cleaned

#from tabeeb: converts standard time to military time
def toTimeObject (inputstr):
    if inputstr[6] == "A":
        x = time(int(inputstr[0:2]), int(inputstr[3:5]), 0)
        return x
    if inputstr[6] == "P":
        t = 12 + int(inputstr[0:2])
        x = time(t, int(inputstr[3:5], 0))
        return x

#from tabeeb: makes a new time 20 min prior(since we are notifying users 20 min prior to the class time)
def subtractMin (min, inputstr):
    #min must be between 0 and 59
    if (min >= 59 or min <= 0):
        return "invalid number of minutes"
    prevmin = int(inputstr[3:5])
    newmin = prevmin - min
    ret = inputstr[0:3] + str(newmin) + inputstr[5:8]
    if newmin < 0:
        newmin = 60 + newmin
        newhr = int(inputstr[0:2]) - 1
        ret = str(newhr) + ":" + str(newmin) + inputstr[5:8]
        if newhr < 10:
            ret = "0" + str(newhr) + ":" + str(newmin) + inputstr[5:8]
    
    return ret

def getCurrentTime():
    x = datetime.now().time()
    return x

def getDay(): 
    dt = datetime.now()
    x = dt.weekday()
    return x

def notifs(schedule, day, curr_time):
    if(day == "0"): day = "Monday"
    if(day == "1"): day = "Tuesday"
    if(day == "2"): day = "Wednesday"
    if(day == "3"): day = "Thursday"
    if(day == "4"): day = "Friday"
    if(day == "5"): day = "Saturday"
    if(day == "6"): day = "Sunday"   
    for i in range(len(schedule)):
        if(day in schedule.at[i, 'Days']):
            start_time = schedule.at[i, 'Time'][0:8]
            prev = subtractMin(20, start_time)
            #checks that the current time is 20 min prior to the 
            if(curr_time == str(toTimeObject(prev))):
                return ("It is " + day + "! You have " + schedule.at[i, 'Course'] + " today at " + schedule.at[i, 'Time'])
                

def main():
    df = PDFtoDF_clean("Test Schedule 2.pdf")
    print(df)
    print(df.at[2, 'Location'])


if __name__ == '__main__':
    main()


message = client.messages \
    .create(
         messaging_service_sid='MG48d415c9a4390e93dc7cee2fa48cd95a	',
         body= message,
         send_at=datetime(2021, 11, 30, 20, 36, 27),
         schedule_type='fixed',
         to=phone_number
     )