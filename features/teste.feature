Feature: teste automatizado

Scenario: buscar Gas Tecnologia
        Given que o  navegador esteja aberto
        And acesso "https://www.google.com.br/"
        When localizar campo de busca "lst-ib"
        And escrever "Gas Tecnologia"
        And clicar no botao "pesquisar"
        And encontrar o titulo "Google"
        Then fechar o navegador
