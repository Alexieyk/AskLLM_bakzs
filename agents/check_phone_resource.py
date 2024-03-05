import random
from phone_utils import check_phone_resource
from bots.chat import send_message
import cfg

class Agent:

    def __init__(self):
        self.phone_number = ""
        self.id_number = ""

    def get_response(self, bot_text, bot_label, user_text):
        total_resource = 100  # Assuming total available resource is 100GB
        resource = check_phone_resource(self.phone_number)
        remaining_resource = total_resource - resource

        # Prepare the response message
        msg = f"��ѯ���������{total_resource}GB������Ŀǰ��ʹ��{resource}GB����ʣ��{remaining_resource}GB"

        return msg

        #�ھ�����ѯ���������xx����/G����ֹĿǰ��ʹ��xx����/G����ʣ��xx����/G��

