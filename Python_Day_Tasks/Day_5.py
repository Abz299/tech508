#[TASK ONE]
# Task: Convert a Python dictionary into a JSON-formatted string and a JSON file
# 🎯 Outcome (By doing this you should):
# •	Learn to use Python scripts to covert dictionary data into:
# o	a string in JSON format
# o	a JSON file
# •	Learn how to decipher existing code, simplify it, comment on different parts of it and explain what it does
#
#  
# Starting code:
# # create the dictionary
# servers_dict = {
#     "server1": {
#         "hostname": "web-server-1",
#         "ip_address": "192.168.1.1",
#         "role": "web",
#         "status": "active"
#     },
#     "server2": {
#         "hostname": "db-server-1",
#         "ip_address": "192.168.1.2",
#         "role": "database",
#         "status": "maintenance"
#     }
# }
#
# Subtasks:
# •	Convert this Python dictionary into a JSON-formatted string
# •	Convert this Python dictionary to a JSON file
#
# Extra guidance:
# •	Use the json library
# •	Write any other code necessary to test things converted correctly

# import json
#
# servers_dict = {
#     "server1": {
#         "hostname": "web-server-1",
#         "ip_address": "192.168.1.1",
#         "role": "web",
#         "status": "active"
#     },
#     "server2": {
#         "hostname": "db-server-1",
#         "ip_address": "192.168.1.2",
#         "role": "database",
#         "status": "maintenance"
#     }
# }

# Task: Convert the Python dictionary into a JSON-formatted string
# json_string = json.dumps(servers_dict, indent=4)
# print("convertone:", json_string)

# # Task: Convert the Python dictionary to a JSON file
# json_filename = "servers_data.json"
# with open(json_filename, 'w') as json_file:
#     json.dump(servers_dict, json_file, indent=4)
#
# print("converttwo", json_filename)

#[TASK TWO]
# Task: Convert JSON file and JSON string from JSON file to Python dict
# 🎯 Outcome (By doing this you should):
# •	Learn to use Python scripts to convert a JSON string and JSON file to a dictionary
# •	Learn how to decipher existing code, simplify it, comment on different parts of it and explain what it does
#
# Subtask 1: Convert JSON file to a Python dictionary
# Steps:
# 1.	Create a new file servers.json and add this JSON to it:
# {
# 	"server1": {
# 		"hostname": "web-server-1",
# 		"ip_address": "192.168.1.1",
# 		"role": "web",
# 		"status": "active"
# 	},
# 	"server2": {
# 		"hostname": "db-server-1",
# 		"ip_address": "192.168.1.2",
# 		"role": "database",
# 		"status": "maintenance"
# 	}
# }
#
# 2.	Create a file called parse_json_to_dict.py and add code to it to:
# Steps:
# a.	Use 'with' to open the file created above
# b.	Parse contents the JSON file into a Python dictionary named "servers"
# c.	Print out the type of "servers"
# d.	Print out the dictionary record with the key "server1"
# e.	Print out the dictionary record with the key "server2"
# f.	Print all of the keys and values. Output should be:
# Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
#   Record key and sub value: 'hostname' = 'web-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.1'
#   Record key and sub value: 'role' = 'web'
#   Record key and sub value: 'status' = 'active'
# Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
#   Record key and sub value: 'hostname' = 'db-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.2'
#   Record key and sub value: 'role' = 'database'
#   Record key and sub value: 'status' = 'maintenance'l

#[1]
servers_dict = {
	"server1": {
		"hostname": "web-server-1",
		"ip_address": "192.168.1.1",
		"role": "web",
		"status": "active"
	},
	"server2": {
		"hostname": "db-server-1",
		"ip_address": "192.168.1.2",
		"role": "database",
		"status": "maintenance"
	}
}

#[2]
import json

json_file_name = "servers.json"

with open(json_file_name, 'r') as file:
    servers = json.load(file)




