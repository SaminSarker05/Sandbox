from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "hello world"

# route paramater
# variable in path name
@app.route("/get-user/<int:user_id>", methods=["GET"])
def get_user(user_id):

  user_data = {
    "user_id": user_id,
    "name": "samin sarker",
    "email": "jk@gmail.com",
  }

  # query parameter; key value pairs added to url 
  # request.args is a dictionary and we use get to get key value
  extra = request.args.get("extra")
  print(extra)

  return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
  print(type(request))
  data = request.get_json() 
  print(data)
  return jsonify("hello world"), 200





if __name__ == "__main__":
  app.run(debug = True)