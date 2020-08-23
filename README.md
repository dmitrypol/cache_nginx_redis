# Setup

```
docker-compose up --build -d
```

* Nginx cache - http://localhost/
* Redis - cache http://localhost:5000/


# Perf benchmark

* Compile https://github.com/wg/wrk

```
# nginx cache
./wrk http://localhost/
Running 10s test @ http://localhost/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.38ms   12.61ms  71.50ms   61.52%
    Req/Sec   215.34     67.65   383.00     64.00%
  4293 requests in 10.01s, 779.60KB read
Requests/sec:    428.75
Transfer/sec:     77.86KB

# redis cache
./wrk http://localhost:5000/
Running 10s test @ http://localhost:5000/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.27ms   51.33ms 472.13ms   96.54%
    Req/Sec    87.61     14.73   131.00     83.94%
  1704 requests in 10.04s, 259.61KB read
Requests/sec:    169.76
Transfer/sec:     25.86KB
```

# Nginx

* https://docs.nginx.com/nginx/admin-guide/content-cache/content-caching/

To view cache content browse to `tmp/cache` folder.


# Redis

* https://redis.io/

Use `redis-cli` to view cache content