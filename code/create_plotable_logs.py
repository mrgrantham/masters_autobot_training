import os
import sys
import subprocess

model_log_path = sys.argv[1]
script_dir_path = os.path.dirname(os.path.realpath(__file__))

#Get directory where the model logs is saved, and move to it
model_log_dir_path = os.path.dirname(model_log_path)
os.chdir(model_log_dir_path)

command = script_dir_path + '/parse_log.sh ' + model_log_path
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()