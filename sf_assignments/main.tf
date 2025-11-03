provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_role" "test_role" {
  name = "test_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "glue.amazonaws.com"
        }
        resource=concat(
           # [for arn in var.aws_arn :  "arn:aws:ec2:${arn.region1}:123456789012:${arn.name}"],
            [for arn in var.aws_arn :  "arn:aws:ec2:${arn}:123456789012:a"],
            ["arn:aws:ec2:us-east-1:123456789012:instance"])
      },
    ]
  })

  tags=merge({"gleu:2"="oo2"},local.resource_tag)
}