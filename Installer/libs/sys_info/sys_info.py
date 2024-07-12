import concurrent.futures
import psutil
import GPUtil

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

        cpu_cores_eng = ""
        cpu_cores_rus = ""
        for i, l in enumerate(psutil.cpu_percent(percpu=True)):  # noqa: E741
            cpu_cores_eng += f"Core {i+1}: {l}%\n"
            cpu_cores_rus += f"Ядро {i+1}: {l}%\n"  


        if gpu_info:
            gpu_details = "".join([f"{gpu['name']} | {gpu['load']:.0f}% | {gpu['used_memory']}MB/{gpu['total_memory']}MB | {gpu['temperature']}°C" for gpu in gpu_info])
        else:
            gpu_details = "No GPU detected"

        return {
            "cpu": cpu_percent,
            "cpu_cores_eng": cpu_cores_eng,
            "cpu_cores_rus": cpu_cores_rus,
            "physical_cores": physical_cores,
            "total_cores": total_cores,
            "occupied_ram": virtual_mem.used / (1024 ** 3),
            "free_ram": virtual_mem.available / (1024 ** 3),
            "total_ram": virtual_mem.total / (1024 ** 3),
            "gpu": gpu_info[0]['load'] if gpu_info else None,
            "gpu_info": gpu_details
        }
