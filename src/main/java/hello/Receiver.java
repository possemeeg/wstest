package hello;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jms.annotation.JmsListener;
import org.springframework.jms.core.JmsTemplate;
import org.springframework.stereotype.Component;

@Component
public class Receiver {

    private final JmsTemplate jmsTemplate;

    @Autowired
    public Receiver(JmsTemplate jmsTemplate) {
      this.jmsTemplate = jmsTemplate;
    }

    @JmsListener(destination = "mailbox", containerFactory = "myFactory")
    public void receiveMessage(Email email) {
        System.out.println("Received <" + email + ">");
        jmsTemplate.convertAndSend("topic/greetings", new Email("info@example.com", "Hello from java"));
    }

}
