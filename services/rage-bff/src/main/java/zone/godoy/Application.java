package zone.godoy;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import java.time.LocalDateTime;

@SpringBootApplication
@EnableScheduling
public class Application {

    public static void main(String[] args) {
        System.out.println("Starting java rage-bff service...");
        SpringApplication.run(Application.class, args);
    }

    @Scheduled(fixedDelay = 60000)
    public void printKeepAliveMessage() {
        System.out.println("java rage-bff running " + LocalDateTime.now());
    }
}