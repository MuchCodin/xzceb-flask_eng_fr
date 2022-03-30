import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('g33Q_travKou6zdN7w6q3pUyW1vgmxRqcg3EfDEfikRz')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/16448c74-65e5-4ebf-8bd0-77b09971f1a5')

def english_to_french(english_text):
    #write the code here
    translation = language_translator.translate(text = english_text, model_id = "en-fr").get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    translation = language_translator.translate(text = french_text, model_id = "fr-en").get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
