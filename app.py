from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    import requests, json

    headers = {'Authorization': 'Key f2f339a3cc374420a221fa27e58a3202'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}


    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    parsed_content = json.loads(response.content)
    ob = parsed_content['name']


    
    

    return render_template('home.html', results=parsed_content)

if __name__ == '__main__':
    app.run(debug=True)