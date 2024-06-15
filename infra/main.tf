terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "ap-south-1"
}

# Create AWS EC2 instance and install grafana and influxdb in it

resource "aws_instance" "monitor" {
  ami = "ami-0f58b397bc5c1f2e8"
  instance_type = "t2.micro"
  user_data = file("user_data.sh")
  security_groups = [aws_security_group.monitoring-sg.name]
  tags = {
    Name = "monitoring"
  }
}

resource "aws_security_group" "monitoring-sg" {
  name = "allow_incoming_traffic"
  tags = {
    Name = "Allow-Incoming-Traffic"
  }

  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8086
    to_port     = 8086
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_kinesis_stream" "health_data_stream" {
    name = "health_data_stream"
    shard_count = "1"
    retention_period = "24"

    shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

    tags = {
    Environment = "test"
  }
}
