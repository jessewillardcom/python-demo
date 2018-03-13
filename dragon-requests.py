from tqdm import tqdm
from urllib import parse
import requests

# Issues Range 001-430
for x in range(1, 51): #Step (1)
#for x in range(50, 101): #Step (2)
#for x in range(101, 151): #Step (3)
	value = str(x)
	if len(value) == 1:
		num = "00"+str(value)
	elif len(value) == 2:
		num = "0"+str(value)
	else:
		num = str(value)
	url = "https://rpg.rem.uz/Dungeons%20%26%20Dragons/Magazines/Dragon/001-050/Dragon%20Magazine%20-%20"+num+".pdf"
	#url = "https://rpg.rem.uz/Dungeons%20%26%20Dragons/Magazines/Dragon/051-100/Dragon%20Magazine%20-%20"+num+".pdf"
	#url = "https://rpg.rem.uz/Dungeons%20%26%20Dragons/Magazines/Dragon/101-150/Dragon%20Magazine%20-%20"+num+".pdf"

	print( parse.unquote(url) )
	response = requests.get(url, stream=True)

	with open("Dragon_"+num+".pdf", "wb") as handle:
	    for data in tqdm(response.iter_content()):
	        handle.write(data)
