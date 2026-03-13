\# Flask Docker CI/CD Deployment on AWS



\## Project Overview



This project demonstrates how to deploy a simple Flask web application using a modern DevOps pipeline.



The application is containerized using Docker and automatically built and deployed to AWS using GitHub Actions CI/CD.



\## Architecture



Flask App

&nbsp;  ↓

Docker Container

&nbsp;  ↓

GitHub Repository

&nbsp;  ↓

GitHub Actions CI/CD

&nbsp;  ↓

Amazon ECR

&nbsp;  ↓

AWS App Runner

&nbsp;  ↓

Public Web Application



\## Technologies Used



\- Python

\- Flask

\- Docker

\- GitHub Actions

\- AWS ECR

\- AWS App Runner



\## Project Structure



flask-docker-app

│

├── app.py

├── requirements.txt

├── Dockerfile

├── README.md

│

└── .github

&nbsp;   └── workflows

&nbsp;       └── deploy.yml



\## Flask Application



A simple Flask web application that returns a greeting message.



Example output:



Hello! This is my simple web app.



\## Run the Application Locally



\### Build Docker Image



docker build -t flask-app .



\### Run Container



docker run -p 5000:5000 flask-app



\### Access the Application



Open browser:



http://localhost:5000



\## CI/CD Pipeline



The GitHub Actions pipeline automatically performs the following steps:



1\. Detects code changes in the main branch

2\. Builds the Docker image

3\. Logs into AWS

4\. Pushes the image to Amazon ECR

5\. Triggers deployment in AWS App Runner



\## AWS Services Used



\- Amazon Elastic Container Registry (ECR)

\- AWS App Runner

\- IAM for secure authentication



\## Deployment Flow



Code Push

&nbsp;  ↓

GitHub Actions

&nbsp;  ↓

Docker Build

&nbsp;  ↓

Push Image to ECR

&nbsp;  ↓

App Runner Deployment



\## Author



Shahbaz Shaikh



\## Learning Objectives



This project demonstrates:



\- Containerizing applications using Docker

\- Automating deployments using CI/CD

\- Deploying containers to AWS

\- Integrating GitHub with AWS services



