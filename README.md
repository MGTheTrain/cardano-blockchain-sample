# cardano-blockchain-sample

## Table of Contents

+ [Summary](#summary)
+ [References](#references)
+ [How to use](#how-to-use)

## Summary

Sample repository demonstrating how to operate on Cardano nodes and Cardano wallets.

## References

### Cardano basics (e.g. cardano-node and cardano-wallet)

- [Python cardano-tools pip package](https://pypi.org/project/cardano-tools/)
- [Cardano Python Module quickstart](https://cardano-python.readthedocs.io/en/latest/quickstart.html)
- [cardano-wallet](https://github.com/cardano-foundation/cardano-wallet/tree/master)
- [Getting started with Cardano testnets](https://docs.cardano.org/cardano-testnet/getting-started/#:~:text=To%20get%20started%20and%20join,ada%20to%20test%20your%20transactions.)
- [The official Cardano Environment configuration files](https://book.world.dev.cardano.org/environments.html#vasil-dev)

### Deploying smart contracts to Cardano blockchain

- [Smart Contracts](https://developers.cardano.org/docs/smart-contracts/)
- [Plutus Pioneer Program - Part 2: How to “deploy” a Smart Contract in Cardano](https://www.essentialcardano.io/article/plutus-pioneer-program-part-2-how-to-deploy-a-smart-contract-in-cardano)

## How to use

### Ramp up the docker-compose cluster containing the cardano-node container and cardano-wallet container

Refer to [`Quickstart` section here](https://github.com/cardano-foundation/cardano-wallet/tree/master). Ramp up the docker-compose and select one of the  Cardano Environment:

```sh
# On Unix systems or on Windows OS 10 with Git Bash or WSL
NETWORK=preview docker-compose up -d --build # Preview Testnet (preferred for development)
NETWORK=preprod docker-compose up -d --build # Pre-Production Testnet
NETWORK=mainnet docker-compose up -d --build # Production (Mainnet)
# This will start up the Cardano node and wallet applications and connect to the specified network (mainnet, preview, preprod)
```

### Execute commands within a running container interactively

```sh
# On Windows OS with Git Bash
winpty.exe docker exec -it <cardano-wallet or cardano-node container id> sh
# On Unix systems
docker exec -it <cardano-wallet or cardano-node container id> sh
```

### Test connection to the cardano-wallet

```sh
# with curl
curl http://localhost:8090/v2/network/information
# with cli in cardano-wallet container
docker run --network host --rm cardanofoundation/cardano-wallet network information

# Wallet operations
docker run --network host --rm cardanofoundation/cardano-wallet wallet list
docker run --network host --rm cardanofoundation/cardano-wallet wallet delete <wallet id>
```

### Run Python sample app interfacing with the Cardano wallet

Execute sample app:

```sh
cd cardano-wallet-app
pip install -r requirements.txt
python main.py
```

Execute sample app in a docker container:

```sh
cd cardano-wallet-app
docker build -t python-cardano-sample-app:stable . # Build docker image
docker run --network host --rm python-cardano-sample-app:stable sh "python main.py" # Run a container
```

### Compile Python smart contract

Compile contract:

```sh
cd cardano-smart-contract
pip install -r requirements.txt
opshin build contract.py
```

Compile contract in a docker container:

```sh
cd cardano-smart-contract
docker build -t python-cardano-sample-smart-contract:stable . # Build docker image
docker run --rm -v $(pwd)/contract/:/app/contract/ python-cardano-sample-smart-contract:stable # Run a container
```

Smart contracts need to be deployed to the Cardano blockchain. See [Plutus Pioneer Program - Part 2: How to “deploy” a Smart Contract in Cardano](https://www.essentialcardano.io/article/plutus-pioneer-program-part-2-how-to-deploy-a-smart-contract-in-cardano).

Copilot: *Smart contracts are self-executing contracts with the terms of the agreement between buyer and seller being directly written into lines of code. They are stored on a blockchain network and automatically execute when certain conditions are met. Here are some examples of smart contract use cases:*
- *Finance: Smart contracts can be used for trading, investing, lending, and borrowing*
- *Healthcare: Smart contracts can be used to store and share medical records securely and efficiently*
- *Gaming: Smart contracts can be used to create decentralized gaming platforms that allow players to earn cryptocurrency rewards* 
- *Real Estate: Smart contracts can be used to automate the process of buying and selling real estate, reducing the need for intermediaries*
- *Legal Industry: Smart contracts can be used to automate legal agreements, such as wills and trusts*

### Clear docker resources

```sh
docker rm -f $(docker ps -qa)
docker system prune --volumes --force
```
