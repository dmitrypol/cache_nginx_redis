package io.dmitrypol;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

import io.dmitrypol.resources.HomeResource;

public class api2Application extends Application<api2Configuration> {

    public static void main(final String[] args) throws Exception {
        new api2Application().run(args);
    }

    @Override
    public String getName() {
        return "api2";
    }

    @Override
    public void initialize(final Bootstrap<api2Configuration> bootstrap) {
    }

    @Override
    public void run(final api2Configuration configuration, final Environment environment) {
        environment.jersey().register(new HomeResource());
    }

}
