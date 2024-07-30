import time
import psutil
import logging

def send_alert(resource, usage, threshold):
    logger.warning(f"{resource} usage is {usage:.2f}%, exceeding threshold of {threshold}%")


def display_usage(cpu_usage,mem_usage,disk_usage,bars=50):
    cpu_percent = (cpu_usage/100.0)
    cpu_bar = '	█' * int(cpu_percent * bars) + '_' * (bars- int(cpu_percent *bars))
    mem_percent = (mem_usage/100.0)
    mem_bar = '	█' * int(mem_percent *bars) + '_' * (bars- int(mem_percent *bars))
    disk_percent = disk_usage / 100.0
    disk_bar = '█' * int(disk_percent * bars) + '_' * (bars - int(disk_percent * bars))


    print(f"\r CPU Usage: | |{cpu_bar} | {cpu_usage:.2f}%")
    print(f"\r Memory Usage: | |{mem_bar} | {mem_usage:.2f}%")
    print(f"\r Disk Usage: | |{disk_bar} | {disk_usage:.2f}%")
    print(f"\r Running Processes: {len(processes)}")


    cpu_threshold   = 80
    mem_threshold = 80
    disk_threshold = 80 
     
     

    if cpu_usage > cpu_threshold:
        send_alert("CPU", cpu_usage, cpu_threshold)
    if mem_usage > mem_threshold:
        send_alert("Memory", mem_usage, mem_threshold)
    if disk_usage > disk_threshold:
        send_alert("Disk", disk_usage, disk_threshold)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    file_handler = logging.FileHandler('system_monitor.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

while True: 
    disk_usage = psutil.disk_usage('/').percent  # add path of your disk 
    processes = psutil.process_iter(['pid', 'name']) # add processe id  and process name 
    psutil. disk_usage(),psutil.Process(),
    display_usage(psutil.cpu_percent(),psutil.virtual_memory().percent,psutil.disk_usage(),processes,30)
    time.sleep(5)