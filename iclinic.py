from selenium import webdriver
from time import sleep


# dados de preenchimento de formulários
username = "marimoara@gmail.com"
password = "abcd1234"
paciente = "Nome do Paciente"
celular = "1111111111"

# iniciar Chrome driver
driver = webdriver.Chrome("chromedriver")

# abrir a pagina do iclinic
driver.get("http://app.iclinic.com.br/new/usuarios/login")

# entrar com o username
driver.find_element_by_id("email").send_keys(username)

# entrar com o password
driver.find_element_by_id("password").send_keys(password)

# clicar para fazer login
driver.find_element_by_xpath('//*[@id="webapp-root"]/div[2]/div[1]/div/div/div[2]/form/button/span[1]').click()

# aguardar a pagina carregar
sleep(5)

#navegar para a pagina da agenda
driver.find_element_by_link_text('Agenda').click()

# aguardar a pagina carregar
sleep(5)

# clicar para iniciar um novo agendamento
driver.find_element_by_css_selector('.jss11 > .jss9').click()

#preenchimento de dados mandatórios do paciente
#preenche nome do paciente
driver.find_element_by_name('patient_name').send_keys(paciente)
#preenche celular do paciente
driver.find_element_by_name('patient_mobile_phone').send_keys(celular)
#clica para escolher o convenio particular
driver.find_element_by_css_selector('.domain-icon > .filter-option').click()
driver.find_element_by_xpath('//*[@id="bs-select-2-1"]').click()
#clica para confirmar
driver.find_element_by_css_selector('.btn-green > span > span').click()


# tempo para ver se criou o agendamento
sleep(10)

driver.quit()
