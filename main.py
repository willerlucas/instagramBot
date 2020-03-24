# necessário ter o geckodriver instalado e adicionado ao Path em variaveis de ambientes (para firefox)
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import random


class InstagramBot:
    def __init__(self, username, password):
        # Login
        print("abrindo firefox")
        self.driver = webdriver.Firefox()
        print("abrindo site")
        self.driver.get("https://instagram.com")
        print("Realizando login")
        sleep(5)
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        # Close Pop-Up
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Agora não')]").click()

    def TagSearch(self, tag):
        # abre o explorador na tag desejada
        try:
            print("Realizando pesquisa por "+str(tag))
            self.driver.get("https://www.instagram.com/explore/tags/"+tag+"/")
            MyBot.Wait()
        except:
            print("erro ao procurar pela tag")

    def Like(self, posts):
        # sortear uma foto para abrir
        linha = random.randint(1,3)
        coluna = random.randint(1,3)
        print("abrindo a foto: ",linha,coluna)
        print("Abrindo foto")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div["+str(linha)+"]/div["+str(coluna)+"]").click()

        #MyBot.Wait()
        sleep(random.random()*10)
        # like
        for x in range(posts):
         

            try:
            	#botão (coração) do post
                like = self.driver.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                MyBot.Wait()
                #botão seguir
                #follow = self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
                # MyBot.Wait()

                #pular quantidade aletória de postagens para evitar bloqueio por spam
                passNumb = MyBot.RandomNext()
                print("passei")
                for x in range(passNumb):
                    print("passando "+str(passNumb))
                    self.driver.find_element_by_xpath(
                        "//a[text()=\"Próximo\"]").click()
                    MyBot.Wait()

            except:
                self.driver.find_element_by_xpath(
                    "//a[text()=\"Próximo\"]").click()

    #funcao para aguardar intervalo aletório entre uma ação e outra para evitar bloqueio por spam
    def Wait(self):
        time = random.random()*50
        print("Esperando "+str(time) + " segundos")
        sleep(time)

    #função criada para retornar numero aleatório de posts a serem pulados
    def RandomNext(self):
        numb = random.randint(1, 5)
        return numb

#INPUTS
#INPUTS
#INPUTS
#INPUTS

username = input("Username: ")
password = input("Password: ")

qntTags = input("Quantidade de tags: ")
while True:
    try:
        qntTags = int(qntTags)
        break
    except:
        qntTags = input("A Quantidade de tags deve ser um valor númerico inteiro: ")


qntPosts = input("Quantidade de likes por tag: ")
while True:
    try:
        qntPosts = int(qntPosts)
        break

    except:
        qntPosts = input("A Quantidade de posts deve ser um valor númerico inteiro: ")	

tagList = []
for x in range(qntTags):
    tag = input("Insira a tag "+str(x+1)+": ")
    tagList.append(tag)

MyBot = InstagramBot(username, password)
for x in tagList:
    MyBot.TagSearch(x)
    MyBot.Like(qntPosts)