# Quantum Key Exchange

A dummy server, client and middleman to test xor and qubits encryption

## Tests Setup and Execution

`virtualenv -p python3.9 <environmentName>` or whatever version of python you are using <br>
`. <environmentName>/bin/activate` to create a new virtual environment <br>
`pip install pytest` to install dependancies <br>
`python -m pytest` to run all tests <br>
Use `deactivate` to exit virtual environment

## MiddleMan Attack Execution

run `python main.py`

### Todos

- Implement QKE exchange and tests
- Create MITM attack and connection
