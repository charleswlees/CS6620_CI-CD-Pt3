from services import s3, dynamodb

def healthcheck():
    try:
        dbhc = dynamodb.healthcheck()
        s3hc = s3.healthcheck()
        if(dbhc=="healthy" and s3hc =="healthy"):
            return "healthy"
        else:
            return ""
    except:
        return ""


# Returns output from GET using the DynanoDB results
def get_recipe(name):
    try:
        s3.get_recipe(name)
        output = dynamodb.get_recipe(name)
        return output
    except:
        return ""

def get_all_recipes():
    s3.get_all()
    output = dynamodb.get_all()
    return output

def add_recipe(recipe):

    if(len(get_recipe(recipe["name"]))>0):
        return ""
    try:
        s3.alter_recipe(recipe)
        dynamodb.alter_recipe(recipe)
        return get_recipe(recipe["name"])
    except:
        return ""

def change_recipe(recipe):

    if(len(get_recipe(recipe["name"]))==0):
        return ""

    try:
        s3.alter_recipe(recipe)
        dynamodb.alter_recipe(recipe)
        return get_recipe(recipe["name"])
    except:
        return ""

# Deletes given recipe, no return
def delete_recipe(name):
    try:
        s3.delete_recipe(name)
        output = dynamodb.delete_recipe(name)
        return output
    except:
        return ""
