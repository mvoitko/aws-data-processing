resource "aws_s3_bucket" "bucket" {
  bucket = "mv-${var.service_name}"
  acl    = "private"
}

resource "aws_s3_bucket_notification" "preprocess_notification" {
  bucket = "${aws_s3_bucket.bucket.bucket}"

  lambda_function {
    lambda_function_arn = "${var.apex_function_arns["preprocess"]}:current"
    events = ["s3:ObjectCreated:*"]
    filter_prefix = "${var.filter_prefix_preprocess}"
  }
}

resource "aws_lambda_permission" "preprocess_allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${var.apex_function_names["preprocess"]}:current"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket.arn}"
}

resource "aws_s3_bucket_notification" "process_bucket_notification" {
  bucket = "${aws_s3_bucket.bucket.bucket}"

  lambda_function {
    lambda_function_arn = "${var.apex_function_arns["process"]}:current"
    events = ["s3:ObjectCreated:*"]
    filter_prefix = "${var.filter_prefix_process}"
  }
}

resource "aws_lambda_permission" "process_allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${var.apex_function_names["process"]}:current"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket.arn}"
}

resource "aws_s3_bucket_notification" "partition_bucket_notification" {
  bucket = "${aws_s3_bucket.bucket.bucket}"

  lambda_function {
    lambda_function_arn = "${var.apex_function_arns["process"]}:current"
    events = ["s3:ObjectCreated:*"]
    filter_prefix = "${var.filter_prefix_partition}"
  }
}

resource "aws_lambda_permission" "partition_allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${var.apex_function_names["process"]}:current"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket.arn}"
}
