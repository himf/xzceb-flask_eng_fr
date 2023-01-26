"""
translator containes functions to translate fron en to fr and from fr to en
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#Load variables from environment
load_dotenv()

# Extract the api key and url from the environment variables
API_KEY = os.environ['APIKEY']
URL = os.environ['URL']

# Initialize the authenticator
authenticator = IAMAuthenticator(API_KEY)

# Initialize the language translator
translator = LanguageTranslatorV3(version='2018-05-01',
                                  authenticator=authenticator)
translator.set_service_url(URL)


def english_to_french(english_text):
	"""
    Translates the given english text to french.

    Args:
    english_text (str): The english text to translate.

    Returns:
    str: The french translation of the english text.
    """
	if english_text == '':
		return ''
	translation = translator.translate(text=english_text,
	                                   source='en',
	                                   target='fr').get_result()
	return translation['translations'][0]['translation']


def french_to_english(french_text):
	"""
    Translates the given french text to english.

    Args:
    french_text (str): The french text to translate.

    Returns:
    str: The english translation of the french text.
    """
	if french_text == '':
		return ''
	translation = translator.translate(text=french_text, source='fr',
	                                   target='en').get_result()
	return translation['translations'][0]['translation']
