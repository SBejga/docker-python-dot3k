# rpi-docker-dot3k

dockerized python code to show information on a raspberry pi 4 with a display-o-tron 3000 (Pimorino Dot3k)

## Raspberry Pi

Tested with a Pi 4 Model B

Requires:
- GPIO activated
- I2C activated
- container runtime (docker community edition) installed

## Build

docker build -t docker.io/library/rpi-docker-dot3k

## Run

```
docker run --privileged --device /dev/i2c-1 --device /dev/gpiomem -v /proc/meminfo:/proc/meminfo --rm docker.io/library/rpi-docker-dot3k
```

## Credits

- dot3k examples: https://github.com/pimoroni/displayotron