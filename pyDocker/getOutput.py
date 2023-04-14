import subprocess

subprocess.run("docker build -t pycode .".split())
f = subprocess.check_output("docker run pycode".split()).decode()
print(f)