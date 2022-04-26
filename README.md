# Quantum Key Exchange

A dummy server, client and middleman to test xor and qubits encryption

## Tests Setup and Execution

`virtualenv -p python3.9 <environmentName>` or whatever version of python you are using <br>
`. <environmentName>/bin/activate` <br> to create a new virtual environment
`pip install pytest` <br> to install dependancies
`python -m pytest` to run all tests <br>
Use `deactivate` to exit virtual environment

## MiddleMan Attack Execution

run `python main.py`

### Todos

- Implement QKE exchange and tests
- Create MITM attack and connection
