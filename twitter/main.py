from flask import Flask, make_response, jsonify
from twitter import Twitter

app = Flask(__name__)
api = Twitter()

@app.route("/")
def index():
	if api.verify():
		return "Twitter Api: Working OK"
	return "Twitter Api: Working BAD"

@app.route('/twitter/user/', methods=['GET'])
@app.route('/twitter/user/<string:username>', methods=['GET'])
def user(username = "Aztrarok"):
	try:
		message = api.get_user(username)
	except:
		return make_response(jsonify({'code': 404, 'message': 'User not found.'}), 404)
	return jsonify(message)

@app.route('/twitter/posts/', methods=['GET'])
@app.route('/twitter/posts/<int:number>', methods=['GET'])
def posts(number = 5):
	if number < 1 or number > 20:
		print("The minimum number of tweets is 5 and the maximum is 20")
		if number < 1:
			number = 5
		else:
			number = 20
	try:
		message = api.get_tweets(number)
	except:
		return make_response(jsonify({'code': 400, 'message': 'User not indicated.'}), 400)
	return jsonify(message)

if __name__== '__main__':
	app.run(debug = True, host='0.0.0.0', port=80)