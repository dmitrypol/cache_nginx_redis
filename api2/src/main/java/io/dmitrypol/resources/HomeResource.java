package io.dmitrypol.resources;

import com.codahale.metrics.annotation.Timed;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

import io.lettuce.core.RedisClient;
import io.lettuce.core.api.StatefulRedisConnection;
import io.lettuce.core.api.sync.RedisCommands;

@Produces(MediaType.APPLICATION_JSON)
@Path("/")
public class HomeResource {

    private static final String REDIS_CONNECTION_STRING = "redis://@" + System.getenv().getOrDefault("REDIS_HOST", "localhost") + ":6379/2";
    RedisClient redisClient = RedisClient.create(REDIS_CONNECTION_STRING);
    StatefulRedisConnection<String, String> connection = redisClient.connect();
    RedisCommands<String, String> lettuceSync = connection.sync();

    @GET
    @Timed
    @Path("/")
    public String root() {
        String key = "root";
        String tmp = lettuceSync.get(key);
        if (tmp == null) {
            try { Thread.sleep(5000); }
            catch(InterruptedException e) { System.out.println(e); }
            String value = "api2";
            Long seconds = 60L;
            lettuceSync.setex(key, seconds, value);
            tmp = value;
        }
        return tmp;
    }

}
