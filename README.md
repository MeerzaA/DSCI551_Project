<h1 align="center">DSCI 551 Course Project, Spring 2024</h1>

<h2 align="center">Website link: <a href="https://dsci551-finalproject-756e6.web.app">https://dsci551-finalproject-756e6.web.app</a></h2>

<h2 align="center">File Structure</h2>

Our project is split between two programs, one for our users and another one for the data administrator. All user interactions are done with our live web app via the above link, and all data administration is done with our Python program called main.py using the CLI. 

The file structure for our project is as follows:

[./main.py](/main.py) is located in the root directory, and is used for the data administration portion of our program.

All web app files are in the [./Webap](./Webapp) directory, this is mainly for viewing since our program is live and you can interact with it via the link.   

Inside the ./Webapp directory, there are several files with one directory called hosting.
You want to navigate to [./Webapp/hosting/src](./Webapp/hosting/src) which contains all the necessary program files.

We used Angular for our frontend framework, which means all of our website components are stored individually, these files can be inspected in [src/assets](./Webapp/hosting/src/assets). 


<h2 align="center">Run Commands</h2>
believe the project requirements are to build a web application that users can visit to interact with a data source. The web app should ideally have a distributed database, with a minimum of two tables, and two UI interfaces. The first one should be front-end heavy and be designed to display our dataset in a meaningful way so that users can interact with it, the other UI should be reserved for data manipulation by a data manager; this one can be a CLI. It is also important to note that the data manag

<h2 align="center">Team Members & Background</h2>

**Meerza Ahmed** - B.S. in Computer Programming & Information Systems from SUNY Farmingdale. I mainly used C++, and Java during my bachelor's, and got to work extensively with database systems. I have previously used SQL, firebase, HTML/CSS, JavaScript, and data modeling to build a web application. I have also worked with PostGIS, to map spatial data.

**Melissa Perkins** - Undergraduate degree in Cognitive Science from UC Berkeley with some Python, R and SQL experience during that time. I started the MS program in Applied Data Science in 2021 as a part-time student while working full-time on the HSC campus. I have since gained more experience with Python and various libraries, I was also introduced to Java and CSS. As a project for DSCI 554, I created a dashboard using a Javascript framework- Vue.

**Alan Trinh** - Minored in Data Science from UC Berkeley with experience in R, SAS, SQL, and Python. I started the MS program in Applied Data Science last fall and have taken DSCI 550. Extensive knowledge in building predictive models, classification models, data analysis, and visualization. Have some experience with Python programming and am looking forward to learning more about full-stack development. Currently working in product development and have lots of experience working with software engineers, data scientists, and UI/UX designers.
