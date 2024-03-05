from phone_utils import check_phone_location
import cfg
from bots.chat import send_message

class Agent:

    def __init__(self):
        self.phone_number = ""
        self.id_number = ""

    def get_response(self, bot_text, bot_label, user_text):
        location_info = check_phone_location(self.phone_number)  # Calling the function from the imported script

        # Prepare the response message
        msg = f"���ã���ѯ���ĺ��������Ϊ��{location_info}"
    #���ã���ѯ���ĺ��������Ϊxx�����ã���ѯ����PIN��Ϊxxx����PUK����ɸ�֪PUK1�룬PIN���粻�Կɸ�֪���Գ�ʼֵ0000���������ã���ѯ����ICCID��Ϊxxx�����ɸ��ݺ����ѯICCID�룬�޷�����ICCID�뷴���ѯ���룬����û���ICCID��֪�����룬�����û��ѿ�������ĵ����ںſͷ����ѯ
        return msg
