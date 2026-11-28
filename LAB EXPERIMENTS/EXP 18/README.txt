EXPERIMENT 18: CI/CD PIPELINE WITH JENKINS FOR A CONTAINERIZED APPLICATION

Aim:
To automate checkout, testing, Docker image building, and image publishing using a Jenkins CI/CD pipeline.

Requirements:
- Jenkins
- Git
- Docker
- Docker Hub account
- Python 3 and pip (on the Jenkins agent)
- Pipeline and Git plugins
- Credentials Binding plugin

Procedure:
1. Create a sample Flask application and Dockerfile.
2. Store the source code and Jenkinsfile in a Git repository.
3. Configure Docker Hub credentials securely in Jenkins.
4. Create a Jenkins Pipeline job connected to the Git repository.
5. Configure the Jenkinsfile as the pipeline script.
6. Run the pipeline.
7. Observe Checkout and dependency installation stages.
8. Run automated tests.
9. Build the Docker image.
10. Push the Docker image to Docker Hub.
11. Verify the pipeline result and the image in Docker Hub.

Pipeline stages:
Checkout → Install Dependencies → Test → Build Docker Image → Push to Docker Hub.

Result:
A Jenkins CI/CD pipeline was configured to automatically test a Flask application, build its Docker image, and publish the image to Docker Hub.
