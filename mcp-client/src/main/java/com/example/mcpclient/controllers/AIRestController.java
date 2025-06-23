package com.example.mcpclient.controllers;

import com.example.mcpclient.agents.AIAgent;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AIRestController {

    private AIAgent agent;

    public AIRestController(AIAgent agent) {
        this.agent = agent;
    }
    @GetMapping("/chat")
    public String askAgent(String query) {
        return agent.askLLM(query);
    }
}
