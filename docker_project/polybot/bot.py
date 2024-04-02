import telebot
from loguru import logger
import os
import time
from telebot.types import InputFile
import telebot 
import boto3
import requests

s3 = boto3.client('s3')
images_bucket = os.environ['BUCKET_NAME']
#yolo5_url = "localhost:8081"
class Bot:

    def __init__(self, token, telegram_chat_url):
        # create a new instance of the TeleBot class.
        # all communication with Telegram servers are done using self.telegram_bot_client
        self.telegram_bot_client = telebot.TeleBot(token)

        # remove any existing webhooks configured in Telegram servers
        self.telegram_bot_client.remove_webhook()
        time.sleep(0.5)

        # set the webhook URL
        self.telegram_bot_client.set_webhook(url=f'{telegram_chat_url}/{token}/', timeout=60)

        logger.info(f'Telegram Bot information\n\n{self.telegram_bot_client.get_me()}')

    def send_text(self, chat_id, text):
        self.telegram_bot_client.send_message(chat_id, text)

    def send_text_with_quote(self, chat_id, text, quoted_msg_id):
        self.telegram_bot_client.send_message(chat_id, text, reply_to_message_id=quoted_msg_id)

    @staticmethod
    def is_current_msg_photo(msg):
        return 'photo' in msg

    def download_user_photo(self, msg):
        """
        Downloads the photos that sent to the Bot to `photos` directory (should be existed)
        :return:
        """
        if not self.is_current_msg_photo(msg):
            raise RuntimeError(f'Message content of type \'photo\' expected')

        file_info = self.telegram_bot_client.get_file(msg['photo'][-1]['file_id'])
        data = self.telegram_bot_client.download_file(file_info.file_path)
        folder_name = file_info.file_path.split('/')[0]

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        with open(file_info.file_path, 'wb') as photo:
            photo.write(data)

        return file_info.file_path

    def send_photo(self, chat_id, img_path):
        if not os.path.exists(img_path):
            raise RuntimeError("Image path doesn't exist")

        self.telegram_bot_client.send_photo(
            chat_id,
            InputFile(img_path)
        )

    def handle_message(self, msg):
        """Bot Main message handler"""
        logger.info(f'Incoming message: {msg}')
        self.send_text(msg['chat']['id'], f'Your original message: {msg["text"]}')


class QuoteBot(Bot):
    def handle_message(self, msg):
        logger.info(f'Incoming message: {msg}')

        if msg["text"] != 'Please don\'t quote me':
            self.send_text_with_quote(msg['chat']['id'], msg["text"], quoted_msg_id=msg["message_id"])


class ObjectDetectionBot(Bot):
    def handle_message(self, msg):
        logger.info(f'Incoming message: {msg}')

        if self.is_current_msg_photo(msg):
            # TODO download the user photo (utilize download_user_photo)
            img_path = self.download_user_photo(msg)
            # TODO upload the photo to S3
            s3.upload_file(img_path, images_bucket, os.path.basename(img_path))
            #TODO send a request to the `yolo5` service for prediction
            # Use requests library to send HTTP post request to Yolo5 predict endpoint + extract the base name of the img
            yolo5_response = requests.post(f"http://yolo5:8081/predict?imgName={os.path.basename(img_path)}")
            # TODO send results to the Telegram end-user
            if yolo5_response.status_code == 200:
                response = yolo5_response.json()['labels'] # This variable decodes the Json output and holds the labels key / Object
                self.send_text(msg['chat']['id'], "Object detection results:")
                detected_objects = {}
                #Loop through response and get hold of the class object that appears in format if it exists then increment it if not then add it.
                for i in response:
                    if i['class'] in detected_objects:
                        detected_objects[i['class']] += 1
                    else:
                        detected_objects[i['class']] = 1
                #logger.info(detected_objects)
                result = ''
                for k,v in detected_objects.items():
                    result += f"{k}: {v}\n" 
                self.send_text(msg['chat']['id'], result) 
            else:
                self.send_text(msg['chat']['id'], "Error processing image. Please try again later.")


