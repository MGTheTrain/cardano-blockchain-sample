# python-cardano-blockchain-sample

## Table of Contents

+ [Summary](#summary)
+ [References](#references)
+ [How to use](#how-to-use)

## Summary

Sample repository demonstrating how to utilize the Cardano blockchain in order to write smart contracts

## References

- [Python cardano-tools pip package](https://pypi.org/project/cardano-tools/)
- [cardano-wallet](https://github.com/cardano-foundation/cardano-wallet/tree/master)
- [Getting started with Cardano testnets](https://docs.cardano.org/cardano-testnet/getting-started/#:~:text=To%20get%20started%20and%20join,ada%20to%20test%20your%20transactions.)
- [The official Cardano Environment configuration files](https://book.world.dev.cardano.org/environments.html#vasil-dev)

## How to use

### Ramp up the docker-compose cluster containing the cardano-node container and cardano-wallet container

Refer to [`Quickstart` section here](https://github.com/cardano-foundation/cardano-wallet/tree/master). Ramp up the docker-compose:

```sh
# On Unix systems or on Windows OS 10 with Git Bash or WSL
NETWORK=mainnet docker-compose up
```

Test connection to the cardano-wallet:

```sh
# with curl
curl http://localhost:8090/v2/network/information
# with cli in cardano-wallet container
docker run --network host --rm cardanofoundation/cardano-wallet network information
```
