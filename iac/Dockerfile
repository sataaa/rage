# Stage 1: Build a base image with all the tools
FROM alpine:3.18 as builder

# Define build arguments for user and group IDs.
# This allows you to match the user on your host machine.
ARG UID=1000
ARG GID=1000

# Install core dependencies: Python for tflocal, curl for downloading Terraform, and other build tools
RUN apk add --no-cache \
  python3 \
  py3-pip \
  curl \
  unzip \
  # Create the non-root user and group
  && addgroup -g ${GID} terraform \
  && adduser -u ${UID} -G terraform -D terraform \
  # Ensure the user has a home directory
  && mkdir -p /home/terraform \
  && chown -R terraform:terraform /home/terraform

# Install tflocal using pip
RUN pip install terraform-local

# Install the AWS CLI (optional, but very useful for debugging)
RUN pip install awscli

# Download and install a specific version of Terraform.
# This ensures consistency across environments.
ARG TERRAFORM_VERSION=1.13.0
RUN curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin \
  && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Stage 2: Create a minimal, final image for running commands
FROM alpine:3.18

# Copy the entire /usr directory from the builder stage to ensure
# all binaries, scripts, and their dependencies are present.
COPY --from=builder /usr /usr
# Also copy the /lib directory for core shared libraries.
COPY --from=builder /lib /lib

# Copy the non-root user from the builder stage
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

# Switch to the non-root user
USER terraform

# Set the working directory for your Terraform files
WORKDIR /usr/src/app

# Set the entrypoint to tflocal
ENTRYPOINT ["tflocal"]

# Define a default command to show help
CMD ["--help"]
