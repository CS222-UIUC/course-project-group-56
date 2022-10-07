# course-project-group-56
OnTime Project Proposal
Pitch
Many students struggle to keep themselves accountable for their daily schedule amidst schoolwork, extracurriculars, and other personal commitments. This, combined with students’ reliance on public transportation or walking as a primary means of getting from place to place, makes planning ahead to get to class on time tedious. OnTime provides students a means of planning out their day, including reminders for when to leave and what transportation to take in order to get to their destination on time.

Functionality
Users can access the date, location, and time of their classes on one application rather than tediously going through their Illinois account and finding all of the information
Users can pick their preferred mode of transportation to get to their class location
Users will be notified when to leave for their classes based on their location and preferred mode of transportation
Reminders will include location, time, and the name of the class so that users will not need to reference their schedule

Components
 Backend:
We will be focusing on the backend development of our application to ensure that we have a minimal viable product that runs on our local device. We will be coding in Python and utilizing the Google Maps API to gather information on the distance between the user and the location of their class. 
Since a lot of students prefer to use the MTD bus to travel around campus, we will also be using the  MTD API to gather information about the bus schedule and when the student should leave for classes based on which bus they want to take. 
To gather information about the user’s schedule, we have two options. The first option is to allow the user to manually input their schedule. The second option is to use UofI’s student developmental REST API’s in order to retrieve the schedule.
One of the purposes of our functions will be to read the user’s schedule from a pdf and store it. To test this, we will use our own schedules as inputs and check to see if they are being stored correctly. From here, we can also test the notifying portion of our code by seeing if it accurately tells the user when to leave for classes. 

Console Output:
Our minimally viable application will display its notifications through the VSCode terminal. When our code is run, it will notify the user throughout the day on when to leave for their classes, and update those times based on how the user’s location moves.
Sample Output: “Leave for the CIF at 1:45 pm to attend CS 222 lecture in room 1015” (Notifies user at 1:30 pm)


Continuous Integration
For testing, we will be using the PyTest testing framework. This is also how we will check code coverage.
We will lint using Pylint, which follows the PEP 8 style guide for python code.
We will assign partners before each week for pull requests, and whenever someone opens a PR their partner should get back to them the following day. If two PR’s edit the same code in different ways, we will choose the more efficient one. If they are the same efficiency, we will take a vote to choose.



Weekly Planning
Research the Google Maps and Google Calendar API, research different possible ways for Users to input their schedule(find which one would be easiest for us to read) . Configure GitHub branches so that we can work independently, and configure docker to provide a stable work environment.
Research and implement code to read the student’s schedule (read a pdf, import from a website..?), and research developer resources available to us to potentially pull students’ schedules from the UI portal.
Develop code to allow students to manually input their schedule and class locations, and create test cases to test if the information is correctly added.
Develop code to grab students’ schedules from a pdf or website depending on what our team decides is the most feasible method. Create test cases to check if it works. 
Develop the necessary algorithms to calculate reminder times relative to distances between students’ inputted destinations, and take user input on preferred travel methods. 
Continue working on developing the aforementioned algorithms and testing their functionality.
 Create a notification system to remind people to get to classes. Add additional functionality, such as reminders to let you know to plan for food between classes. 
 Test our application with sample student schedules to ensure all aspects of the project work correctly, fix any last-minute bugs.

Potential Risks
We may encounter some issues when we attempt to read a pdf of the user’s schedule. Right now we have looked into having the user download a pdf of their schedule from the UIUC self-service page, but the pdf is not very organized and may be hard to gather data. We anticipate that this setback will only take us a few days to counteract because we have a backup option already in place: having users manually enter their weekly schedule.
We are unsure how to tackle the real-time notification aspect of our console-based app. Since we don’t want our code to be running all day long, we need to find a way to have the user receive notifications periodically throughout the day. This setback could take us a week since we would need to research potential ways of going around that issue and then also implement it afterward. Our back up plan is to use the Google Calendar API to send time notifications.
Since the reminder will be occurring before the person’s class starts, we also don’t know how to accurately notify the user if their location moves within that time frame. Since a user can be further away from their class and then move in a different direction after they are notified we need to figure out a way to have a uniform way of notifying our users. As a back up, we will allow the user to choose a set time to be notified, such as 20 minutes before their class starts.

Teamwork
This project will be split into two parts. The first part will include taking the input of a student’s schedule and retrieving the timings and locations of his/her class. This will be worked on by Aditya and Neeya. The second part will be to use the Google Maps API to send the time it would take for the student to go to class at a certain time. This will be worked on by Ria and Tabeeb. We will use discord to communicate with each other, and create tasks for each group to finish by the end of the week. Additionally, we will meet up twice a week at an organized time to collaborate.
