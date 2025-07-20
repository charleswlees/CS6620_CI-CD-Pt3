import pytest, requests

#URL = "http://localhost:8080/recipes"
URL = "http://localstack:8080/recipes"
#URL="http://host.docker.internal:8080/recipes"

recipe = {
           'name': 'Beans',
           'steps': [
               'Put Beans in Pot',
               'Profit'
               ]
           }
recipe2 = {
           'name': 'Beef Willington',
           'steps': [
               'Sear Beef',
               'Wrap in Pastry'
               'Bake'
               ]
           }

combined = [recipe, recipe2]


# Sending a GET request that finds no results returns the appropriate response
def test_empty_get():
    response = requests.get(f"{URL}/beef")
    assert response.status_code == 400
    assert response.text == "Error, Recipe not found"
    

# Sending a POST request results in the JSON body being stored as an item in the database, and an object in an S3 bucket

def test_post_valid():
    response = requests.post(f"{URL}", json=recipe)
    assert response.json() == recipe
    assert response.status_code == 200


# Sending a duplicate POST request returns the appropriate response

def test_post_duplicate():
    response = requests.post(f"{URL}", json=recipe)
    assert response.text == "Error, Recipe already present"
    assert response.status_code == 400

# Sending a GET request with appropriate parameters returns expected JSON from the database

def test_get():
    response = requests.get(f"{URL}/{recipe['name']}")
    assert response.status_code == 200
    assert response.json() == recipe

# Sending a GET request with no parameters returns the appropriate response
def test_get_all():
    response = requests.post(f"{URL}", json=recipe2)
    response = requests.get(f"{URL}")
    assert response.json() == combined
    assert response.status_code == 200
    requests.delete(f"{URL}/{recipe2['name']}")

# Sending a GET request with incorrect parameters returns the appropriate response
def test_bad_get():
    response = requests.get(f"{URL}/12345")
    assert response.status_code == 400
    assert response.text == "Error, Recipe not found"

# Sending a PUT request that targets an existing resource results in updates to the appropriate item in the database and object in the S3 bucket
def test_put():
    new_recipe = {
               'name': 'Beans',
               'steps': [
                   'Put Beans in Pot',
                   'Stir',
                   'Profit'
                   ]
               }
    response = requests.put(f"{URL}", json=new_recipe)
    assert response.json() == new_recipe
    assert response.status_code == 200
    response = requests.put(f"{URL}", json=recipe)

# Sending a PUT request with no valid target returns the appropriate response

def test_bad_put():
    response = requests.put(f"{URL}", json=recipe2)
    assert response.text == "Error, Recipe not found"
    assert response.status_code == 400

# Sending a DELETE request results in the appropriate item being removed from the database and object being removed from the S3 bucket
def test_delete():
    response = requests.delete(f"{URL}/{recipe['name']}")
    assert response.status_code == 200
    assert response.json()["Attributes"] == recipe

# Sending a DELETE request with no valid target returns the appropriate response
def test_bad_delete():
    response = requests.delete(f"{URL}/{recipe2['name']}")
    assert response.text == "Error, Recipe not found"
    assert response.status_code == 400
