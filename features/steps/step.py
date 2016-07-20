from selenium import webdriver
from behave import step

dicionario = {"pesquisar": "btnG"}
driver = None
id_s = None

@step('que o  navegador esteja aberto')
def abrir_navegador(context):
    global driver
    driver = webdriver.Firefox()

@step('acesso "{site}"')
def teste_site(context,site):
    driver.get(site)

@step('localizar campo de busca "{campo}"')
def campo_busca(context,campo):
    global id_s
    id_s = driver.find_element_by_id(campo)

@step('escrever "{texto}"')
def text(context,texto):
    id_s.send_keys(texto)

@step('clicar no botao "{pesquisar}"')
def teste_pesquisar(context,pesquisar):
    driver.find_element_by_name(dicionario["pesquisar"]).click()

@step('encontrar o titulo "{texto}"')
def palavra(context,texto):
    assert texto in driver.title

@step('fechar o navegador')
def fechar_navegador(context):
    driver.save_screenshot("browser.png")
    driver.close()
