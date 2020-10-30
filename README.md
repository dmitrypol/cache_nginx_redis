# Setup

* Install Docker Compose https://docs.docker.com/compose/install/
* Install Apache Maven https://maven.apache.org/install.html

```
mvn clean install
docker-compose up --build -d
```

api1 is built using Python Flask and api2 uses Java Dropwizard.  To start api2 oustide the container `cd api2` and `java -jar target/api2-1.0-SNAPSHOT.jar server config.yml`.  Check that it's is running via `http://localhost:8080` and `http://localhost:8081/healthcheck`.  


* Nginx cache - http://localhost/api1
* Redis - cache http://localhost:5001/


# Perf benchmark

* Compile https://github.com/wg/wrk

```
# nginx cache
./wrk http://localhost/api1
Running 10s test @ http://localhost/api1
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.38ms   12.61ms  71.50ms   61.52%
    Req/Sec   215.34     67.65   383.00     64.00%
  4293 requests in 10.01s, 779.60KB read
Requests/sec:    428.75
Transfer/sec:     77.86KB

# redis cache
./wrk http://localhost:5001/
Running 10s test @ http://localhost:5001/
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