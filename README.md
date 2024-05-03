<h1 align="center">DSCI551 Project: Study Yelp</h1>

<h2 align="center">
  Website <a href="https://dsci551-finalproject-756e6.web.app">https://dsci551-finalproject-756e6.web.app</a>
  Youtube <a href="https://www.youtube.com/watch?v=jvr61s6kXJ0&ab_channel=AlanTrinh">https://www.youtube.com/watch?v=jvr61s6kXJ0&ab_channel=AlanTrinh</a>
</h2>

<h2 align="center">Run Commands</h2>

You are able to download the whole code base and run it locally to test it. All interactions with our database are done through CURL commands for both the user and the data administrators. Note that you can interact with the webapp without needing to download the project since you can just click the above link to access the web/user portion of the program. 

Here are some important libraries you need to download in your terminal before running this project locally.

Download: [Nodejs](https://nodejs.org/en/download/current) & [Python](https://www.python.org/downloads/) 

Open a terminal in the directory with the project files, and run the following commands.

Install Python libraries: 
`pip3 install json` | `pip3 install requests` | `pip3 install sys` | `pip3 install uuid | pip3 install geopy`

Install Node libraries: 
`npm install firebase` | `npm install firebase-tools` `npm install -g @angular/cli` | `npm install axios` | `npm install bootstrap`

To launch the web app locally do: `ng serve`, then go to http://localhost:4200/home 

<h2 align="center">File Structure</h2>

Our project is split between two programs, one for our users and another one for the data administrator. All user interactions are done with our live web app via the above link, and all data administration is done with our Python program called main.py using the CLI. 

The file structure for our project is as follows:

[./main.py](/main.py) | handles all data administration tasks, simply open a terminal in the root directory and run the commands listed above each function in `__main__`. 

[./WebApp](/WebApp/) | All web app files are in this directory, this is mainly for viewing since our program is live and you can interact with it via the link.   
  
Inside the `./WebApp` directory, there are several files that can be ignored, and one directory called `hosting/`.

To view our webapp codebase you can navigate to [./WebApp/hosting/src](/WebApp/hosting/src) which contains all the necessary program files, `index.html`, `main.ts`,`styles.css`.

We used Angular for our frontend framework, and all of our website components are stored individually, these files can be viewed in [/src/app](/WebApp/hosting/src/app), Note that we talked about the individual components in dept in our implementation video. 




<h2 align="center">Team Members & Background</h2>

`Meerza Ahmed` - B.S. in Computer Programming & Information Systems from SUNY Farmingdale. I mainly used C++, and Java during my bachelor's, and got to work extensively with database systems. I have previously used SQL, firebase, HTML/CSS, JavaScript, and data modeling to build a web application. I have also worked with PostGIS, to map spatial data.

`Melissa Perkins` - Undergraduate degree in Cognitive Science from UC Berkeley with some Python, R, and SQL experience during that time. I started the MS program in Applied Data Science in 2021 as a part-time student while working full-time on the HSC campus. I have since gained more experience with Python and various libraries, I was also introduced to Java and CSS. As a project for DSCI 554, I created a dashboard using a Javascript framework- Vue.

`Alan Trinh` - Minored in Data Science from UC Berkeley with experience in R, SAS, SQL, and Python. I started the MS program in Applied Data Science last fall and have taken DSCI 550. Extensive knowledge in building predictive models, classification models, data analysis, and visualization. Have some experience with Python programming and am looking forward to learning more about full-stack development. Currently working in product development and have lots of experience working with software engineers, data scientists, and UI/UX designers.
