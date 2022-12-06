# course-project-group-56
Introduction:

Many students struggle to keep themselves accountable for their daily schedule amidst schoolwork, extracurriculars, and other personal commitments. This, combined with students’ reliance on public transportation or walking as a primary means of getting from place to place, makes planning ahead to get to class on time tedious. OnTime provides students a means of planning out their day, including reminders for when to leave and what transportation to take in order to get to their destination on time.


Technical Architecture:

PDFtoDF() - This is the main method which calls other methods (convert_pdf_to_csv(), clean_frame()) to convert the user's schedule as a pdf to a dataframe and cleans it. It takes in the name of the PDF as the parameter and returns a dataframe. Aditya and Neeya wrote this method in Python.

convert_pdf_to_csv() - This method utilized the Tabula library to automatically convert the pdf file into a usable CSV file. It takes in the name of the pdf and returns a CSV. We used this so that it would be easier to work with our users' data. Aditya and Neeya wrote this method in Python.

clean_frame() - This method is the main method used to clean up and remove any unnecessary data. It takes in a CSV and returns a Python dataframe. Additionally, it also calls other methods (get_info(), get_courses(), get_crn()) as well in order to perform this task. We utilized the Pandas library to fix our dataframe. Neeya wrote this method in Python.

get_info() - This method is used to retrieve the unfilitered information from the schedule of the original dataframe. It takes in a CSV and the row number and returns a string from the CSV. Neeya wrote this method in Python.

get_courses() - This method is used to retrieve the course information from the schedule of the original dataframe. It takes in a CSV and the row number and returns a string from the CSV. Neeya wrote this method in Python.

get_crn() - This method is used to retrieve the crn information from the schedule of the original dataframe. It takes in a CSV and the row number and returns a string from the CSV. Neeya wrote this method in Python.

toTimeObject() - This method incorporates the datetime library in order to convert he givent time from standard time to military time. It has a paramenter of a string and  returns a string. Tabeeb wrote this method in Python.

getCurrentTime() - This method retrieves the current time for the user with the datetime library. It takes in no parameters and returns a string. Tabeeb wrote this method in Python.

subtractMin() - This method identifies n minutes before the time given. This will be used to determine 20 minutes before the starting time of the user's class in order to send the notification. It takes in the parameters of a float for the minutes and string for the time and returns the new string. Tabeeb wrote this method in Python.

getDay() - This method retrieves the current day for the user with the datetime library. It takes in no parameters and returns a string. Tabeeb wrote this method in Python.

notifs() - This method uses all the information to construct a text to send as a notification to the user. The parameters for this function is the dataframe, the day, and the current time and returns a string. Ria wrote this method in Python.

Twilio - We used this to send the notification to users. This technology sends notifications through texts. Ria worked on configuring this.

Streamlit - This was utilized to connect the backend to a simple, applicable frontend where the user can upload their schedule and give their phone number. Aditya worked on configuring this.


Installation Instructions:

1) Install homebrew - https://brew.sh/
2) Navigate to your terminal and run "brew install git"
3) Navigate to your terminal and run "brew install python3"
3) Click on the green "Code" button and copy the link
4) Clone the link copied above and open on Visual Studio.
5) Navigate to your terminal and run "pip3 install pandas", "pip3 install tabula", and "pip3 install datetime"
6) Go to the "App.py" file and run the file
7) Follow the instructions that show up on the console


Group Roles:

Aditya - Utilized Streamlit software to connect frontend and backend. Worked with Streamlit library.

Neeya - Constructed scheduling parsing methods from the user's data. Worked with Pandas and Tabula libraries.

Tabeeb - Developed all of the methods to identify dates and times from the user's data. Worked with Datetime library.

Ria - Configured notifications for projects and integrated it with the backend. Worked with Twilio Library.
