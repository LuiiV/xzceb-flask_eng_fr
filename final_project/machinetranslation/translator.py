import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['APIKEY']
url = os.environ['URL']

def english_to_french(english_text):

    authenticator = IAMAuthenticator(apikey)

    language_translator = LanguageTranslatorV3(
        version = '2023-01-13', 
        authenticator=authenticator
        )

    language_translator.set_service_url(url)

    french_translation = language_translator.translate(
        text = english_text, 
        model_id = 'en-fr')

    dictionary = french_translation.get_result()

    french_text = dictionary['translations'][0]['translation']

    return french_text

def french_to_english(french_text):

    authenticator = IAMAuthenticator(apikey)

    language_translator = LanguageTranslatorV3(
        version = '2023-01-13', 
        authenticator=authenticator
        )

    language_translator.set_service_url(url)

    english_translation = language_translator.translate(
        text = french_text, 
        model_id = 'fr-en')

    dictionary = english_translation.get_result()

    english_text = dictionary['translations'][0]['translation']

    return english_text