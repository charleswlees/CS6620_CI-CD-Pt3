import boto3
import json

s3 = boto3.resource(
    "s3",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    #endpoint_url="http://localhost:4566",
    endpoint_url="http://host.docker.internal:4566"
)

bucket = s3.Bucket('ci-cd-pt3-bucket')

#response = s3.list_buckets()
#print(response)

def healthcheck():
    try:
        bucket.load()
        return "healthy"
    except:
        return ""


#######
# GET # 
#######

def get_recipe(name: str):
    recipe_obj = bucket.Object(f'data/{name}.json')
    recipe = recipe_obj.get()['Body'].read().decode('utf-8')
    return recipe

def get_all():
    return bucket.objects.all 

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
#

def alter_recipe(recipe: dict):
    recipe_json = json.dumps(recipe,indent=4)
    bucket.put_object(
        Key=f'data/{recipe["name"]}.json',
        Body=recipe_json,
        ContentType='application/json'
    )

##########
# DELETE #
##########

def delete_recipe(recipe_name: str):
    recipe_obj = bucket.Object(f'data/{recipe_name}.json')
    recipe_obj.delete()



