terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

resource "aws_api_gateway_rest_api" "rage_api" {
  name        = "RAGE-API"
  description = "The main API Gateway for the RAGE project"

  body = templatefile("${path.module}/api-definitions/rage-ai.yaml.tftpl", {
    backend_uri = "http://rage-ai:8000"
  })
}

resource "aws_api_gateway_deployment" "api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.rage_api.id

  triggers = {
    redeployment = sha1(templatefile("${path.module}/api-definitions/rage-ai.yaml.tftpl", {
      backend_uri = "http://rage-ai:8000"
    }))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "dev_stage" {
  deployment_id = aws_api_gateway_deployment.api_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.rage_api.id
  stage_name    = "dev"
}