"""
squeue --partition=mllm-align
             JOBID  VIRTUAL_PARTITION       NAME     QUOTA_TYPE     USER PHX_PRIORITY ST        TIME  NODES TOTAL_GRES NODELIST(REASON)                        
          16707396         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707394         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707392         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707390         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707388         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707385         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707384         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707382         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707379         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707377         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707374         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707372         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707371         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707368         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707365         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707363         mllm-align     python       reserved zhouzhan       normal PD        0:00      1      gpu:4 (Quota)                                 
          16707359         mllm-align     python       reserved zhouzhan       normal  R        3:56      1      gpu:4 SH-IDC1-10-140-0-153                    
          16707361         mllm-align     python       reserved zhouzhan       normal  R        3:56      1      gpu:4 SH-IDC1-10-140-0-153                    
          16707357         mllm-align     python       reserved zhouzhan       normal  R        4:04      1      gpu:4 SH-IDC1-10-140-1-104                    
          16707358         mllm-align     python       reserved zhouzhan       normal  R        4:04      1      gpu:4 SH-IDC1-10-140-1-104                    
          16707352         mllm-align     python       reserved zhouzhan       normal  R       17:58      1      gpu:4 SH-IDC1-10-140-0-204                    
          16707354         mllm-align     python       reserved zhouzhan       normal  R       17:58      1      gpu:4 SH-IDC1-10-140-0-204                    
          16707349         mllm-align     python       reserved zhouzhan       normal  R       26:37      1      gpu:4 SH-IDC1-10-140-0-206                    
          16707347         mllm-align     python       reserved zhouzhan       normal  R       27:37      1      gpu:4 SH-IDC1-10-140-0-206                    
          16707345         mllm-align     python       reserved zhouzhan       normal  R       34:57      1      gpu:4 SH-IDC1-10-140-0-151                    
          16708347         mllm-align interactiv       reserved lixiangt       normal  R       46:20      1      gpu:1 SH-IDC1-10-140-0-151                    
          16707343         mllm-align     python       reserved zhouzhan       normal  R       49:33      1      gpu:4 SH-IDC1-10-140-1-89                     
          16707342         mllm-align     python       reserved zhouzhan       normal  R       58:29      1      gpu:4 SH-IDC1-10-140-1-89                     
          16707339         mllm-align     python       reserved zhouzhan       normal  R     1:16:45      1      gpu:4 SH-IDC1-10-140-1-173                    
          16706802         mllm-align interactiv       reserved liuyujie       normal  R     5:04:06      1      gpu:1 SH-IDC1-10-140-1-173                    
          16703920         mllm-align interactiv       reserved dongzhic       normal  R    19:42:46      1      gpu:2 SH-IDC1-10-140-1-173                    
          16703899         mllm-align interactiv       reserved dongzhic       normal  R    19:52:21      1      gpu:2 SH-IDC1-10-140-0-151                    
          16699588         mllm-align interactiv       reserved liuzhixu       normal  R    19:54:07      1      gpu:8 SH-IDC1-10-140-0-155                    
          16701027         mllm-align liuzhixuan       reserved liuzhixu       normal  R  1-02:32:33      1      gpu:0 SH-IDC1-10-140-0-151                    
          16697758         mllm-align       bash       reserved lixiangt       normal  R  1-11:50:34      1      gpu:0 SH-IDC1-10-140-0-204                    
          16696353         mllm-align       bash       reserved wangyuan       normal  R  1-15:18:57      1      gpu:8 SH-IDC1-10-140-0-188                    
          16682684         mllm-align       bash       reserved wangyuan       normal  R  3-07:24:26      1      gpu:8 SH-IDC1-10-140-1-39                     
          16671059         mllm-align       bash       reserved yangchao       normal  R  4-23:04:08      1      gpu:0 SH-IDC1-10-140-0-153                    
          16670959         mllm-align       bash       reserved yangchao       normal  R  4-23:13:44      1      gpu:0 SH-IDC1-10-140-1-104
"""
# */30 8-1 * * * /usr/bin/python3 /path/to/your_script.py
import requests
import subprocess


# 交互对齐团队
URL = "https://open.feishu.cn/open-apis/bot/v2/hook/dadc8a28-ee60-479a-a4e3-58ee17fb907e"

# Run the squeue command and capture the output
command = "squeue --partition=mllm-align"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# Parse the output into a list of dictionaries
lines = result.stdout.splitlines()
headers = lines[0].split()  # The first line contains the headers

# List to store job information
jobs = []

# Iterate over the lines and extract the job details
for line in lines[1:]:  # Skip the header line
    fields = line.split()
    job_dict = dict(zip(headers, fields))
    jobs.append(job_dict)

# Step 3: Identify jobs that request gpu:8 but have no GPU usage
eight_gpu_jobs = [job for job in jobs if "gpu:8" in job["TOTAL_GRES"]]

# Step 4: Run swatch command for each of these jobs to check GPU usage
idle_eight_gpu_jobs = []
for job in eight_gpu_jobs:
    nodelist = job["NODELIST(REASON)"]
    
    # Run the swatch command to monitor GPU usage
    swatch_command = f"swatch -n {nodelist} nv always"
    swatch_result = subprocess.run(swatch_command, shell=True, capture_output=True, text=True)

    if swatch_result.stdout.count(" 0%") >= 4 or "No running processes found" in swatch_result.stdout:
        idle_eight_gpu_jobs.append(job)

content = []
for job in idle_eight_gpu_jobs:
    content.append({"tag": "text", "text": f"JOBID:{job['JOBID']} | USER:{job['USER']} | NODELIST(REASON):{job['NODELIST(REASON)']}\n"})

if content:
    response = requests.post(
        URL,
        json = {
            "msg_type": "post",
            "content": {
                "post": {
                    "en": {
                        "title": "有不活跃任务",
                        "content": [content],
                    }
                }
            }
        }
    )
