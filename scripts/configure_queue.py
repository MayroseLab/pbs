from __future__ import print_function
import sys

if len(sys.argv) > 1:
    conf_path = sys.argv[1]
else:
    conf_path = "queue.conf"
print("Welcome to the queue configuration wizard."
      "Please insert the following default values."
      "If you don't want to set a default value for"
      "a parameter, simply hit Return.")

conf_params = {
    "queue": None,
    "account": None,
    "nodes": 1,
    "ppn": 1,
    "walltime": None,
    "pmem": None,
    "qos": None,
    "email": None,
    "priority": 0
}
conf_params["queue"] = raw_input("What is the default queue name?")
conf_params["account"] = raw_input("What is the default account name?")
conf_params["walltime"] = raw_input("What is the default job walltime?")
conf_params["qos"] = raw_input("What is the default Quality of Service?")
conf_params["email"] = raw_input("What is your E-mail address? (for notifications)")

with open(conf_path,'w') as fo:
    for par in conf_params:
        if conf_params[par]:
            print("%s=%s" %(par, conf_params[par]), file=fo)
print("Queue configuration created at %s" % conf_path)
