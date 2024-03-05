import random
import cfg
from bots.chat import send_message
from phone_utils import check_phone_card_plan
class Agent:

    def __init__(self):
        self.phone_number = ""
        self.id_number = ""

    def get_response(self, bot_text, bot_label, user_text):
        plan = check_phone_card_plan(self.phone_number)  # Calling the function from the imported script

        # Prepare the response message
        msg = f"�����ֻ����ײ�Ϊ��{plan['package']}�����⣺{plan['monthly rent']}Ԫ��������{plan['remain_data']}��ʣ��ͨ��ʱ����{plan['remain_call']}����"
 #������˾��������-89�û��������ʷ�����Ϊ�ײͷ�89Ԫ/�£�����60����ȫ������ͨ����20Gȫ������������������0.15Ԫ/���ӣ�����3Ԫ/G�հ���������Ч���Զ�����������0.1Ԫ/��������0.5Ԫ/��������������ʾ������ִ�б�׼�ʷѡ��������°��������ײͷѺ���Դ����Լ��2�꣬�ڼ��ֹͣ�����Ž��ɱ��Ϊͬϵ�иߵ��ײʹ�����Ч��

        return msg




