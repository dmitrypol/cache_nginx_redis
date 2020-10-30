# we will use openjdk 8 with alpine as it is a very small linux distro
FROM openjdk:8-jre-alpine3.9

EXPOSE 8080
EXPOSE 8081

COPY target/api2-1.0-SNAPSHOT.jar /demo.jar
COPY config.yml /config.yml

# set the startup command to execute the jar
CMD ["java", "-jar", "/demo.jar", "server", "/config.yml"]