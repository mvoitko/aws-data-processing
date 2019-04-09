output "BucketName" {
  value = "${aws_s3_bucket.bucket.id}"
}

output "BucketArn" {
  value = "${aws_s3_bucket.bucket.arn}"
}
