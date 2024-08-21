import sys
import os 

args = sys.argv
arg = args[1]
progam_file = args[0]

print(f"hellow {arg} from {progam_file}")
host = os.environ.get("HOST")
print(f"connecting to {host}")

#$Env:HOST = "arthur"

#$Env:HOST