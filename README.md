# python-cardano-blockchain-sample

## Table of Contents

+ [Summary](#summary)
+ [References](#references)
+ [How to use](#how-to-use)

## Summary

Sample repository demonstrating how to utilize the Cardano blockchain in order to write smart contracts

## References

- [Python cardano-tools pip package](https://pypi.org/project/cardano-tools/)
- [Cardano Python Module quickstart](https://cardano-python.readthedocs.io/en/latest/quickstart.html)
- [cardano-wallet](https://github.com/cardano-foundation/cardano-wallet/tree/master)
- [Getting started with Cardano testnets](https://docs.cardano.org/cardano-testnet/getting-started/#:~:text=To%20get%20started%20and%20join,ada%20to%20test%20your%20transactions.)
- [The official Cardano Environment configuration files](https://book.world.dev.cardano.org/environments.html#vasil-dev)

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
cd app
pip install -r requirements.txt
python main.py
```

Execute sample app in a docker container:

```sh
cd app
docker build -t python-cardano-sample-app:stable . # Build docker image
docker run --network host --rm python-cardano-sample-app:stable /bin/sh -c "python main.py" # Run a container
```

### Clear docker resources

```sh
docker rm -f $(docker ps -qa)
docker system prune --volumes --force
```
