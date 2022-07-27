import subprocess
import os
import time
import sys
from time import sleep

home = os.path.expanduser("~")
words = "Hello! Thanks for using my script\n"
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

runcmd("wget https://playit.gg/downloads/playit-0.8.1-beta", verbose = True)
runcmd("wget https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar", verbose = True)


os.system("sudo apt install screen")
os.system("screen -dmS bungee java -jar BungeeCord.jar")
os.system("chmod 777 playit-0.8.1-beta")
os.system("screen -dmS playit ./playit-0.8.1-beta")
time.sleep(2)
runcmd("wget --directory-prefix=plugins https://github.com/Kr1S-D/UltimateAntibotRecoded/releases/download/v4.0.2/UltimateAntibot-bungeecord-4.0.2-ABYSS.jar", verbose = False)
time.sleep(2)
os.system(f"screen -S brungee -X quit")
os.system(f"screen -S playit -X quit")
os.system("pkill screen")
os.system("nano config.yml")
os.system("screen -dmS bungee java -jar BungeeCord.jar")
os.system(f"screen -S brungee -X quit")
time.sleep(2)
os.chdir(f"{home}/test/plugins/UltimateAntiBot")
os.system("nano config.yml")
time.sleep(2)
os.chdir(f"{home}/test")
time.sleep(2)
os.system("pkill screen")
os.system("chmod 777 playit-0.8.1-beta")
os.system("screen -dmS playit ./playit-0.8.1-beta")
os.system("screen -dmS bungee java -jar BungeeCord.jar")
os.system("screen -r playit")
