provider "aws" {
  alias                       = "p1"
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true
  endpoints {
    dynamodb = "http://localstack:4566"
    s3       = "http://localstack:4566"
  }
}

