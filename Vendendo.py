from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib
import pyautogui

#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get('https://web.whatsapp.com/')
#time.sleep(15)

def info_trampo():
    vaga = input('Digite o nome da vaga:')
    candidato = input('Digite o nome do candidato:')   
    numero_candidato = int(input('Digite o número do candidato ( com código nacional, DD e número tudo junto): '))
    data = input('Digite a data: ')
    horario = input('Digite o horário da entrevista: ')
    local = input('Digite o local da entrevista: ')

    def entrevista():
        respostas = ['sim', 'claro', 'com certeza' , 's']
        saudação = str(f'Olá, candidato(a), bem-vindo(a), analisamos seu curriculo e você foi selecionado(a) para a entrevista')
        resposta1 = input(f'Você têm experiência na vaga de {vaga} ?')
        resposta2 = input(f'Você deseja participar do processo seletivo?').lower()
        
        if resposta1 == respostas:
            tempo_de_experiencia = str(input('Quanto tempo ?'))
            
            if resposta2 == respostas:
                conversa2 = str('Iremos agendar a entrevista')
                
                def agendando():
                    marcando = str(f'A entrevista será às ' +{horario}+ ' no dia ' +{data}+ ' no endereço ' +{local})
            
            else:
                não_quis = str('Muito obrigado')
        else:
            sem_interesse = str('Muito obrigado, não iremos continuar com a sua candidatura')
    
    def agendando():
        marcando = str(f'A entrevista será às ' +{horario}+ ' no dia ' +{data}+ ' no endereço ' +{local})

    

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements_by_id('side')) < 1:
  time.sleep(1)

numw =  [5511988016162]

for enviar in numw:
    
    texto = urllib.parse.quote(mensagem)
    
    time.sleep(3)
    
    link = f'https://web.whatsapp.com/send?phone={enviar}&text={texto}'
    
    navegador.get(link)
    
    time.sleep(15)

    pyautogui.moveTo(1015, 669)
    time.sleep(15)
    pyautogui.click()
    
    time.sleep(15)
    
    navegador.find_element_by_css_selector("span[data-icon = 'clip']").click()
    
    attach = navegador.find_element_by_css_selector("span[[type = 'file']").click
    
    attach.send_keys(imagem)

    anexar = navegador.find_element_by_css_selector("span[data-testid = 'send']")

    anexar.click()
    
    time.sleep(3)
    
    while len(navegador.find_elements_by_id('side')) < 1:
        
        time.sleep(1)
    time.sleep(10)
  
    








#Funcao que pesquisa o Contato / Grupo
#def  buscar_contato(contato):
    #campo_pesquisa = driver.find_element_by_xpath('// div [contains (@class, "copyable-text selectable-text")]')
    #time.sleep(2)
    #campo_pesquisa.click()
    #campo_pesquisa.send_keys(contatos)
    #campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia uma mensagem
#def  enviar_mensagem(mensagem,mensagem2):
    #campo_mensagem = driver.find_elements_by_xpath('// div [contains (@class, "copyable-text selectable-text")]')
    #campo_mensagem[1].click()
    #time.sleep(3)
    #campo_mensagem[1].send_keys(str(mensagem) + str(contato) + str(mensagem2))
    #campo_mensagem[1].send_keys(Keys.ENTER)

#Funcao que envia midia como mensagem
#def  enviar_midia(imagem):
    #driver.find_element_by_css_selector( "span [data-icon = 'clip']").click()
    #attach = driver.find_element_by_css_selector("input [type = 'file']")
    #attach.send_keys(imagem)
    #time.sleep(3)
    #enviar = driver.find_element_by_css_selector("span [data-icon = 'send']")
    #enviar.click()    

#Percorre todos os contatos / Grupos e envia como mensagens
#for contato in contatos :
    #buscar_contato(contato)
    #enviar_mensagem(mensagem,mensagem2)       
    #enviar_midia(imagem)
    #time.sleep(1)