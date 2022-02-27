## Inspiration

When we first arrived at the University, and didn't know anyone, the best way to socialize was in the dorm dining halls. We wanted to reignite the thrill of meeting new people on campus once again. Inspired by this motive, we came together to come up with the idea of Food Buddies, where people can meet new friends and share a meal with them. 

## What it does

After logging in, a user is first greeted by a list of meet-ups going on near them. For each meet-up, the restaurant or bakery is displayed, as well as the time and the number of attendees. All attendee information is kept anonymous. When logging in, the user must login with their Illinois email through Google, establishing security for our users. Users also have the option to create a meet-up and after choosing a restaurant and time, their meet-up will show up for others nearby. When using the app, one will have the option in settings to set their location preferences for their meet-ups homepage. 

## How we built it

To create our project, all members of our team used VSCode to write code. We utilized a git repository to collaborate and organize our workflow. We built the backend using Python and a flask app. Our frontend used Vue and Javascript to create the user interface. Finally, our app was deployed to Heroku cloud computing.

**Backend:** To begin the project, we used the documenu API to gather a list of all restaurants within 25 miles of the Illini Union. The data was stored as a JSON, and afterwards, we iterated through the data and created an instance of a restaurant class for each restaurant. The restaurant class contained an id, name, and address. We used a Meetup class to store information about a meet-up, like the creator's id and the list of attendees. We had functions to interact with each Meetup as well. We utilized a Meetup Cache to store all the meet-ups, and filtered through this cache to find a user's joined meetups and available meetups. We also used different algorithms to sort the meet-ups and calculate distance from the user. 

The flask app used GET requests to retrieve information and data from the backend cache and database, such as latitude/longitude and list of meet-ups. The app used POST requests to change the meet-up list when a new meet-up was created. 

**Frontend:** The frontend utilized Vue to make different pages of the application. Each Vue template, from the components directory, is responsible for a different page. For example, the LoadingScreen page has its own Vue template, as well as the SettingsPage, GoogleLogin, Restricted Access page, CreateMeetup page, and the page for all the Meetups. In each Vue component, we had a template with the code for that component written using various Vue UI components. Each Vue file also has a script to dynamically update the data based on the user interaction.

## Challenges we ran into

We first tried to take on the challenge of creating it as a mobile application. After some difficult hours, our lack of experience with mobile development urged us to create a web-based app instead.

The Google authentication login was also very difficult to implement. With lots of research and trial and error, we eventually learned the ropes of it and were successfully able to include it in our project.

When we first started coming up with ideas, we had a core idea that we were very attached to. After much discussion and contemplation however, we decided to change our idea completely, as we realized our first idea would not solve problems as well as we would have wanted it to. We kept brainstorming and discussing and eventually came to our idea of Food Buddies.

## Accomplishments that we're proud of

An accomplishment that our team prides ourselves in is our idea and innovation process. We came up with many good ideas and had meaningful discussions about them as a team. We continued this collaborative and constructive process to further develop features on our project. 

After our continuous efforts, we are delighted to have a finished working product that aligns with what we envisioned. We are also very proud to each have learned more about various areas of software development.

## What we learned

Each of us deepened our understanding of software engineering. We learned the different parts of full stack development. In the frontend, we learned how to use Vue and Javascript to create the layout of an app. We also learned how to integrate the backend algorithms into the frontend part of the app.

We gained experience with app development through flask/Python and Vue. Additionally, we learned how to use and interact with different APIs. 

As a team, we practiced working with version control systems and using professional software conventions. It was a very fun and helpful experience for all of us to go through the entire process of coming up with an idea, developing it, and finishing it to the end. 

## What's next for Food Buddies

Food Buddies has high hopes for the future. After thorough testing on the UIUC campus, we plan to deploy our product to other busy campuses. We will also keep enhancing the features and quality of our app. In the long term, we want to keep maintaining the app and use feedback from users to keep providing for our user base.