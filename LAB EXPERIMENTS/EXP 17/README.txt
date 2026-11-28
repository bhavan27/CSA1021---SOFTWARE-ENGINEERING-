EXPERIMENT 17: FLASK API CONTAINERIZED WITH DOCKER, PUSHED TO DOCKER HUB AND DEPLOYED ON KUBERNETES

Aim:
To containerize a Flask API using Docker, push the image to Docker Hub, and deploy the API on Kubernetes.

Requirements:
- Python 3
- Docker Desktop
- Docker Hub account
- Kubernetes cluster (Docker Desktop Kubernetes or Minikube)
- kubectl

Procedure:
1. Create a Flask API application with REST endpoints.
2. Create requirements.txt to specify Flask dependency.
3. Write a Dockerfile to containerize the Flask application.
4. Build the Docker image using docker build.
5. Run the container locally and test the API endpoints.
6. Log in to Docker Hub using docker login.
7. Tag and push the image to Docker Hub.
8. Configure Kubernetes Deployment and Service YAML files.
9. Apply the YAML files using kubectl.
10. Verify Pods, Deployment, and Service using kubectl commands.
11. Access the deployed API through the Kubernetes Service.

API endpoints:
- / : basic API status
- /api/hello : greeting endpoint
- /api/info : application information

Commands and setup details are provided in Code/deployment_commands.txt.

Result:
The Flask API was containerized using Docker, pushed to Docker Hub, and deployed on Kubernetes using Deployment and Service resources.
