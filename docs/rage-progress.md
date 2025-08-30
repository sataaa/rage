### **Project Summary: RAGE (Retro Achievements Guide Engine)**

**Core Objective:** To build an AI-powered assistant that uses a Retrieval-Augmented Generation (RAG) pipeline to provide hints and identify missable achievements in retro video games. The project is being built using a modern microservices architecture and will be deployed via a professional CI/CD and Infrastructure as Code (IaC) workflow.

**Current Status:** **In Progress.** The local development environment and initial service skeletons have been established. `rage-ai` Python server has been created, `/embeddings` endpoint works with the exposed API through API Gateway.

---

### **Component Breakdown, Status, and Dependencies**

**1. Local Development Environment**
* **Description:** Base setup for the project, including the monorepo structure and local container/cloud tooling.
* **Status:** ✅ **In Progress**
* **Progress:** The monorepo structure is created. The `docker-compose.yaml` file successfully defines and orchestrates the core local services (`localstack`, `terraform`, `rage-bff`, `rage-ai`) on a shared network. The `rage-bff` and `rage-ai` services are successfully communicating via the API Gateway endpoint.
* **Remaining Tasks:** Refine service configurations as new requirements (e.g., databases, new lambdas) are added. Add the Cognito to the localstack configuration.

**2. Python AI Inference Service (Private Backend)**
* **Description:** A specialized FastAPI service responsible for running the LLM and embedding models.
* **Status:** 🟡 **Started**
* **Progress:** The service directory (`services/rage-ai`), a placeholder Python file, and a `Dockerfile` have been created. The service is integrated into `docker-compose`. A placeholder `/chat` endpoint is working. The codebase is structured to follow Clean Architecture principles. The FastAPI wrapper is implemented. The `/embeddings` endpoint has been implemented successfully. 
* **Remaining Tasks:** Implement the FastAPI application logic for the `/chat` endpoints. Integrate `llama-cpp-python` and the sentence-transformer models to provide actual AI functionality. Create unit tests, linting and coverage validations to run before being able to run the service. Create integrated tests to run in CI/CD after deploy.

**3. Java/Spring Boot BFF Service (Public-Facing API)**
* **Description:** A Java 21/Spring Boot 3 service that acts as the secure public entry point (Backend for Frontend).
* **Status:** 🟡 **Started**
* **Progress:** The Gradle project structure (`services/rage-bff`), a placeholder `Application.java`, and a `Dockerfile` have been created. The service is integrated into `docker-compose`. The codebase is structured to follow Clean Architecture principles.
* **Remaining Tasks:** Implement the primary REST controllers. Establish the service-to-service communication with the `rage-ai` service via the internal API Gateway. Integrate OpenAPI (`springdoc-openapi`) documentation. Extract everything from `Application.java` into the correct packages and java files created, implement the service itself. The files are created but are empty. Create unit tests, linting and coverage validations to run before being able to run the service. Create integrated tests to run in CI/CD after deploy.

**4. API Security Layer**
* **Description:** Secures the Java BFF using an AWS API Gateway with a built-in Cognito User Pool Authorizer.
* **Status:** 🟡 **Started**
* **Progress:** Terraform setup for the API Gateway is complete and successfully deploys to LocalStack.
* **Remaining Tasks:** Define the Cognito User Pool in Terraform. Configure the API Gateway in Terraform to use the Cognito Authorizer for the BFF's routes.
* **Dependencies:** `3. Java/Spring Boot BFF Service`.

**5. RAG Data Processing Pipeline (ETL)**
* **Description:** An AWS Step Functions workflow that processes walkthrough text files from S3, chunks them, generates embeddings, and loads them into a vector database.
* **Status:** ⚫ **Not Started**
* **Remaining Tasks:** Add a vector database (e.g., ChromaDB) to `docker-compose`. Write the Lambda functions and the Step Function state machine in Terraform.
* **Dependencies:** `2. Python AI Inference Service` (for its `/embeddings` endpoint).

**6. React Frontend Application**
* **Description:** The user interface with integrated user authentication where users select a game and interact with the AI assistant. 
* **Status:** ⚫ **Not Started**
* **Remaining Tasks:** Create the `rage-front` directory and React project. Integrate the AWS Amplify library to handle the Cognito sign-up/sign-in flow. Implement secure token management. Build UI components and integrate with the public RetroAchievements API and the secure Java BFF.
* **Dependencies:** `4. API Security Layer`.

**7. Infrastructure as Code (IaC) & Kubernetes**
* **Description:** Terraform and Kubernetes manifests defining the cloud infrastructure and application deployments.
* **Status:** ✅ **In Progress**
* **Progress:** The `iac` directory is set up with `main.tf` and `variables.tf`. A containerized Terraform environment is defined in `docker-compose` to automatically apply configurations against LocalStack. The API Gateway configuration for the `rage-bff` service is complete. The swagger for the `rage-ai`'s `/embeddings` and `/chat` are defined and are being configured in the Localstack's API Gateway service.
* **Remaining Tasks:** Add the Cognito User Pool to the Terraform configuration. Define the specific AWS resources (S3, API Gateway, Lambdas, etc.) in Terraform. Create the Kubernetes manifests for each service. Create a different API gateway for the rage-bff, so it can be called independently from the rage-ai gateway, with different security for each endpoint (and so that the `/chat` endpoint can be replicated on both). Use the gateway ID and uris as an output, `rage-ai`'s for the `rage-bff` configuration, and `rage-bff`'s for `rage-front`'s configuration.

**8. CI/CD Pipeline**
* **Description:** A GitHub Actions workflow to automate building, testing, and infrastructure validation.
* **Status:** ⚫ **Not Started**
* **Remaining Tasks:** Create the `.github/workflows/ci.yml` file and define the pipeline jobs.
* **Dependencies:** `7. Infrastructure as Code & Kubernetes` and all application codebases.

**9. Developer Experience & Documentation**
* **Description:** Supporting materials for the project.
* **Status:** 🟡 **Started**
* **Progress:** An initial architecture diagram file (`docs/rage-architecture.drawio`) has been created. This progression readme has been created (`docs/rage-progress.md`).
* **Remaining Tasks:** Flesh out the architecture diagram. Create an Insomnia collection. Write comprehensive documentation in `README.md`. Update the progress document often.