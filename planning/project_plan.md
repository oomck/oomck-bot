# Oomck Chatbot Project Plan
###### 19th February, 2021
-  For COSC 310
- By Owen Murovec, Opey Adeyemi, Mathew de Vin, Carson Ricca, and Keyvan Khademi

#### Project Description
In this project, we are creating a chatbot that will allow a user to interact with the agent and maintain a conversation about Ubuntu and issues that they may be having. The agent will be able to maintain a conversation with the user for approximately 30 turns. The agent will play the role of a customer support personnel. The user will have the role of a client that is looking for technical help. The repository for our project can be found at https://github.com/oomck/oomck-bot. 

#### SDLC & Rationale
An incremental development lifecycle is proposed for this project. More specifically, agile practices will be employed. An agile approach is preferred by the small and well-knit team of developers, as well as the scope of the work involving rapidly shifting requirements as the team becomes more acquainted with the tasks at hand. The chatbot is a small application with a specific purpose that is suited for agile development. Despite an agile approach being the primary choice, components of integration and configuration will be used. This is due to the prevalence of pre-existing, reliable, and robust systems that accomplish parts of what Oomck Chatbot aims to achieve.

#### SDLC Phases
SCRUM is an iterative development method that focuses on managing iterative development practices. Scrum has three main phases that we will implement in our project.
1. The initial phase is an outline planning phase in which the general objectives are established for the project, and the software architecture is designed.
    1. Creating a Project Plan:
        1. Brief Project Description.
        2. Chosen SDLC and Rationale.
        3. A List of the Phases of the SDLC.
        4. A WBS.
        5. Create a Gantt Chart.
    2. Search for Dataset:
        1. Find Possible Datasets.
        2. Explore Possibility of Dataset for NLP, Pattern Matching, API Implementation.
        3. Determine Dataset(s) to Use.
    3. DevOps Setup:
        1. Set-Up Automated Unit Testing.
        2. Containerize ElasticSearch Using Docker.
        3. Transition Jira TODOs on Successful Merge.
        4. Create Setup Script.

2. The second phase is a series of sprint cycles, each cycle implements an increment of the system.
    1. Create Command Line Interface:
        1. Read Input from Command-Line.
    2. User Input Parsing:
        1. Retrieve User Input.
        2. Create a Dictionary of Useless Words.
        3. Eliminate Useless Words and Return Key Words.
        4. Categorize Key Words.
        5. Fix Extraneous Cases.
    3. Initialize ElasticSearch with Data (Script):
        1. Clone the Data Repo.
        2. Filter Data and Delete Ones that are Not Needed.
        3. Upload Data to ElasticSearch Container.

3. The final phase wraps up the project, required documentation is completed, and lessons learned from the project are assessed.
    1. Finish Project Plan:
        1. Create a List of Limitations of our ChatBot.
        2. Include Sample Output.
    2. Project Presentation:
        1. Create a Video Showcasing the Project’s Strengths and Weaknesses (3-4 Minutes).
        2. Give a Brief Overview of Who Did What (1 Minute).
        3. Show PM Graphs on Github (1 Minute).
        4. Showcase the Jira Project.

#### Project Objectives
To develop a conversational agent capable of retaining dialogue with a user for 30 turns back and forth (a turn is defined as a prompt-response pair). This agent is to have a topic upon which it centers its responses as well as a distinct tone through which it responds.

#### Project Requirements
- Capability to keep a 30 turn dialogue.
    - A turn is defined as a prompt-response pair.
- Focus conversation around the topic of Ubuntu OS.
- Distinctly have the tone of a technical helper.

#### Project Scope
Technology and techniques used in this:
1. Python.
2. Docker.
3. GitHub.
4. ElasticSearch.
5. Jira.
6. Discord.

#### Activity Dependencies

#### Work Breakdown Structure
Current Issues:
- Create a Project Plan - **Carson/Opey.**
- DevOps Setup - **Owen.**
- User Input Parsing - **Mathew**.
- Search for Dataset - **Carson.**
- Create Command Line Interface - **Mathew/Owen.**
- Update README - **Carson/Opey.**
- Initialize ElasticSearch with Data - **Owen/Carson.**
- Class-based code structure - **Keyvan.**
- Overall project structure - **Keyvan.**

#### Overall Schedule

#### Limitations

#### Sample Output



