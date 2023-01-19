import subprocess
import re

def get_ping(host):
    # Exécutez un test de ping avec un timeout de 1 seconde
    result = subprocess.run(
        ['ping', '-c', '1', '-W', '1', host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


    output = result.stdout.decode('utf-8')


    latency_search = re.search('time=(\d+\.\d+) ms', output)
    if latency_search:
        return float(latency_search.group(1))
    else:
        return None


latency = get_ping('google.com')

