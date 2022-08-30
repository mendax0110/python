#import the necessary packages
import os, platform, subprocess, socket, psutil, netifaces, cpuinfo

#define the sizes
kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)

#get the memory info
memTotal = int(psutil.virtual_memory()[0]/gb)
memUsed = int(psutil.virtual_memory()[3]/gb)
memFree = int(psutil.virtual_memory()[1]/gb)
memPercent = int(memUsed/memTotal*100)
storageTotal = int(psutil.disk_usage('/')[0]/gb)
storageUsed = int(psutil.disk_usage('/')[1]/gb)
storageFree = int(psutil.disk_usage('/')[2]/gb)
storagePercent = int(storageUsed/storageTotal*100)
info = cpuinfo.get_cpu_info()['brand']

#get the cpu usage
def service():
    print()
    pidToal = len(psutil.pids())
    print('PID Total: ' + str(pidToal))

#print the average load
def load_avg():
    print()
    print('----------Load Average----------')
    print()
    print("Load avg(1 mins) :", round(os.getloadavg()[0],2))
    print("Load avg(5 mins) :", round(os.getloadavg()[1],2))
    print("Load avg(15 mins):", round(os.getloadavg()[2],2))

#print the system info
def system():
    core = os.cpu_count()
    host = socket.gethostname()
    print()
    print('----------System Info----------')
    print()
    print("Hostname     :", host)
    print("System       :", platform.system(), platform.machine())
    print("Kernel       :", platform.release())
    print("Compiler     :", platform.python_compiler())
    print("CPU          :", info, core, "(Core)")
    print("Memory       :", memTotal, "GB (Total)", memUsed, "GB (Used)", memFree, "GB (Free)", memPercent, "% (Percent)")
    print("Disk         :", storageTotal, "GB (Total)", storageUsed, "GB (Used)", storageFree, "GB (Free)", storagePercent, "% (Percent)")

#print the CPU usage
def cpu():
    print()
    print('----------CPU Info----------')
    print()
    print("CPU Usage : ", cpuUsage, "GiB")

#print the Memory usage
def memory():
    print()
    print('----------Memory Info----------')
    print()
    print("RAM Used     : ", memUsed, "GiB /", memTotal, "GiB","(",memPercent,"%",")")
    print("Disk Used    : ", storageUsed,"GiB /",storageTotal,"GiB","(",storagePercent,"%",")")

#print the network info
def network():
    active = netifaces.gateways()['default'][netifaces.AF_INET][1]
    speed = psutil.net_io_counters(pernic=False)
    sent = speed[0]
    psend = round(speed[2]/kb, 2)
    psecv = round(speed[3]/kb, 2)
    print()
    print('----------Network Info----------')
    print()
    print("Active Interfaces : ",active)
    print("Packet send       : ",psend, "KiB/s")
    print("Packet recv       : ",psecv, "KiB/s")

def main():
    service()
    system()
    load_avg()
    memory()
    network()

main()