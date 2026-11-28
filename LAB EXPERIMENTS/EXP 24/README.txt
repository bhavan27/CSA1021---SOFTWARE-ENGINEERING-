EXPERIMENT 24: CI/CD PIPELINE FOR A FLASK APPLICATION USING GITHUB ACTIONS WITH CLOUD DEPLOYMENT

Aim:
To automate testing and cloud deployment of a Flask application using GitHub Actions.

Requirements:
- Python 3.12
- Git and GitHub account
- Flask, pytest, Gunicorn
- Render account for cloud hosting

Procedure:
1. Create a Flask web application.
2. Add dependencies and Dockerfile.
3. Create pytest test cases.
4. Create a GitHub Actions workflow.
5. Push the source code to GitHub.
6. Configure a Render Web Service for the repository.
7. Create a Render deploy hook.
8. Store the deploy hook as a GitHub Actions repository secret.
9. Push a change to the main branch.
10. Observe the workflow in the GitHub Actions tab.
11. Verify tests pass and deployment stage runs.
12. Open the cloud URL and test the application and health endpoint.

Result:
A CI/CD workflow was configured to automatically test the Flask application and trigger cloud deployment on successful tests after a push to the main branch.
