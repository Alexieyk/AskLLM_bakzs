import json
import datetime
from phone_utils import check_phone_recharge
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
            # Return None if no dates are provided
            return None
        return result

    def get_response(self, bot_text, bot_label, user_text):
        response_text = llm_chat(
            query=f"<�û��ı�>{user_text}</�û��ı�>\n������Ҵ��û��ı��У���ȡ������Ҫ��ѯ��ʱ�����䡣����['20240401','20240430']",
            system="����һ����������ˣ�����԰��Ҵ��û��ı��У���ȡ������Ҫ��ѯ��ʱ�����䡣����['20240401','20240430']�����ʽΪ:['��ʼʱ��','����ʱ��']",
        )
        time_interval = self.extract_dates(response_text)

        if time_interval is None:
            # No time interval provided, retrieve the most recent record
            recharge_records = check_phone_recharge(self.phone_number)
            if recharge_records:
                # Extract the most recent record
                most_recent_record = max(recharge_records,key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'))
                # Prepare the response message for the most recent record
                msg = f"��ѯ��������ĳ�ֵ��¼���£�\n���ڣ�{most_recent_record['date']}����{most_recent_record['amount']}"
            else:
                msg = "��Ǹ��û���ҵ��κγ�ֵ��¼��"
        else:
            start_date = time_interval["start_date"]
            end_date = time_interval["end_date"]
            # Retrieve recharge records within the specified time interval
            recharge_records = check_phone_recharge(self.phone_number, start_date, end_date)

            if recharge_records:
                # Prepare the response message for the recharge records within the specified time interval
                msg = "��ѯ�����ĳ�ֵ��¼���£�\n"
                for record in recharge_records:
                    msg += f"���ڣ�{record['date']}����{record['amount']}\n"
            else:
                msg = "��ָ��ʱ�䷶Χ��δ�ҵ��κγ�ֵ��¼��"

        return msg
