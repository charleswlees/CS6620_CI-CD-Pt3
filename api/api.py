# Charlie Lees
# CS 6620
# Basic API supporting all basic operations (GET, PUT, POST, and DELETE) on the 
# recipes endpoint


from flask import Flask, request
from db import (
        get_recipe,
        get_all_recipes,
        add_recipe,
        change_recipe,
        delete_recipe,
        healthcheck
)

app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def api_healthcheck():
    try:
        output = healthcheck()
        if len(output) > 0 :
            return "online", 200
        else: return "offline", 400
    except:
        return("Internal Server Error", 500)



@app.route("/recipes", methods=["GET"])
@app.route("/recipes/<recipe_name>", methods=["GET"])
def get_recipes(recipe_name=""):
    try:
        if len(recipe_name) > 0:
            output = get_recipe(recipe_name) 
            if len(output) > 0:
                return output, 200
            else:
                return "Error, Recipe not found", 400
        else:
            output = get_all_recipes()
            print(output)
            return output
    except:
        return("Internal Server Error", 500)


@app.route("/recipes", methods=["POST"])
def new_recipe():
    try:
        output = add_recipe(request.json)
        if len(output) > 0:
            return output, 200
        else:
            return "Error, Recipe already present", 400
    except:
        return("Internal Server Error", 500)



@app.route("/recipes", methods=["PUT"])
def update():
    try:
        output = change_recipe(request.json)
        if len(output) > 0:
            return output, 200
        else:
            return "Error, Recipe not found", 400
    except:
        return("Internal Server Error", 500)



@app.route("/recipes/<recipe_name>", methods=["DELETE"])
def delete(recipe_name):
    try:
        output = delete_recipe(recipe_name)
        if 'Attributes' in output:
            return output, 200
        else:
            return "Error, Recipe not found", 400
    except:
        return("Internal Server Error", 500)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

