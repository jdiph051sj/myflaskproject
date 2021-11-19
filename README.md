# myflaskproject

# Python Flask CI/CD Pipeline Project..!!
# Using GitHub, AWS Elastic Beanstalk, AWS CodeBuild, AWS CodePipeline
# To deploy a Python Flask Web Application

This repository contains a sample Python Flask web application built using Flask deployed into ElasticBeanstalk environment ..!!

# Prerequisites:-

○ A Github account
○ A sample Python Flask Web Application to be deployed
○ AWS Elastic Beanstalk environment
○ AWS CodeBuild
○ AWS CodePipeline

# Github

Create a code repository containing a sample Python Flask Web Application to trigger a ci/cd pipeline by running below commands:

> git init
> git status
> create new file .gitignore
> git add .
> git commit -m 'init'
> git -c user.name='jdiph051sj' -c user.email='jdiph051@gmail.com' commit -m 'init1'
> git remote add origin https://github.com/jdiph051sj/myflaskproject.git
> git branch -M main
> git push -u origin main


#Python Flask virtual environment

Create virtual environment to deploy the application locally by running below commands:

> python 3 -m venv venv
> sudo apt install python3.8-venv
> . venv/bin/activate
> pip install Flask/pip3 install Flask
> pip3 list
> pip3 install --upgrade pip
> pip3 freeze > requirements.txt
	>> Click
	>> Flask
	>> Jinja2
	>> Pip 
	>> Werkzeug
	
> export FLASK_APP="application.py"
> flask run (which will deploy the app on a local environment running on http://127.0.0.1:5000/


# AWS Elastic Beanstalk

Create and deploy a web application using AWS Elastic Beanstalk environment, which will create the below:

> ec2 instance
> loadbalancer
> auto-scaling

# Built Project

Use AWS CodeBuild to build the source code stored in our GitHub repository

# -> Buildspec File

version: 0.2
phases:
    build:
        commands:
            - npm i --save
artifacts:
    files:
        - '**/*'
	
# Create CI/CD Pipeline by initializing the below:

> pipeline
> source provider: github
> connection to github
> repo name: project name 
> branch name: main

Set up a ci/cd pipeline using AWS CodePipeline to configure a source stage using GitHub repo
Configure a build stage using AWS CodeBuild
Configure a deploy stage using AWS ElasticBeanstalk environment

Then deploy the application hosted on GitHub to ElasticBeanstalk through a pipeline which will allows developers to release software more quickly by automating the build, test and deploy processes.

# Instructions to execute and test the solution..!!

1. Navigate to the Github Repo:-

Link: https://github.com/jdiph051sj/myflaskproject/ 

2. open application.py file and edit the code and this can also be achieved using the command line 

3. git add . all to the origin branch

4. commit the code changes 

5. git push -u origin main (CodePipeline will detect the changes using the webhooks and automatically trigger the CodeBuild and deploy changes that were committed)

6. Open deployed web application

http://myflaskproject-env.eba-jbvhzbhh.us-east-1.elasticbeanstalk.com/

5. New changes should be displayed in less than 3min after the code has been pushed and deployed

6. Repeat steps 2 through 3 to see continues integration

##################
