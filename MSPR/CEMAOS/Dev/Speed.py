import subprocess

def get_speed():
    try:
        result = subprocess.run(['bash', '/etc/speed.sh'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        download_speed = output.split("\n")[0].split(": ")[1]
        upload_speed = output.split("\n")[1].split(": ")[1]
        return (download_speed, upload_speed)
    except:
        return ("Error", "Error")

download_speed, upload_speed = get_speed()
print(f"Download speed: {download_speed}")
print(f"Upload speed: {upload_speed}")