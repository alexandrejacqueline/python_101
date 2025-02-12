import sys
import re
import pandas as pd

def parse_log_data():
    parsed_log_data=[]

    with open('/home/alexandrejacqueline/code/alexandrejacqueline/pyton_101/101/hadoop.log','r') as f:
        for line in f:
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w*) \[(.*?)\] (.*?): (.*)', line)
            if match:
                parsed_log_data.append({
                    "timestamp": match.group(1),
                    "level": match.group(2),
                    "thread": match.group(3),
                    "source": match.group(4),
                    "message": match.group(5),
                })
    return parsed_log_data

def write_to_csv(parsed_log_data):
    df = pd.DataFrame(parsed_log_data)
    df.to_csv('/home/alexandrejacqueline/code/alexandrejacqueline/pyton_101/101/result.csv',index=False)


if __name__ == '__main__':
    write_to_csv(parse_log_data())
