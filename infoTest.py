# coding=utf-8
import psutil
import json

cpu_time = psutil.cpu_times()
virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
disk_usage = psutil.disk_usage('/')
disk_io_counters = psutil.disk_io_counters()

data = {
    'cpu_count_logical': psutil.cpu_count(),
    'cpu_count': psutil.cpu_count(logical=False),
    'cpu_time': {
        'user': cpu_time[0],
        'nice': cpu_time[1],
        'system': cpu_time[2],
        'idle': cpu_time[3]
    },
    'cpu_percent': psutil.cpu_percent(interval=1, percpu=True),
    'virtual_memory': {
        'total': virtual_memory[0],
        'available': virtual_memory[1],
        'percent': virtual_memory[2],
        'used': virtual_memory[3],
        'free': virtual_memory[4],
        'active': virtual_memory[5],
        'inactive': virtual_memory[6],
        'wired': virtual_memory[7]
    },
    'swap_memory': {
        'total': swap_memory[0],
        'used': swap_memory[1],
        'free': swap_memory[2],
        'percent': swap_memory[3],
        'sin': swap_memory[4],
        'sout': swap_memory[5]
    },
    'disk_usage': {
        'total': disk_usage[0],
        'used': disk_usage[1],
        'free': disk_usage[2],
        'percent': disk_usage[3]
    },
    'disk_io_counters': {
        'read_count': disk_io_counters[0],
        'write_count': disk_io_counters[1],
        'read_bytes': disk_io_counters[2],
        'write_bytes': disk_io_counters[3],
        'read_time': disk_io_counters[4],
        'write_time': disk_io_counters[5]
    },
    'pids_len': len(psutil.pids()),
}

print(json.dumps(data, ensure_ascii=False, indent=4))