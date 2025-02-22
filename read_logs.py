import json
import re
import pathlib

logs_path = pathlib.Path('rspamd_log.txt')
output_json_file = 'rspamd_logs.json'

log_pattern = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "  
    r"#(?P<process_id>\d+)\((?P<process_type>\w+)\) "       
    r"<(?P<task_id>[a-z0-9]+)>; "                          
    r"(?P<category>\w+); "                                 
)
log_array = []

with open(logs_path, 'r') as log:
    for line in log:
        match = log_pattern.match(line)
        if match:
            log_data = match.groupdict()
            log_array.append(log_data)
            print(log_array)
    

with open(output_json_file, 'w') as rspamd_json:
     json.dump(log_array, rspamd_json, indent=4)
     
print({output_json_file})     
    
    

    

