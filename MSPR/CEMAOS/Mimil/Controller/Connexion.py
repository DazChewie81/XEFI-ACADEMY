import speedtest

test = speedtest.Speedtest(secure=1)
test.get_servers()
best = test.get_best_server()

print(f"Found:{best['host']} located in  {best['country']}")

download_result = test.download()
upload_result = test.upload()
ping_result = test.results.ping


print(f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result}s")