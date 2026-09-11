
# Azure DevOps Application Delivery Lab

End-to-end Azure DevOps application delivery project demonstrating a production-style CI/CD lifecycle.

## Architecture

Developer → GitHub → Azure DevOps → CI → Testing → Security → Artifact → Docker → ACR → Azure Runtime → Monitoring

## Application

A simple Python FastAPI REST API used as the application workload.

### Endpoints

- `GET /` - Application information
- `GET /health` - Application health check

## DevOps Objectives

- Git branching and pull requests
- Azure DevOps YAML pipelines
- Continuous Integration
- Automated testing
- Code quality analysis
- Dependency/security scanning
- Build artifacts
- Docker containerization
- Azure Container Registry
- Continuous Deployment
- Azure application hosting
- Key Vault integration
- Application monitoring
- Production troubleshooting
- Deployment rollback

## Project Structure

```text
azure-devops-app-delivery-lab/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── requirements.txt
└── README.md

##  Project Structure
 
mkdir app
mkdir tests
New-Item app\\\_\_init\_\_.py -ItemType File
New-Item app\\main.py -ItemType File
New-Item tests\\test\_main.py -ItemType File
New-Item requirements.txt -ItemType File
New-Item README.md -ItemType File    




