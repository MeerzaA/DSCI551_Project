<h1 align="center">DSCI 551 Course Project, Spring 2024</h1>

<h2 align="center">Website link: <a href="https://dsci551-finalproject-756e6.web.app">https://dsci551-finalproject-756e6.web.app</a></h2>

<h2 align="center">File Structure</h2>

Our project is split between two programs, one for our users and another one for the data administrator. All user interactions are done with our live web app via the above link, and all data administration is done with our Python program called main.py using the CLI. 

The file structure for our project is as follows:

[./main.py](/main.py) | handles all data administration tasks, simply open a terminal in the root directory and run the commands listed above each function in `__main__`. 

[./WebApp](/WebApp/) | All web app files are in this directory, this is mainly for viewing since our program is live and you can interact with it via the link.   
  
Inside the `./WebApp` directory, there are several files that can be ignored, and one directory called `hosting/`.

To view our webapp codebase you can navigate to [./WebApp/hosting/src](/WebApp/hosting/src) which contains all the necessary program files, `index.html`, `main.ts`,`styles.css`.

We used Angular for our frontend framework, and all of our website components are stored individually, these files can be viewed in [/src/app](/WebApp/hosting/src/app). 


<h2 align="center">Run Commands</h2>
believe the project requirements are to build a web application that users can visit to interact with a data source. The web app should ideally have a distributed database, with a minimum of two tables, and two UI interfaces. The first one should be front-end heavy and be designed to display our dataset in a meaningful way so that users can interact with it, the other UI should be reserved for data manipulation by a data manager; this one can be a CLI. It is also important to note that the data manager

<h2 align="center">Team Members & Background</h2>

`Meerza Ahmed` - B.S. in Computer Programming & Information Systems from SUNY Farmingdale. I mainly used C++, and Java during my bachelor's, and got to work extensively with database systems. I have previously used SQL, firebase, HTML/CSS, JavaScript, and data modeling to build a web application. I have also worked with PostGIS, to map spatial data.

`Melissa Perkins` - Undergraduate degree in Cognitive Science from UC Berkeley with some Python, R, and SQL experience during that time. I started the MS program in Applied Data Science in 2021 as a part-time student while working full-time on the HSC campus. I have since gained more experience with Python and various libraries, I was also introduced to Java and CSS. As a project for DSCI 554, I created a dashboard using a Javascript framework- Vue.

`Alan Trinh` - Minored in Data Science from UC Berkeley with experience in R, SAS, SQL, and Python. I started the MS program in Applied Data Science last fall and have taken DSCI 550. Extensive knowledge in building predictive models, classification models, data analysis, and visualization. Have some experience with Python programming and am looking forward to learning more about full-stack development. Currently working in product development and have lots of experience working with software engineers, data scientists, and UI/UX designers.
