package zone.godoy;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import java.time.LocalDateTime;
import lombok.extern.slf4j.Slf4j;

@SpringBootApplication
@EnableScheduling
@Slf4j
public class Application {

    public static void main(String[] args) {
        log.info("Starting java rage-bff service...");
        SpringApplication.run(Application.class, args);
    }

    @Scheduled(fixedDelay = 60000)
    public void printKeepAliveMessage() {
        log.info("java rage-bff running {}", LocalDateTime.now());
    }
}