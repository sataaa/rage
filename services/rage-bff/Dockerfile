# Stage 1: Build the application using Gradle and a JDK image
FROM gradle:8.8-jdk21 as builder

WORKDIR /usr/src/app

COPY . .
RUN gradle bootJar --info
RUN ls /usr/src/app/build
RUN ls /usr/src/app/build/libs

# Stage 2: Create the final, minimal image with a JRE to run the app
FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

COPY --from=builder /usr/src/app/build/libs/rage-bff.jar .

EXPOSE 8000

ENTRYPOINT ["java", "-jar", "rage-bff.jar"]