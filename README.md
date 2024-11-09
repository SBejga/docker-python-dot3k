# rpi-docker-dot3k

## Build

docker build -t docker.io/library/rpi-docker-dot3k

## Run

```
docker run --privileged --device /dev/i2c-1 --device /dev/gpiomem -v /proc/meminfo:/proc/meminfo --rm docker.io/library/rpi-docker-dot3k
```

## Credits

- dot3k examples: https://github.com/pimoroni/displayotron