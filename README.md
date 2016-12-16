# Run ZeroTier as a docker container
Also automatically allow this node via the API.

## Usage
```bash
docker run -d --net=host -e NETWORK=123MYNETWORKID -e ZEROTIER_TOKEN=abcMYAPITOKEN --cap-add=NET_ADMIN --cap-add=SYS_ADMIN --device=/dev/net/tun zerotier
```
