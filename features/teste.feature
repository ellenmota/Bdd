Feature: teste automatizado


Scenario: pesquisar "Cartão" no site
        Given que o navegador esteja aberto
        And encontrar o site "http://ellenmotatutoriais.com/"
        When encontrar o campo de pesquisa "pesquisa"
        And digitar "cartao"
        And clicar no botao "buscar"
        Then deve encontrar a palavra "cartao"
        And fechar o navegador
