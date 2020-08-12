# Learning Github
:pushpin: learning to use Github  
:pushpin: run a basic Python script in Repl.it  
:pushpin: create your own python script and run it  

## Create an Account
- Sign up for free GitHub account using your school email.  (You can always add your personal as a secondary account)

## Instructions
- Copy the GitHub link for this assignment: https://github.com/OmahaCentralCybersecurity/LearningGithub
- In [Repl.it](https://repl.it), click the **New Repl (+)** in the top right corner
- Select **Import from GitHub** and paste the link
- The **.replit** file decides what happens when you click the run button. You may have to use the settings below
  ```
  language = "python3"
  run = "python mydemoapp.py"
  ```
  :rotating_light: If we try to 'save' this back to Github, you'll run into an error because you won't have access to make any changes.  

## Version Control
- An important feature of Git is called version control. Version control keeps a history of changes to the code as well as managing those changes.  You may notice some new words being used.  **branch**, **master**, **fork**, **commit** and **push**

1. The **master** branch usually refers to the repository where the default devlopment branch is located.  
2. A **branch** is a parallel version of a repository. It is contained within the repository, but does not affect the primary or master branch allowing you to work freely without disrupting the "live" version. When you've made the changes you want to make, you can merge your branch back into the master branch to publish your changes.
3. To **fork** a repository is a personal copy of another repository.  You usually do not have access to alter someone else's code, thus forking a repo allows you to make changes without altering the working version.  
4. A **commit**  or "revision", is an individual change to a file (or set of files). When you make a commit to save your work, Git creates a unique ID that allows you to keep record of the specific changes commited along with who made them and when. Commits usually contain a commit message which is a brief description of what changes were made.
5. To **push** means to send your committed changes to a remote repository on GitHub.com. For instance, if you change something locally, you can push those changes so that others may access them.


## Our Workflow
Since we will be using Repl.it, we will be **forking** a repository that I have up on our [OmahaCentralCybersecurity](www.github.com/OmahaCentralCybersecurity) organization.

![Directions to add repl.it from Github](https://www.codewithrepl.it/img/06-importing-from-github.png)

Create a new repl and import this fork of the project instead.  Configure the .replit file again and open the version control tab, as before. Under "what did you change" enter "add .repl file" or a similar message to describe what contributions you're making, and press commit and push.  You'll see the error again and be presented with the option to connect your Repl.it account to GitHub to prove that you authorise Repl.it to make these changes to GitHub on your behalf. You can give Repl.it access to all of your repositories (useful if you want to use this integration a lot), but by default it will only get permission for the specific repository that we're working with.

![Pushing Changes to a Repo](https://www.codewithrepl.it/img/06-version-control-tab.png)

---

## Your instructions & questions
:one: Fork this repo, import to Repl.it, configure the .replit file and then run the program.  
:two: What does this program do?  
:three: If you've never worked in Python, what are some things you notice about python that are different from other common languages like javascript or java? 

## FirstProgram.py
:tophat:s off to Derek Babb for a great python & cybersecurity curriculum. Some of which is used. 

:four: In repl.it create a **new python program** that will ask the user for their name, age and calculate their birth year.  

Please label all of your work. There is an area at the top of the code for the file name, your name, the purpose of the file, and the last revision date. Please update all of this info.
```
#FirstProgram.py
#Name:
#Date:
#Assignment: 
#Purpose: To ask a user for their name, and calculate their birth year based of their age. 
```
- We are going to make a program that that says hello and asks for your name.  
- We have not yet used input, you will need the following code to make it work. Experiment to answer these questions.
  - Do I need a prompt or can I simply get input?
  - How do I use the value the user just gave me?
  - What is the data type of the value the user just gave me?
    - Can it be printed?
    - What happens if it is a number and we try to do math with it?
    - Can I convert data types if this one is not correct for my needs?
- Test this program with various inputs

## Assignment Submission
Once you have completed this assignment, share your code (either a link or embed code) and then turn in via Canvas.  
You can also create a new repository on GitHub with your python script.  (optional)
