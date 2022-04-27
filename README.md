# Quantum Key Exchange

A dummy server, client and middleman to test xor and qubits encryption

## Tests Setup and Execution

To create a new virtual environment: `virtualenv -p python3.9 <environmentName>` or whatever version of python you are using <br>
To activate the environment: `. <environmentName>/bin/activate` <br>
To install dependancies: `pip install pytest`  <br>
To run all tests: `python -m pytest` <br>
Use `deactivate` to exit virtual environment

## MiddleMan Attack Execution

run `python main.py`

### Todos

- Implement QKE exchange and tests
- Create MITM attack and connection
