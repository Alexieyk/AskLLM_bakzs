from phone_utils import check_phone_status
import cfg
from bots.chat import send_message


class Agent:

    def __init__(self):
        self.phone_number = ""
        self.id_number = ""

    def get_response(self, bot_text, bot_label, user_text):
        phone_status = check_phone_status(self.phone_number)  # Calling the function from the imported script

        # Prepare the response message based on the phone status
        if phone_status["status"] == "����":
            msg = f"���ã������ֻ���״̬Ϊ��������ǰ���Ϊ{phone_status['balance']}Ԫ���ײ�Ϊ{phone_status['package']}��ʣ������Ϊ{phone_status['remain_data']}��ʣ��ͨ��ʱ��Ϊ{phone_status['remain_call']}���ӡ�"
        elif phone_status["status"] == "ͣ��":
            msg = "���ã������ֻ�����ͣ�������ֵ����ʹ�á�"
        elif phone_status["status"] == "Ƿ��":
            msg = f"���ã������ֻ�����Ƿ�ѣ�Ƿ�ѽ��Ϊ{abs(float(phone_status['balance']))}Ԫ���뼰ʱ��ֵ�Իָ�ʹ�á�"

        return msg
