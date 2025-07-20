resource "aws_s3_bucket" "hw-bucket" {
  provider = aws.p1
  bucket   = "ci-cd-pt3-bucket"

  tags = {
    Name = "Homework S3 Bucket"
  }
}

resource "aws_dynamodb_table" "hw-table" {
  provider     = aws.p1
  name         = "ci-cd-pt3-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "name"

  attribute {
    name = "name"
    type = "S"
  }
}

