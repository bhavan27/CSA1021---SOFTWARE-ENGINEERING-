EXPERIMENT 19: CONTINUOUS DEPLOYMENT OF A DOCKERIZED APPLICATION USING GITHUB ACTIONS

Aim:
To automate the building and publishing of a Dockerized application using GitHub Actions, and configure a deployment workflow.

Requirements:
- GitHub account and repository
- Docker
- Docker Hub account
- Flask and Python (for local testing)
- GitHub Actions

Procedure:
1. Create a sample Flask application.
2. Create a Dockerfile to containerize the application.
3. Create a GitHub Actions workflow file in .github/workflows/.
4. Configure Docker Hub credentials as GitHub repository secrets.
5. Push the source code to the main branch.
6. Observe the GitHub Actions workflow execution.
7. Build the Docker image automatically.
8. Push the Docker image to Docker Hub.
9. Verify the image and tag in Docker Hub.
10. (Optional) Configure SSH secrets and deployment commands to deploy the image to a remote server.

Result:
A GitHub Actions workflow was configured to automatically build and publish the Docker image of the application. A deployment step can be enabled for a remote server using securely stored SSH secrets.
