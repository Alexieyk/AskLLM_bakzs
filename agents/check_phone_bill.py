import json
import datetime
from phone_utils import check_phone_bill  # Importing the required function
from bots.chat import send_message
import cfg


class Agent:

    def __init__(self):
        self.phone_number = ""
        self.id_number = ""

    @staticmethod
    def extract_dates(input_str):
        try:
            # Extract dates from the string
            dates = json.loads(input_str)
            start_date_str, end_date_str = dates
            # Convert date strings to datetime objects
            start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')
            end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')
            # Format datetime objects to specified string format
            formatted_start_date = start_date.strftime('%Y-%m-%d')
            formatted_end_date = end_date.strftime('%Y-%m-%d')

            # Build result dictionary
            result = {
                "start_date": formatted_start_date,
                "end_date": formatted_end_date
            }
        except Exception as e:
            # Use default dates when an error occurs, from the 1st of the current month to the current day
            today = datetime.datetime.today()
            start_date = today.replace(day=1)  # First day of the current month
            end_date = today

            result = {
                "start_date": start_date.strftime('%Y-%m-%d'),
                "end_date": end_date.strftime('%Y-%m-%d')
            }
        return result

    def get_response(self, bot_text, bot_label, user_text):
        response_text = llm_chat(
            query=f"<�û��ı�>{user_text}</�û��ı�>\n������Ҵ��û��ı��У���ȡ������Ҫ��ѯ��ʱ�����䡣����['20240401','20240430']",
            system="����һ����������ˣ�����԰��Ҵ��û��ı��У���ȡ������Ҫ��ѯ��ʱ�����䡣����['20240401','20240430']�����ʽΪ:['��ʼʱ��','����ʱ��']",
        )
        time_interval = self.extract_dates(response_text)
        start_date = time_interval["start_date"]
        end_date = time_interval["end_date"]


        bill_info = check_phone_bill(self.phone_number)


        if bill_info:
            msg = f"���ã������˵���ϢΪ��{bill_info}"
        else:
            msg = "��Ǹ��δ�ܲ�ѯ�������˵���Ϣ"
        #�����˵����ͷ������ã���ѯ�������ֹĿǰΪֹ/10�¹������� Ԫ�����а����ײͷ��� Ԫ�����ŷ� Ԫ��
        #��ʷ�˵����ͷ������ã���ѯ��10�����ѽ��� Ԫ�������ײͷ� Ԫ�����ŷ���Ԫ��
        return msg
