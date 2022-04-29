# Quantum Key Exchange

A dummy server, client and middleman to test xor and qubits encryption

## Tests Setup and Execution

To create a new virtual environment: `virtualenv -p python3.9 <environmentName>` or whatever version of python you are using <br>
To activate the environment: `. <environmentName>/bin/activate` <br>
To install dependancies: `pip install pytest`  <br>
To run all tests: `python -m pytest` <br>
Use `deactivate` to exit virtual environment

#### All 5 tests will pass:
- XOR unit test
- Qubit unit test
- QKE test where client sends data to the server (at qubit lengths 16, 256 and 1024)

## MiddleMan Attack Execution

Enter the virtual environment <br>
Run `python main.py`

The keys for the server, client and middleman will be displayed.

The client's sent message and the recieved messages for the middleman and server will be displayed.

The XOR encryption happens before the UTF-8 encoding, so sometimes the middleman and client are unable to decode the UTF-8 encoding (as it has been corrupted). In these cases the error `Cannot decode UTF-8` will appear and the corrupted UTF8 encoding will be displayed.