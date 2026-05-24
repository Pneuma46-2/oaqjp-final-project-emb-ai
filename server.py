''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app 
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emotion_first_five_key = response.keys()[:4]
    emotion_last_key = response.keys()[5]
    emotion_dom_key = reponse.keys()[6]

    emotion_first_five_value = response.values()[:4]
    emotion_last_value = response.values()[5]
    emotion_dom_value = reponse.values()[6]

    print(emotion["dominant_emotion"])
    print ("For the given statement, the system response is {}".format(emotion))

    print(emotion)
    return "For the given statement, the system response is"


@app.route("/")
def render_index_page():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    