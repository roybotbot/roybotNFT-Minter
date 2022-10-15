from sys import argv
import requests
import urllib3
import json
import csv
import time

urllib3.disable_warnings()

script, mint_data = argv

headers = {'Content-Type': 'application/json'}
url = "https://localhost:9256/nft_mint_nft"
cert = ('/Users/roy/.chia/mainnet/config/ssl/wallet/private_wallet.crt', '/Users/roy/.chia/mainnet/config/ssl/wallet/private_wallet.key')

print("Minting NFTs")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")


with open(mint_data, 'r', encoding='ISO-8859-1') as file:
	csv_reader = csv.reader(file, delimiter=',')
	next(csv_reader) # skipping the first row since it's the column headers
	j=0
	for row in csv_reader:
		print("\n")
		print("Minting NFT #{}".format(j+1))
		
		data = {
			"wallet_id":row[1],
			"uris":[str(row[2]),str(row[3])],
			"hash":str(row[4]),
			"meta_uris":[str(row[5]),str(row[6])],
			"meta_hash":str(row[7]),
			"license_uris":[str(row[8]),str(row[9]),str(row[10])],
			"license_hash":str(row[11]),
			"royalty_address":str(row[12]),
			"royalty_percentage":row[13],
			"edition_number":row[14],
			"edition_count":row[15],
			"fee":row[16]
		}
		data_json = json.dumps(data)
		j+=1
		
		# TESTING: if you want to test and see if the proper JSON is created, uncomment the line below:
		# print(data_json) # But wait, there's more...
		
		# !!!!!!!
		# THEN comment out the rest of the lines below
		response = json.loads(requests.post(url, data=data_json, headers=headers, cert=cert, verify=False).text)
		print(json.dumps(response, indent=4, sort_keys=True))
		print("Waiting 75 seconds...")
		time.sleep(75)