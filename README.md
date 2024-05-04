<h1 align="center">DSCI551 Project: Study Yelp</h1>

<h2 align="center">
  Website: <a href="https://dsci551-finalproject-756e6.web.app/home">Cafe Yelp Webapp</a> | 
  Youtube: <a href="https://www.youtube.com/watch?v=jvr61s6kXJ0&ab_channel=AlanTrinh">Video implementation</a>
</h2>

<h2 align="center">Run Commands</h2>

You can download and run the whole code base locally to test it. All interactions with our database are done through CURL commands for the user and the data administrators. Just so you know, you can interact with the web app without needing to run it locally since you can click the above link to access the web/user portion of the program. 

You must download some essential libraries in your terminal before running this project locally.

Download: [Nodejs](https://nodejs.org/en/download/current) & [Python](https://www.python.org/downloads/) 

You can open a terminal with the project files in the directory and run the following commands.

Install Python libraries: 
`pip3 install json` | `pip3 install requests` | `pip3 install sys` | `pip3 install uuid | pip3 install geopy`

Install Node libraries: 
`npm install firebase` | `npm install firebase-tools` `npm install -g @angular/cli` | `npm install axios` | `npm install bootstrap`

To launch the web app locally, open a terminal, cd into /WebApp/hosting/ and do: `ng serve,` then go to http://localhost:4200/home 

<h3 align="center">Webapp Query Instructions</h3>
Our web app queries are limited to what is in our Firebase real-time databases. 

Here are some sample queries you can type in the search bar. 

**Zipcode:** `46184`, `18974`, `33701`

**Business Name:** `IHOP`, `Starbucks`, `Einstein Bros. Bagels` 

<h2 align="center">File Structure</h2>

Our project is split between two programs, one for our users and another for the data administrator. All user interactions are done with our live web app via the above link, and all data administration is done with our Python program, main.py, using the CLI. 

The file structure for our project is as follows:

[./main.py](/main.py) | handles all data administration tasks, open a terminal in the root directory and run the commands listed above each function in `__main__`. 

[./WebApp](/WebApp/) | This directory contains all web app files. It is mainly for viewing since our program is live, and you can interact with it via the link.   
  
Inside the `./WebApp` directory, there are several files that can be ignored, and one directory is called `hosting/.`

To view our web app codebase, navigate to [./WebApp/hosting/src](/WebApp/hosting/src), which contains all the necessary program files: `index.html`, `main.ts`, and styles.css`.

We used Angular for our frontend framework, and all of our website components are stored individually, these files can be viewed in [/src/app](/WebApp/hosting/src/app), Note that we talked about the individual components in dept in our implementation video. 


<h2 align="center">Team Members & Background</h2>

`Meerza Ahmed` - B.S. in Computer Programming & Information Systems from SUNY Farmingdale. I mainly used C++ and Java during my bachelor's and got to work extensively with database systems. I have previously used SQL, firebase, HTML/CSS, JavaScript, and data modeling to build a web application. I have also worked with PostGIS to map spatial data.

`Melissa Perkins` - Undergraduate degree in Cognitive Science from UC Berkeley with some Python, R, and SQL experience during that time. I started the MS program in Applied Data Science in 2021 as a part-time student while working full-time on the HSC campus. I have since gained more experience with Python and various libraries and was also introduced to Java and CSS. As a project for DSCI 554, I created a dashboard using a Javascript framework- Vue.

`Alan Trinh` - I minored in data science from UC Berkeley and have experience in R, SAS, SQL, and Python. I started the MS program in Applied Data Science last fall and have taken DSCI 550. Extensive knowledge in building predictive models, classification models, data analysis, and visualization. I have some experience with Python programming and am looking forward to learning more about full-stack development. I am currently working in product development and have a lot of experience working with software engineers, data scientists, and UI/UX designers.
