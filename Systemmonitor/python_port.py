# import the packages
import psutil


# acceess the port
def python_port_name(process_name, port):
    processes = [proc for proc in psutil.process_iter()
                 if proc.name() == process_name]

    for p in processes:
        for c in p.connections():
            if c.status == 'LISTEN ON PORT' and c.ladder.port == port:
                return p

    return None


# print the result
print("PID", " ")
