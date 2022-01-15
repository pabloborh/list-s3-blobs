provider "aws" {
  region = local.region
}

resource "aws_s3_bucket" "s3_blobs" {
  bucket = local.bucket_name
  acl    = "private"

  tags = {
    Environment = "poc"
  }
}
