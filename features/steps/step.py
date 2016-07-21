from selenium import webdriver
from behave import step

driver = None
id_d = None

dicionario = {
"pesquisa":"s",
"buscar":"submit"
}
@step('que o navegador esteja aberto')
def testar_navegador(context):
    global driver
    driver = webdriver.Firefox()

@step('encontrar o site "{endereco}"')
def entrada_endereco(context,endereco):
    driver.get(endereco)

@step('encontrar o campo de pesquisa "{pesquisa}"')
def testar_campo(context,pesquisa):
    global id_d
    id_d = driver.find_element_by_name(dicionario["pesquisa"])

@step('digitar "{texto}"')
def testar_digitacao(context,texto):
    id_d.send_keys(texto)

@step('clicar no botao "{buscar}"')
def testar_botao(context,buscar):
    id_d = driver.find_element_by_name(dicionario["buscar"]).click()

@step('deve encontrar a palavra "{texto}"')
def achar_palavra(context,texto):
    assert texto in driver.title

@step('fechar o navegador')
def fechar_nav(context):
    driver.close()
