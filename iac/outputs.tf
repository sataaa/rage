output "api_gateway_invoke_url" {
  description = "The invocation URL for the API Gateway's dev stage"
  value       = "${aws_api_gateway_stage.dev_stage.invoke_url}/chat"
}