	#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
import argparse
import json

print("""

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

███╗░░░███╗██╗░░░██╗██╗░░░░░████████╗██╗░██████╗░█████╗░░█████╗░███╗░░██╗
████╗░████║██║░░░██║██║░░░░░╚══██╔══╝██║██╔════╝██╔══██╗██╔══██╗████╗░██║
██╔████╔██║██║░░░██║██║░░░░░░░░██║░░░██║╚█████╗░██║░░╚═╝███████║██╔██╗██║
██║╚██╔╝██║██║░░░██║██║░░░░░░░░██║░░░██║░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║░╚═╝░██║╚██████╔╝███████╗░░░██║░░░██║██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░░░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
	 
𝗪𝗮𝗿𝗻𝗶𝗻𝗴 : 𝗜𝗳 𝘆𝗼𝘂 𝗮𝗿𝗲 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗮𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗳𝗶𝗿𝘀𝘁 𝘁𝗶𝗺𝗲, 𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗮𝗽𝗶 𝗸𝗲𝘆 𝘄𝗶𝘁𝗵 𝘁𝗵𝗲 𝗗 𝗼𝗽𝘁𝗶𝗼𝗻.

▄▀█   █▀▀ █▀█ █▀█   █ █▀█   █▀ █▀▀ ▄▀█ █▄░█
█▀█   █▀░ █▄█ █▀▄   █ █▀▀   ▄█ █▄▄ █▀█ █░▀█	 
	 
▄▄▄ 
█▄█   █▀▀ █▀█ █▀█   █▀▀ █ █░░ █▀▀   █▀ █▀▀ ▄▀█ █▄░█
█▄█   █▀░ █▄█ █▀▄   █▀░ █ █▄▄ ██▄   ▄█ █▄▄ █▀█ █░▀█	 


█▀▀   █▀▀ █▀█ █▀█   █░█ █▀█ █░░   █▀ █▀▀ ▄▀█ █▄░█
█▄▄   █▀░ █▄█ █▀▄   █▄█ █▀▄ █▄▄   ▄█ █▄▄ █▀█ █░▀█


█▀▄   ▀█▀ █▀█   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▄▀█ █▀█ █   █▄▀ █▀▀ █▄█
█▄▀   ░█░ █▄█   ██▄ █░▀█ ░█░ ██▄ █▀▄   █▀█ █▀▀ █   █░█ ██▄ ░█░	 
""")

secim = input("(A, B, C, D): ")


if secim == "D":

	key = input('Please enter the Api key for Virus Total: ')

	# Dosyayı yazma modunda aç
	with open("vırusapi.txt", "w") as file:
    	# Dosyaya adı yaz
   	 file.write(key)
   	 
	abuse = input('Please enter the Api key for abuse: ')

	# Dosyayı yazma modunda aç
	with open("abuseapi.txt", "w") as file:
    	# Dosyaya adı yaz
   	 file.write(abuse)
   	 secim = input("(A, B, C, D): ")

if secim == "D":

	key = input('Please enter the Api key for Virus Total: ')

	# Dosyayı yazma modunda aç
	with open("vırusapi.txt", "w") as file:
    	# Dosyaya adı yaz
   	 file.write(key)
   	 
	abuse = input('Please enter the Api key for abuse: ')

	# Dosyayı yazma modunda aç
	with open("abuseapi.txt", "w") as file:
    	# Dosyaya adı yaz
   	 file.write(abuse)
   	 
elif secim == "A":
    # Seçenek A seçilirse bu kod bloğu çalışacak
        
	print("""
	𝕿𝖍𝖆𝖓𝖐 𝖞𝖔𝖚 𝖋𝖔𝖗 𝖈𝖍𝖔𝖔𝖘𝖎𝖓𝖌 𝖚𝖘 <3
	""")
	 
	name = input('Name of IP List?: ')
	
	with open("vırusapi.txt", "r") as file:
  	  # Dosyadan adı oku
   	 apikey = file.read()
	#virüs = input('Please enter the Api key for Virus Total: ')
	  
	#abuse = input('Please enter the Api key for abuse: ')

	with open("abuseapi.txt", "r") as file:
  	  # Dosyadan adı oku
   	 apikeyabuse = file.read()
	 
	print("""

	░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗██╗███╗░░██╗░██████╗░
	██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██║████╗░██║██╔════╝░
	╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║██║██╔██╗██║██║░░██╗░
	░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██║██║╚████║██║░░╚██╗
	██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║██║██║░╚███║╚██████╔╝
	╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░
                                                                 
	""")
	
	with open(name, 'r') as f:
	
	    for a in f:
	        a.replace(" ", "")
	        line = \
	            requests.get('https://www.virustotal.com/api/v3/ip_addresses/%s'
	                          % a,
	                         headers={'User-agent': 'Mozilla/5.0(X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
	                         ,
	                         'x-apikey': apikey
	                         }).json()
	        
	        url = 'https://api.abuseipdb.com/api/v2/check'
	        querystring = {'ipAddress': '%s' % a, 'maxAgeInDays': '365'}
	        headers = {'Accept': 'application/json',
	                   'Key': apikeyabuse}
	        response = requests.request(method='GET', url=url,
	        headers=headers, params=querystring).json()
	        tot_abuse_count = response["data"]["totalReports"]
	        abuse_scor = response["data"]["abuseConfidenceScore"]
	        
	        country_info = line["data"]["attributes"]
	        dict_web = line['data']['attributes']['last_analysis_results']
	        tot_engine_c = 0
	        tot_detect_c = 0
	        result_eng = []
	        eng_name = []
	        count_harmless = 0
	        for i in dict_web:
	            tot_engine_c = 1 + tot_engine_c
	            if dict_web[i]['category'] == 'malicious' \
	                or dict_web[i]['category'] == 'suspicious' \
	                or dict_web[i]['category'] == 'malware':
	                result_eng.append(dict_web[i]['result'])
	                eng_name.append(dict_web[i]['engine_name'])
	                tot_detect_c = 1 + tot_detect_c
	        res = []
	        for i in result_eng:
	            if i not in res:
	              res.append(i)
	        result_eng = res
	        tespit = str(tot_detect_c)
	        engine = str(tot_engine_c)
	        engine_name = str(eng_name)[1:-1]
	        ulke = country_info["country"]
	        sahip = country_info["as_owner"]

	        b = a.replace('\n', ' ')
	        c = tespit.replace('\n', ' ')
	            
	        d = sahip
	        e = abuse_scor
	        f = tot_abuse_count
	        sonuc= "IP = " +str(b).replace(" ", "")+","+"Total Detect = " +c+"," + "Owner = "+d+ "," "Abuse Scor = " +str(e)+ "," "Reported = "+str(f)+" "
	        print("IP = " +str(b).replace(" ", "")+","+"Total Detect = " +c+"," + "Owner = "+d+ "," "Abuse Scor = " +str(e)+ "," "Reported = "+str(f)+" ")
	        result = open("result.txt", "a")
	        result.write(sonuc+"\n")
	        result.close()
	        time.sleep(5)
	        

elif secim == "B":
        # Seçenek B seçilirse bu kod bloğu çalışacak

	with open("vırusapi.txt", "r") as file:
  	  # Dosyadan adı oku
   	 apikey = file.read()
    
	print("""
	𝕿𝖍𝖆𝖓𝖐 𝖞𝖔𝖚 𝖋𝖔𝖗 𝖈𝖍𝖔𝖔𝖘𝖎𝖓𝖌 𝖚𝖘 <3
	""")
	
	# VirusTotal API anahtarınızı buraya girin
	#key = input('Please enter the Api key for Virus Total: ')
	#API_KEY = key
	
	file = input('please enter the file path: ')
	
	# Dosya yolunu belirtin
	file_path = file
	
	# Dosya taraması için URL'yi belirtin
	url = "https://www.virustotal.com/vtapi/v2/file/scan"
	
	print("""

	░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗██╗███╗░░██╗░██████╗░
	██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██║████╗░██║██╔════╝░
	╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║██║██╔██╗██║██║░░██╗░
	░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██║██║╚████║██║░░╚██╗
	██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║██║██║░╚███║╚██████╔╝
	╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░
                                                                 
	""")
	
	# Dosya taraması için istek yapın
	params = {"apikey": apikey}
	files = {"file": open(file_path, "rb")}
	response = requests.post(url, files=files, params=params)
	
	# Tarama sonucunu yazdırın
	barbaros=response.json()
	
	a = barbaros['scan_id']
	b = barbaros['sha1']
	c = barbaros['resource']
	d = barbaros['response_code']
	e = barbaros['sha256']
	f = barbaros['permalink']
	g = barbaros['md5']
	h = barbaros['verbose_msg']
	
	print(f"scan_id: {a}")
	print(f"sha1: {b}")
	print(f"resource: {c}")
	print(f"response_code: {d}")
	print(f"sha256: {e}")
	print(f"permalink: {f}")
	print(f"md5: {g}")
	print(f"verbose_msg: {h}")

elif secim == "C":

	with open("vırusapi.txt", "r") as file:
  	  # Dosyadan adı oku
   	 apikey = file.read()
   	 
	print("""
	𝕿𝖍𝖆𝖓𝖐 𝖞𝖔𝖚 𝖋𝖔𝖗 𝖈𝖍𝖔𝖔𝖘𝖎𝖓𝖌 𝖚𝖘 <3
	""")	
	
	url = 'https://www.virustotal.com/vtapi/v2/url/report'
	
	#key = input('Please enter the Api key for Virus Total: ')

	http = input('Url address you want to scan?: ')
	
	print("""

	░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗██╗███╗░░██╗░██████╗░
	██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██║████╗░██║██╔════╝░
	╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║██║██╔██╗██║██║░░██╗░
	░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██║██║╚████║██║░░╚██╗
	██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║██║██║░╚███║╚██████╔╝
	╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░
                                                                 
	""")

	params = {'apikey':apikey, 'resource': http}
	
	response = requests.get(url, params=params)
	
	# Tarama sonucunu yazdırın
	barbaros=response.json()
	
	a = barbaros['scans']
	b = barbaros['scan_id']
	c = barbaros['permalink']
	d = barbaros['url']
	e = barbaros['total']

	print(json.dumps(a, indent=4))
	print(f"Scan ID: {b}")
	print(f"Permalink: {c}")
	print(f"Url: {d}")
	print(f"Total: {e}")
	



else:
	print("An invalid option has been selected.")
	        

