import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey_lt = os.environ['apikey']
url_lt = os.environ['url']

authenticator_lt = IAMAuthenticator('apikey_lt')
language_translator = LanguageTranslatorV3(
    version = '2023-01-13',
    authenticator = authenticator_lt
)

language_translator.set_service_url(url_lt)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):

    french_text = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()
    dictionary = json.loads(json.dumps(french_text, indent = 2))
    french_text = dictionary["translation"][0].get["translation"]
    return french_text

def french_to_english(french_text):
    english_text = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()
    dictionary = json.loads(json.dumps(english_text, indent= 2))
    english_text = dictionary["translation"][0].get["translation"]
    return english_text