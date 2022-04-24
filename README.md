# Quantum Key Exchange
A dummy server, client and middleman to test xor and qubits encryption
## Tests Setup and Execution

`virtualenv -p python3.9 <environmentName>` or whatever version of python you are using <br>
`. <environmentName>/bin/activate` <br> to create a new virtual environment
`pip install pytest` <br> to install dependancies
`python -m pytest` to run all tests
Use `deactivate` to exit virtual environment

### Todos

- Fix dummy server and client (TCP or nodes?)
- Write and QKE algorithm
- Create MITM attack
