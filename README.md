# roybotNFT-Minter
Chia NFT minting script using RPC and data from a CSV file.

This script can be used to mint NFTs with multiple URIs. All the scripts I have seen so far mint with only one URI.

## How to Use
1. Generate your image, metadata, and license files. 
	- For metadata generation, I used this handy script from: https://github.com/zakhikhan/chia-nft-minting-helper
2. Upload them to nft.storage and ardrive.io. 
	- Make sure you get the CID for nft.storage and/or for ardrive create a manifest. This will allow you to have the same base URL and append the filename to the end to get the URI for the asset. This means you can generate all the URIs quickly in a spreadsheet program.
3. Generate the hashes for all the files. I just used a CLI command to generate them as a list in a txt file.
4. Put all the URIs, hashes, and other info into the TEMPLATE csv file and rename it to `rpc_mint_data.csv`
5. Test the script out first on testnet
6. Run with `python mint-rpc.py rpc_mint_data.csv`

If you have questions, ask me on [Twitter @roybotNFT](https://twitter.com/roybotNFT).

roybot NFTs: [https://roybot.io/nft/](https://roybot.io/nft/)
