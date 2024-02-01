from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuração do Selenium
driver_path = 'caminho/para/o/chromedriver.exe'  # Substitua pelo caminho do seu driver
driver = webdriver.Chrome(executable_path=driver_path)

# Página de login do Instagram
driver.get('https://www.instagram.com/accounts/login/')

# Espera o carregamento da página
time.sleep(2)

# Preenche as credenciais (substitua pelos seus dados)
username = 'seu_usuario'
password = 'sua_senha'

# Preenche as credenciais e faz login
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('password').send_keys(Keys.RETURN)

# Aguarda o login
time.sleep(5)

# Navega até a página de postagem
driver.get('https://www.instagram.com/p/criar/')  # Substitua pela URL de criação de postagem

# Aguarda o carregamento da página de postagem
time.sleep(2)

# Preenche os campos de postagem (substitua pelos seus dados)
legenda = 'Sua legenda aqui'
caminho_imagem = 'caminho/para/imagem.jpg'  # Substitua pelo caminho da sua imagem

# Carrega a imagem
input_file = driver.find_element_by_xpath('//input[@type="file"]')
input_file.send_keys(caminho_imagem)

# Adiciona a legenda
legenda_input = driver.find_element_by_xpath('//textarea[@aria-label="Legenda"]')
legenda_input.send_keys(legenda)

# Espera alguns segundos antes de postar (pode ajustar conforme necessário)
time.sleep(2)

# Clica no botão de postar
post_button = driver.find_element_by_xpath('//button[@type="submit" and contains(text(), "Postar")]')
post_button.click()

# Aguarda alguns segundos para a postagem ser realizada (pode ajustar conforme necessário)
time.sleep(5)

# Fecha o navegador
driver.quit()
