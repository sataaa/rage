FROM alpine:3.18 as builder

# non root user
ARG UID=1000
ARG GID=1000

RUN apk add --no-cache \
  python3 \
  py3-pip \
  curl \
  unzip \
  # Setup the non-root user, group, and home
  && addgroup -g ${GID} terraform \
  && adduser -u ${UID} -G terraform -D terraform \
  && mkdir -p /home/terraform \
  && chown -R terraform:terraform /home/terraform

RUN pip install terraform-local

# for debugging
RUN pip install awscli

ARG TERRAFORM_VERSION=1.13.0
RUN curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
  && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin \
  && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Stage 2: Create a minimal, final image for running commands
FROM alpine:3.18

COPY --from=builder /usr /usr
COPY --from=builder /lib /lib

# Copy the non-root user from the builder stage
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

USER terraform

WORKDIR /usr/src/app
