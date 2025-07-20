### Overview

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

### TO-DO

Seems like this is VERY similar to what I did last time, just adding the LocalStack and Docker Compose wrinkle

1. Create a terraform file for the LocalStack infrastructure
    * Not strictly necessary but will be nice when containerizing everything
2. Re-tool implementation to pull from LocalStack/AWS instead of MongoDB
3. Refactor tests from Pt-2 and put them into pytest per his feedback last time
4. Containerize
5. Make Github Workflow for automated testing.
    * Since we have to make a testing container, can just use that.


----------

If not present, create a `.env` file similar to this. 
If deploying, please declare these same environment variables in the workflow.

```sh
# Sets Environment Variables for local development
export TF_VAR_region=us-east-1
export TF_VAR_access_key=test
export TF_VAR_secret_key=test
export TF_VAR_dynamodb_endpoint=http://localhost:4566
export TF_VAR_s3_endpoint=http://localhost:4566

```

Before running any terraform actions make sure to source this: 
Ex.
```sh
source ./.env
terraform plan
```
