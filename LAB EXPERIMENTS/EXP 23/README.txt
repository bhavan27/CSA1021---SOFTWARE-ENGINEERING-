EXPERIMENT 23: MULTI-CONTAINER APPLICATION (FRONTEND, BACKEND, DATABASE) ON KUBERNETES WITH SCALING

Aim:
To deploy a multi-tier task application on Kubernetes using separate frontend, backend, and database components, and demonstrate horizontal scaling.

Components:
- Frontend: Nginx static web interface
- Backend: Flask REST API
- Database: PostgreSQL
- Kubernetes Deployments, Services, ConfigMap, Secret, PVC and HPA

Procedure:
1. Build frontend and backend Docker images.
2. Tag images with Docker Hub repository names.
3. Push images to Docker Hub.
4. Update image names in Kubernetes manifests.
5. Apply Secret and ConfigMap.
6. Deploy PostgreSQL with persistent storage and Service.
7. Deploy backend replicas and Service.
8. Deploy frontend replicas and NodePort Service.
9. Verify pods, deployments, services and PVC.
10. Open the frontend and add/complete/delete tasks.
11. Scale backend manually using kubectl scale.
12. Optionally apply HPA after metrics-server is available.
13. Observe replica counts using kubectl get pods and kubectl get hpa.

Result:
The frontend, backend and PostgreSQL database are deployed as separate Kubernetes components. The application is accessible through the frontend Service and backend replicas can be scaled manually or automatically using HPA when metrics are available.
