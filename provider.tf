terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.26"
    }
  }

  backend "s3" {
    bucket = "mysterio"
    key    = "terraform/states"
    region = "eu-west-1"
  }  
}
 
provider "aws" {
  profile = "default"
  region  = var.aws_region
}