import concurrent.futures
import psutil
import GPUtil
import platform
import pynvml
from datetime import datetime



" FOR APP "
class SystemInfo:
    def __init__(self):
        pass

    def get_cpu_count(self):
        physical_cores = psutil.cpu_count(logical=False)
        total_cores = psutil.cpu_count(logical=True)
        return physical_cores, total_cores
    def get_gpu_info(self):
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append({
                'id': gpu.id,
                'name': gpu.name,
                'load': gpu.load * 100,
                'free_memory': gpu.memoryFree,
                'used_memory': gpu.memoryUsed,
                'total_memory': gpu.memoryTotal,
                'temperature': gpu.temperature
            })
        return gpu_info
    def get_memory_info(self):
        virtual_mem = psutil.virtual_memory()
        return virtual_mem
    def get_formatted_info(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            count_future = executor.submit(self.get_cpu_count)
            gpu_future = executor.submit(self.get_gpu_info)
            mem_future = executor.submit(self.get_memory_info)

            cpu_percent = psutil.cpu_percent()
            physical_cores, total_cores = count_future.result()
            gpu_info = gpu_future.result()
            virtual_mem = mem_future.result()

        cpu_I = []
        cpu_percents = []
        for i, l in enumerate(psutil.cpu_percent(percpu=True)):  # noqa: E741
            cpu_I.append(i)
            cpu_percents.append(l) 


        if gpu_info:
            gpu_details = "".join([f"{gpu['name']} | {gpu['load']:.0f}% | {gpu['used_memory']}MB/{gpu['total_memory']}MB | {gpu['temperature']}°C" for gpu in gpu_info])
        else:
            gpu_details = "No GPU detected"

        return {
            "cpu": cpu_percent,
            "cpu_cores_i": cpu_I,
            "cpu_cores_percent": cpu_percents,
            "physical_cores": physical_cores,
            "total_cores": total_cores,
            "occupied_ram": virtual_mem.used / (1024 ** 3),
            "free_ram": virtual_mem.available / (1024 ** 3),
            "total_ram": virtual_mem.total / (1024 ** 3),
            "gpu": gpu_info[0]['load'] if gpu_info else None,
            "gpu_info": gpu_details
        }

" FOR TELEGRAM BOT "
def get_system_info():
    try:
        pynvml.nvmlInit()
        nvml_load = True
    except:   
        pass
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os_info = platform.system()
    operating_system_version = platform.release()
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_usage = memory.used / (1024 ** 3)
    total_memory = memory.total / (1024 ** 3)
    memory_have = total_memory - memory_usage
    if nvml_load is True:
        device_count = pynvml.nvmlDeviceGetCount()
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            gpu_info = pynvml.nvmlDeviceGetUtilizationRates(handle)
            gpu_load = gpu_info.gpu
    message_info_rus = "| Pc-Stat-Bot |"
    message_info_rus += "| ЦП:\n"
    cpu_usage = "\n".join(
        f"|    Ядро {i+1}: {l}%" for i, l in enumerate(psutil.cpu_percent(percpu=True)))  # noqa: E741
    message_info_rus += cpu_usage
    message_info_rus += f"\n|    ЦП: {cpu_percent}%\n|\n"
    message_info_rus += "| Память:\n"
    message_info_rus += f"|    Занято/Всего: {memory_usage:.2f} ГБ / {total_memory:.2f} ГБ\n"
    message_info_rus += f"|    Занято: {memory_usage:.2f} ГБ\n"
    message_info_rus += f"|    Свободно: {memory_have:.2f} ГБ\n"
    message_info_rus += f"|    Всего: {total_memory:.2f} ГБ\n|\n"
    message_info_rus += "| Прочее:\n"
    if nvml_load is True:
        message_info_rus += f"|    ГП: {gpu_load}%\n"
    else:
        message_info_rus += "|    ГП: Ошибка - GPU_1\n"
    message_info_rus += f"|    Время: {current_time}\n"
    message_info_rus += f"|    ОС: {os_info} {operating_system_version}\n|\n"
    message_info_rus += "| Pc-Stat-Bot |"

    message_info_eng = "| Pc-Stat-Bot |"
    message_info_eng += "| Cpu:\n"
    cpu_usage = "\n".join(
        f"|    Core {i}: {l}%" for i, l in enumerate(psutil.cpu_percent(percpu=True)))  # noqa: E741
    message_info_eng += cpu_usage
    message_info_eng += f"\n|    Cpu: {cpu_percent}%\n|\n"
    message_info_eng += "| Memory:\n"
    message_info_eng += f"|    Occupied/Total: {memory_usage:.2f} GB / {total_memory:.2f} GB\n"
    message_info_eng += f"|    Occupied: {memory_usage:.2f} GB\n"
    message_info_eng += f"|    Free: {memory_have:.2f} GB\n"
    message_info_eng += f"|    Total: {total_memory:.2f} GB\n|\n"
    message_info_eng += "| Other:\n"
    if nvml_load is True:
        message_info_eng += f"|    GPU: {gpu_load}%\n"
    else:
        message_info_eng +=  "|    GPU: Error - GPU_1\n"
    message_info_eng += f"|    Time: {current_time}\n"
    message_info_eng += f"|    OS: {os_info} {operating_system_version}\n|\n"
    message_info_eng += "| Pc-Stat-Bot |"

    return message_info_eng, message_info_rus