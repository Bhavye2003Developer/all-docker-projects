import subprocess

subprocess.run('docker build -t ide .'.split())

res = subprocess.run('docker run ide'.split(), stdout=subprocess.PIPE)

print(res.stdout)