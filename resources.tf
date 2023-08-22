provider "aws" {
	region="ap-south-1"
	 shared_credentials_files = ["/home/surya/.aws/credentials"]
	
}
data "aws_iam_policy_document" "assume_role" {
	statement { 
		effect = "Allow"
		principals {
			type = "Service"
			identifiers = ["lambda.amazonaws.com"]
		}
		
		actions = ["sts:AssumeRole"]
	}
}
resource "aws_iam_role" "iam_for_water_notification_lambda" {
	name = "iam_for_lambda"
	assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role" "iam_for_consumer_registration_lambda" {
	name = "iam_for_consumer_registration_lambda"
	assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
resource "aws_iam_policy" "function_logging_policy" {
	name = "function-logging-policy"
	policy = jsonencode({
		"Version": "2012-10-17"
		"Statement": [
		{
			Action: ["logs:*"],
			Effect: "Allow",
			Resource: "arn:aws:logs:*:*"
		}
	]
})
}

resource "aws_iam_role_policy_attachment" "function_logging_policy_attachment" {
	role=aws_iam_role.iam_for_water_notification_lambda.id
	policy_arn = aws_iam_policy.function_logging_policy.arn
}

resource "aws_iam_role_policy_attachment" "consumer_registration_logging_policy_attachment" {
	role = aws_iam_role.iam_for_consumer_registration_lambda.id
	policy_arn = aws_iam_policy.function_logging_policy.arn
}


data "archive_file" "water_notification_lambda" {
	type = "zip"
	source_dir = "./water_notification_lambda"
	output_path = "water_notification_lambda_payload.zip"
}

data "archive_file" "consumer_registration_lambda" {
	type = "zip"
	source_dir = "./consumer_registration_lambda"
	output_path = "consumer_registration_lambda_payload.zip"

}



resource "aws_lambda_function" "notification_lambda" {
	filename =  "water_notification_lambda_payload.zip"
	function_name = "water_notification_lambda"
	role = aws_iam_role.iam_for_water_notification_lambda.arn
	handler = "index.handler"
	source_code_hash = data.archive_file.water_notification_lambda.output_base64sha256
	runtime = "python3.11"
	timeout = 15
	
}

resource "aws_lambda_function" "consumer_registration_lambda" {
	filename = "consumer_registration_lambda_payload.zip"
	function_name = "consumer_registration_lambda"
	role = aws_iam_role.iam_for_consumer_registration_lambda.arn
	handler = "index.handler"
	source_code_hash = data.archive_file.consumer_registration_lambda.output_base64sha256
	runtime = "python3.11"
	timeout = "15"
}

