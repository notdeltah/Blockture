import json
import os
import pyperclip
import requests
import secrets
from time import sleep

headers = {'Authorization': f'token {os.environ["gh_key"]}'}

def generate_user_key():
	while True:
		uak = secrets.token_hex(8)
		if uak not in json.loads(
		  requests.get(url=f"https://api.github.com/gists/{os.environ['gist_id']}",
		               headers=headers).content)["files"]["accs.json"]["content"]:
			break
	return uak


class style:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'


with open("title.txt", "r") as fp:
	title = fp.read()

while True:
	os.system("cls||clear")
	print(f"{style.BOLD}{title}{style.END}")
	print("1 - sign in")
	print("2 - join blockture")
	select = input()
	if select.strip() == "1":
		while True:
			os.system("cls||clear")
			print("please enter your access key:")
			ak = input()
			if ak in json.loads(requests.get(url=f"https://api.github.com/gists/{os.environ['gist_id']}",
		               headers=headers).content)["files"]["accs.json"]["content"]:
										 break
		break
		...
	elif select.strip() == "2":
		os.system("cls||clear")
		print("generating your access key...")
		ak = generate_user_key()
		os.system("cls||clear")
		print(f"------------------\n {ak}\n------------------")
		print("\nkeep this key safe and secret. if it's lost, there will be no way of recovering your data.")
		sleep(5)
		print("press enter to proceed.")
		input()
		os.system("cls||clear")
		break

with open("saves.txt", "r") as fp:
	print(f"{style.BOLD}{fp.read()}{style.END}")

print("SAVE 1")
print("NEW SAVE")
