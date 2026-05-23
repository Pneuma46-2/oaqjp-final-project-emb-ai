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
    emotion = response['emotion'] 
    return "For the given statement, the system response is {} : {}.".format(label.split('_')[1], emotion)


@app.route("/")
def render_index_page():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    