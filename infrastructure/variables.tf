variable "apex_function_arns" { type="map" default={} }
variable "apex_function_names" { type="map" default={} }
variable "aws_region" { default = "eu-west-1" }
variable "filter_prefix_preprocess" { default = "raw/" }
variable "filter_prefix_process" { default = "preprocessed/" }
variable "filter_partition_process" { default = "processed/" }
variable "profile_name" { default = "personal" }
variable "service_name" { default = "processing" }
