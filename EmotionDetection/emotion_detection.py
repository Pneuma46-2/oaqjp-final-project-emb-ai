import requests
import json

def emotion_detector(text_to_analyse):
    #string to connect to API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    
    #convert response string to json format
    formatted_response = json.loads(response.text)
    
    #pull dictionary with emotions and values  
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    
    #add dominant emotion
    emotion["dominant_emotion"] = max(emotion, key = emotion.get)
    
    #return dictionary
    return emotion