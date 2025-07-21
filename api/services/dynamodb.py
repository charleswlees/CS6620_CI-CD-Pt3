# Charlie Lees
# CS 6620
# Uses BOTO3 to interface with dynamodb


import boto3

dynamo = boto3.resource(
    "dynamodb",
    region_name='us-east-1',
    aws_access_key_id="test",
    aws_secret_access_key="test",
    #endpoint_url="http://localhost:4566",
    endpoint_url="http://localstack:4566"
)

table = dynamo.Table('ci-cd-pt3-table')

# Healthcheck

def healthcheck():
    try:
        table.load()
        return "healthy"
    except:
        return ""

#######
# GET # 
#######

def get_recipe(name: str):
    recipe = table.get_item(
        Key={'name': name}
    )
    return recipe['Item']

def get_all():
    recipes = table.scan()
    return recipes['Items']


############
# POST/PUT # 
############

#recipe_name='Beans'
##
#recipe = {
#        'name': recipe_name,
#        'steps': [
#            'Put Beans in Pot',
#            'Profit'
#            ]
#        }

def alter_recipe(recipe: dict):
    table.put_item(
        Item=recipe
    )


##########
# DELETE #
##########

def delete_recipe(recipe_name: str):
    recipe = table.delete_item(
                Key={'name': f'{recipe_name}'},
                ReturnValues='ALL_OLD'  
    )
    return recipe



