variable "aws_region" {
  description = "The AWS region where resources will be provisioned."
  type        = string
  default     = "us-east-1"  # Update with your desired default region
}

variable "glue_tag" {
  type=string
  default = "Glue:poo"
}
variable "aws_arn" {
  type = list(string)
  #type = list(object({
   # region1=string,
    #name=string
  #}))
  default = []
}

locals {
  resource_tag ={
    "Glue:poo"="ooo"
  }
  
}






