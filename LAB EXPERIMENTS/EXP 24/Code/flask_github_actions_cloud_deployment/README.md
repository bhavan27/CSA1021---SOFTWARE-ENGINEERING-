# Flask CI/CD with GitHub Actions and Cloud Deployment

A small Flask app tested by GitHub Actions and deployed to Render after tests pass on pushes to `main`.

## Local run
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Visit `http://localhost:5000` and `http://localhost:5000/health`.

## GitHub Actions setup
1. Create a GitHub repository and upload this project.
2. Ensure the default branch is named `main`.
3. In GitHub repository Settings → Secrets and variables → Actions, add:
   - Name: `RENDER_DEPLOY_HOOK`
   - Value: your Render service deploy-hook URL.
4. Commit/push to `main`. Actions checks out code, installs dependencies, runs pytest, then requests a Render deployment only if tests pass.

## Cloud setup (Render)
1. Sign in to Render and create a Web Service from your GitHub repository.
2. Choose Docker as runtime (or let the included `render.yaml` configure it).
3. Deploy the service once to create the service.
4. In Render service settings, find Deploy Hook and copy its URL.
5. Add the URL to GitHub as `RENDER_DEPLOY_HOOK` secret.
6. Push a code change to the `main` branch to trigger the pipeline.
7. Use the Render service URL to verify the deployment and `/health` endpoint.

Do not expose the deploy hook URL in code or screenshots.

## Pipeline
Checkout → Setup Python → Install → Test → Deploy to Render (main branch push only).

The deployment trigger uses a Render deploy hook. The service may also have its own automatic Git deploy setting; for a strict Actions-controlled pipeline, disable automatic deploys in Render after the initial setup.
