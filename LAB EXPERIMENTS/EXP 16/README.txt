EXPERIMENT 16: STATIC WEBSITE CONTAINERIZED AND SERVED WITH DOCKER AND NGINX

Aim:
To containerize a static website using Docker and serve it using the Nginx web server.

Requirements:
- Docker Desktop (or Docker Engine)
- Terminal / PowerShell
- Web browser

Procedure:
1. Create a project folder and add the static website files.
2. Create an index.html file containing the website content.
3. Create a Dockerfile using the official Nginx image.
4. Copy the website files into the Nginx web root directory inside the container.
5. Build the Docker image using the docker build command.
6. Run a container and map host port 8080 to container port 80.
7. Open http://localhost:8080 in a web browser.
8. Verify that the static website is served successfully by Nginx.
9. Stop and remove the container after testing if required.

Commands:
Refer to Code/docker_commands.txt. The complete website and Docker configuration are included in Code/website_project/.

Expected Output:
The sample static website loads in the browser at http://localhost:8080 and is served by an Nginx container.

Result:
A static website was successfully containerized with Docker and served using Nginx.
