# */30 8-23 * * * /usr/bin/python3 /path/to/your_script.py
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
