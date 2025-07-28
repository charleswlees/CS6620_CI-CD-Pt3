## Overview

In the last assignment, you created a REST API with endpoints for GET, POST, PUT, and DELETE verbs, and tests for each endpoint. Make sure the POST and PUT endpoints accept JSON. Add functionality to create, read, update, and destroy items in a DynamoDB table and an S3 bucket. Use Localstack to run a mock of AWS as part of your application stack. Create two compose files and corresponding shell scripts: one will run the stack until manually stopped, the other will run the tests and exit with a zero status if the tests pass and a non-zero status if the tests fail. Put all relevant files into a repository, and enable automatic and manual runs of the tests using a workflow. Include a README along with instructions for running the stack and tests, and share it with the TA.

Tests should cover at least these cases:
- Sending a GET request with appropriate parameters returns expected JSON from the database
- Sending a GET request that finds no results returns the appropriate response
- Sending a GET request with no parameters returns the appropriate response
- Sending a GET request with incorrect parameters returns the appropriate response
- Sending a POST request results in the JSON body being stored as an item in the database, and an object in an S3 bucket
- Sending a duplicate POST request returns the appropriate response
- Sending a PUT request that targets an existing resource results in updates to the appropriate item in the database and object in the S3 bucket
- Sending a PUT request with no valid target returns the appropriate response
- Sending a DELETE request results in the appropriate item being removed from the database and object being removed from the S3 bucket
- Sending a DELETE request with no valid target returns the appropriate response


## Submission
>In the last assignment, you created a REST API with endpoints for GET, POST, PUT, and DELETE verbs, and tests for each endpoint. Make sure the POST and PUT endpoints accept JSON. Add functionality to create, read, update, and destroy items in a DynamoDB table and an S3 bucket.

I have created a new API from scratch to use DynamoDB and S3. This API supports all listed tests in the assignment description. Each endpoint verifies that the s3 and Dynamo table are matching.

>Use Localstack to run a mock of AWS as part of your application stack. 

I am using localstack via docker-compose to simulate DynamoDB and S3.

>Create two compose files and corresponding shell scripts: one will run the stack until manually stopped, the other will run the tests and exit with a zero status if the tests pass and a non-zero status if the tests fail. 

I am using the profile feature of docker-compose to only run my tests with the "test" profile. 
In other words I only need one docker-compose file but I have two scripts: `test.sh` and `start.sh`.
The test script `test.sh` is used in the github workflow as well.

>Put all relevant files into a repository, and enable automatic and manual runs of the tests using a workflow. 

All of my work is hosted on github and my test workflow runs automatically as well as manually.

>Include a README along with instructions for running the stack and tests, and share it with the TA.

This is the README :), this repo is public so there should be no access issues.



## Running my Submission
If you'd like to run my submission to tinker with the api locally please use the `start.sh` script in the root directory.

You can also run the tests manually through Github Workflows or through the `test.sh`.

# External Resources used

For the most part the external resources used were the documentation for the various tools. Otherwise I referenced forum posts which I have also cited in the comments of the code. 
Please see these sources below: 


* boto3 (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* Flask (https://flask.palletsprojects.com/en/stable/)
* Healthchecks for docker-compose (https://github.com/localstack/localstack/issues/1095)
* Pytest (https://docs.pytest.org/en/stable/contents.html)
* Docker Compose (https://docs.docker.com/compose/)
* Using localstack with Terraform (https://docs.localstack.cloud/aws/integrations/infrastructure-as-code/terraform/)
 

