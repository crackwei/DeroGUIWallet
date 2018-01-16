# DERO GUI Wallet

This is a fork of the Sumokoin GUI Wallet: https://github.com/sumoprojects/SumoGUIWallet adopted to work with Dero binaries.

You can download Windows binaries from https://github.com/drigler/DeroGUIWallet/releases/download/v0.0.1/DeroWallet-Win64_v0.0.1.zip, extract it somewhere on you pc and run DeroWallet.exe.

Zipped release is prepacked with Dero v0.11.2 binaries. If you have any doubt, download the official release from https://github.com/deroproject/dero/releases/download/v0.11.2/dero-windows-amd64.zip and put the binary files into 'Resources/bin' sub-directory.

For non Windows users, or users who want to run from source:

1. Install dependencies (with Python 2.7):

	* Generally, you can use Python `pip` to install required components:
		
			pip install PySide, requests, psutil
	
	* or
			
			pip install -r requirements.txt 
	
	* On some OSes, PySide may be required to install from pre-built packages. For example, on Ubuntu 16.04, install PySide with the following command:
			
			sudo apt install python-pyside


2. Build/download Dero binaries from https://github.com/deroproject/dero and put it to `Resources/bin` sub-directory.

3. Run the wallet (Python 2.7):
		
		cd /path/to/DeroGUIWallet
		python wallet.py

4. Contribution

	If you want to help out, feel free to contact me.
