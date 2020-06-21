# QA DevOps Core Fundamental Project: Quiz Creator


## Contents
1. [Brief](#brief)
2. [My Application](#my-application)
3. [Architecture](#architecture)
4. [Project Tracking](#project-tracking)
5. [Risk Assessment](#risk-assessment)
6. [Testing](#testing)
7. [Front-End Design](#front-end-design)
8. [Future Improvements](#future-improvements)
9. [Acknowledgements](#acknowledgements)
10. [Author](#author)



## Brief
The aim of this project was to create a basic CRUD application (create, read, update delete functionality) with utilisation of the following:
* Project Management
* Python Fundamentals
* Python Testing
* Git
* Basic Linux
* Python Web Development
* Continuous Integration
* Cloud Fundamentals
* Databases

For this project, I also conducted a risk assessment, managed planning with a Trello board and created multiple entity-relationship diagrams.  

## My Application

I have decided to produce a simple 'quiz creator'. My application allows the user to create their own questions and then add them to a quiz - which is essentially a set of questions. The user can also update and delete their questions and quizzes. Initially, I also wanted to let the user answer the questions and give them a score. However, due to time constraints and limited scope of the project I have been unable to do so. 

## Architecture

### Database structure

My entity-relationship diagram has evolved throughout the project. 

As you can see in the first image my initial ERD included only user and question tables. However, I quickly realised that this would not be appropriate for the project.

My next ERD consisted of 'questions' and 'quiz' tables. Although this would have been appropriate for the project, I decided against after a while. If I had implemented this table, the user would only be able to add three questions. Additionally, this kind of database structure turned out to be more challenging to implement than anticipated. 

Finally, I decided to create two parent tables and one child table for many-to-many relationship. Whilst this approach came with its own challenges, I believe it helped me make the application as good as it could be. At the moment, the user can add as many questions to their questions as they want. 

### CI Pipeline

My application is stored in a Virtual Machine instance managed by Google Cloud Platform. I used Python as my source code with Flask as my micro-framework. My continuous integration pipeline allows for quick development-to-deployment cycle. I used git for version control and GitHub as my remote repository. I also used Jenkins as my CI server. Jenkins can clone my GitHub repository and then run my application as a systemd service in the background. I used pytest for unit testing and I utilised some selenium modules for integration testing. Additionally, I used to Trello for project tracking.

## Project Tracking

As previously mentioned, I used a Trello board for project tracking. I created several user stories with features that I would like to include in my application. Then, I separated them into different categories - 'must-have' features (green) and 'could-have' features (yellow). This is because I knew I might not have enough time to implement all features I would like. As such, I decided to prioritise CRUD functionality. 

## Risk Assessment


## Testing

I used pytest to test my code. For this project, I was required to use both unit and integration testing. My test coverage for the backend is currently at 90 per cent. Unfortunately, I have not been able to test every line of code due to strict time constraints, but I believe this coverage should be sufficient for this project. All tests have passed successfully. Despite my efforts, I have not been able to find any major bugs. Nevertheless, whilst running the application I noticed that adding a quiz with the same title results in an integrity error. This constraint does not apply to questions. I did not believe it was a major problem and as such the issue remains unresolved. Given more time, I would attempt to fix this bug. 

## Front-End Design

The front-end of my application is rather simple and uses basic HTML. However, it was important to me to make the application at least somewhat presentable. As such, I changed the background of the application and used different fonts. In addition, I made the navigation bar more noticeable. 

## Future Improvements

There are a number of improvements I would like to make. As I mentioned earlier, my time for this project was very limited and I have not been able to implement all the features in the product backlog. Here is a list of a few improvements I would like to make:
* I would like to make sure that every line of code is tested and that there are no bugs (e.g. integrity error).
* At the moment, users can add questions to their quiz, but they cannot remove them as easily. The only way to remove questions from a quiz is to delete the question. However, this deletes the question from all the other quizzes as well. I do not think it is a major problem, but it is definitely a feature I would like to add.
* I believe that, despite my best efforts, my planning was not always perfect. In future projects, I would like to make sure that I manage my time more effectively. 
* I would like to spend more time working on my front-end design to make the app more appealing, user-friendly and functional. 
* I would like to allow user to run their quiz, answer questions and give them a score based on how many questions they answered correctly. 
* It would be useful to implement a simple filter and allow the user to filer questions and quizzes (e.g. by user, title, difficulty or date)
* I believe users should be able to register and save their quizzes/questions.
* I think it would be useful if users were able to select the difficulty of questions and quizzes. 

Inevitably, there are many other things that could be improved. Nevertheless, I believe that this list outlines the most important improvements.  
## Acknowledgements

I would like to thank my trainers for their guidance and help throughout the project. Without them this project would have never been finished. 

## Author

Produced by Pawel Stypulkowski
pstyp94@gmail.com
