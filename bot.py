#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("893774031:AAGl0ZYo7v868yF1sMKqusFccQE63voXclc")
User_bot("@JuliaRobot ") 

@bot.message_handler(commands=["frase"])
def frase_command(m):
	if m.text == '/frase' or m.text == '/frase@JuliaRobot ' or m.text == 'Julia' :
		list = ["●Eu sei moça, dói sim. Mas a gente cresce floresce e planta amor em outro alguém 🌸🍃", "A Melhor Maneira De Resolver as Coisas É Ficar  De Pé Diante Do Mundo E Ficar De Joelhos diante de Deus💕🙌🏼🌹","Paraíso é uma praia, eu e você, seus beijos e seu cafuné… 💏🌅","Lua cheia, desliga o farol, namora comigo a espera do sol… 💏🌇","Eu acabei gostando de você muito mais do que pensei. 💬","Qualquer coisa aqui, se não fosse com você, me causaria tédio 🎶","E quando o sol chegar, a gente ama de novo, a gente liga pro povo, fala que ta namorando e casa semana que vem… 💑💕","Então vem, deixa eu te mostrar, que é ao meu lado que você tem que ficar. 👫💕","Beijar já é bom, com mordidas então… 👌😍","Se der saudade, me liga! O número é o mesmo e a vontade de você também.. 😔📞","Quando se trata de você, sei lá, é diferente. 💭","Cê topa fugir daqui? Ver o nascer do sol, longe de tudo. Só eu e você.  🍃☀🌅","Me traz o seu sossego, atrasa o meu relógio, acalma a minha pressa. 👌❤️","E se eu te pedir você vem? Te dou um espacinho na minha cama só pra cê me fazer bem 💑💘😍" , "Enxergue cada dia como uma nova chance ♻️", "Se o final valer a pena, o caminho nem importa.. 🏳", " Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼 ", " Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌", "Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","Você é mais forte do que pensa e vai ser mais feliz do que imagina.", "Procure a felicidade, não a opinião dos outros 🔮🌻" , "O melhor sorriso é aquele que te faz sorrir junto. ❣", "Eu era pedra, mas você me fez flor. 🌸" , "Que minha única mania seja sorrir, e meu único vicio seja a felicidade. ✨🌺","Prefiro sorrir. Me permito ser feliz. Porque sim. Por causa mim. ✨🌼"," Eu ando sorrindo pra vida e ela sorrindo pra mim. 🔮🌻","Vai crescer porque eu não nasci pra ser tua babá. 🙅👌","E quando você ver ela sorrindo pra outro, vai entender o quanto podia ter feito ela feliz e não fez.✌️👊","Vou dar amor para quem merece. 👊🏻","Chega garota para de drama, você queria amor e ele queria cama. 👊","Você acha que vai me deixar sem juízo, mas deixa eu te contar uma coisa: eu nunca tive nenhum ✌✌","A pior perca, é a perca de tempo! ","Não vou te bloquear, nem te excluir, nem nada do tipo. Quero que você esteja presente e veja, como eu sou mais feliz sem você, babaca 😘✌️","Não valorizou? Manda o próximo da fila por favor ✌","Segue teus planos pq nos dela você não tá mais. 😗✌","Liga pra mim nessa madrugada e diz que não consegue dormir porque está sentido minha falta. 💔 ","Melhor uma sacanagem sincera do que um amor forçado.👌","Adorei a indireta que vc postou, vou até curtir pra te irritar mais. 😗✔","Vou amar quem me ama, esquecer quem não me quis, e mostrar pra quem me odeia o prazer de ser feliz. 👊💥","Bobeia pra ver que eu te faço um estrago! 👌🚼🔞","O nosso santo bateu, o amor da sua vida sou eu. Tudo que é meu hoje é seu e o fim nem precisa rimar! 🎶💑"," Paciência não é uma das minhas virtudes.","“Logo quando você acha que conhece uma pessoa, você descobre que não sabe nada sobre ela.”"," Agradar a si, não aos outros.","Procure alguém que também te procure.","Nunca desista de algo que você não consegue passar um dia sem pensar.👌","Eu tenho fé, nada me abala. Eu tô ligado, aqui se faz, aqui se paga!","To numa fase da vida que se quiser me procurar pra conversar comigo tudo bem, mas se não quiser tudo bem também, tanto faz… 🍃","Momentos felizes merecem hora extra.","“Moça de alma colorida, pintou as suas dores com tintas e plantou flores em suas feridas”.🌸💭","Se eu te chamar pra fugir comigo, onde o sol se faz de abrigo e o mar é o paraíso, você vem? ☀🌊🍃","Vem cá. Me abraça. Não precisa falar nada.","Quer se afastar? Pode ir, só não espere que eu vá atrás. 😉","• Existem coisas pelas quais devemos esperar, outras que devemos correr atrás, e outras que nem valem a pena perder tempo. 📃☀","Os melhores apertos da vida, são os abraços. 💕","A gente nunca sabe quem vem pra","Pisando na grama, roubando rosas, as melhores ideias são as perigosas 🍁","Evite amor a todo custo, esse é meu lema. 📍👌🏻  ","Ela diz que quer um cara calmo, mas caras calmos nunca chamam sua atenção 🎶🌸","Nao troque o certo, pelo duvidoso. 🌹👊💜","Nós só precisamos de nós 💞","É só chegar e beijar, elas tão loucas, dançando em cima da mesa virando um litro na boca. 👌🍸🎵 ","A casa não caiu, muito menos desabou, tô firme e forte, se fudeu quem desacreditou. 🔫👌👊🎆 ","Jeitinho reservado, talvez até meio gelado. Quem vê já cria um rótulo, mas quem conhece sabe que nada sobre ela é facilmente decifrado. 🌸❄️","Eu largo tudo hoje se você me prometer que vai me amar amanhã 🎶😍","No meu coração, que era pedra, nasceu uma flor 🌸","A arma dos fracos é criticar os fortes. A arma dos fortes é ignorar os fracos!👌☀ ","Vou rabiscar estrelas no chão pra passear no céu. 🎇⭐️","Tudo vai, tudo é fase. 🍁 ","Quis que você fosse minha âncora, mas lembrei que fui feita pra ser sereia e não navio. ⚓️🐚🌊 ","Não temer, só sorrir 💝","Tanto motivo pra beber, imagina aê, se eu vou gastar uma dose pensando em você 🎶🍻 ","Deixa ser, deixa o amor ser sua saída, deixa o mar curar a ferida, deixa o sol iluminar a sua vida! ","Com seu amor, ninguém pode me derrubar  💗","De todos os cupins, baratas, pernilongos, gafanhotos, pulgas, abelhas, moscas, ratos, formigas.. Você foi a praga mais legal que eu já conheci 💗👫","Amigos são anjos que nos deixam em pé quando nossas asas esquecem de como voar. ✨👼😍","É, eu não paro de pensar em você. 😍💭","Se eu te perder, eu me perco. 😻","Às vezes eu penso em você, e do nada vêm aquele sorriso bobo. 🙆💕💭","Tão inteligente para escrever sobre o amor e tão burra para amar…👑","Ela é daquelas mina que não tá nem aí pra sua opinião, toca tua vida, se orienta vacilão. 😏👊 ","Sejamos como o sol que não visa nenhuma recompensa, nenhum elogio, não espera lucros nem fama, simplesmente brilha. 💭 ✨ ","Joga o sorriso no ar e faça toda a noite brilhar. 😁🌙💫 ","Fazer do teu abraço um abrigo…👫💑","Boa sorte. Boa vida. E te desejo uma maré de lembranças de mim. 🌊💥","A melhor maneira de curar um coração ferido, é deixar que outra pessoa ocupe ele novamente. 🙌🏻💑❣","Existem duas maneiras de mentir, com as palavras e com os sentimentos! 💭😔","Enxergue cada dia como uma nova chance ♻️","Se o final valer a pena, o caminho nem importa.. 🏳","Para uns ela era primavera. Para outros, ela era inverno.","Se ame um pouco mais a cada dia.","Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼","Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌","É preciso paz pra poder sorrir.","Desculpe por não me importar com o que você pensa"," estou ocupada sendo feliz 😘","Me viciei na alegria 🌸","Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","O que o mundo vai dizer quando o amor vencer? 🌺📸","Sem juízo pra não causar prejuízo 💥","Que a minha única mania seja sorrir e que meu único vício seja a felicidade 🍀","Ela nao vive de meios termos, meia saudade ou meio amor. Ela gosta de transbordar ☀️","Ela quer alguém pra amar da maneira certa 💚","Não era um vazio, era só um silêncio ✉️🗯🔕","É melhor a gente seguir em frente e aceitar as coisas como são 📌","Então viva uma vida que vai se lembrar 🌠🌇","Deus e essa mania bonita de cuidar tão bem do meu coração 😍","A gratidão muda tudo ❤️","Ela não tira o sorriso do rosto nem pra passar batom, cê acha que vai tirar por você ? 💋","Quem faz o bem, conquista paz interior. 🌸","Sorria sem câmera , converse sem celular, ajude sem platéia, ame sem condições 💙","Na vida tudo é possível a mente atrai o que você pensar 💭??💛","O mal olhado não é nada, perto da Luz que me guia 🙏🏻💡","To solteira, to vivendo nem amando nem sofrendo 🙌🏻🌸","Aumente o som do seu riso, e deixe surda sua dor. 🐚","Tenho o riso frouxo pra poder aguentar esses apertos no coração 💖","Sorrir já é um recomeço 🌼🙌🏻","Vai achando que eu ainda to encanada em você ✌" , "Prefiro sorrir. Me permito ser feliz. Porque sim. Por mim. ✡","Você não navegará ao futuro enquanto estiver ancorado ao passado 🌙⚓️"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "* {} *✨ [{}](http://telegram.me/Sad_Station) \n\n☝_Esta mensagem podera Ser Repetida a qualquer momento_☝".format(m.from_user.first_name, resposta), parse_mode='Markdown')
		
		#####Apaixonado#####
		
@bot.message_handler(commands=["apaixonado"])
def apaixao(m):
	if m.text == '/apaixonado' or m.text == '/apaixonado@JuliaRobot ':
		list = ["Apaixonado (a)"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{} *Você está *{}%  *{}* ".format(m.from_user.first_name, valor, resposta), parse_mode='Markdown')
		
	#######Lindo######
	
@bot.message_handler(commands=["lindeza"])
def lindeza(m):
	if m.text == '/lindeza' or m.text == '/lindeza@JuliaRobot ':
		list = ["Lindeza (o) "]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{} *Você está com *{}%  *de* *{}* ".format(m.from_user.first_name, valor, resposta), parse_mode='Markdown')
		
#########Start
		
def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('💞 | Canal Official',
                                          url='https://telegram.me/Fakesofc'))
                                         
    return markup


@bot.message_handler(commands=['start'])
def canal_command(me):
    bot.reply_to(m,
                    '🙊 | Este Bot Foi Criador Por : @Fraviin \n\n✅| Canal Do Bot Official : @Fakesofc\n\nUser o Command /help\n\n 👇Meus Canais oficiais👇',
                    reply_markup=gen_markup())
                    
                    
#####

@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, u"""\
💞 Olá ! {} 
Para receber uma Frase você pode enviar o comando /frase

Terei prazer em ajudar você

Comandos disponíveis:

/Start - _Iniciar o Bot_
/ajuda - _envia ajuda_
/sugerir - _solicita uma sugestão_
/calificar - _votar neste bot na store_
/frase - _Frases aleatória_
/link - _envia o  link do bot_
/lindeza - _Veja o Quanto vc tem de Lindeza_
/apaixonado - _Veja o Quanto voce esta paixonado_
/lixomentro - _Veja o Quanto vc e de Lixo_
/novidades - _Novidades_
/contacto - _envia informações de contato_
/delicia - _Veja O Quanto Voce e Delicioso (a)_
/cheiro - _Veja o Quanto Voce e Cheirosa (o)_
/mais  -  _Veja Novos Bots_
/canal-  _canal do bot_
/dono - _Criador Do Bot_

OUTRO BOT CRIADO COM MESMA API DA JULIA ROBOT
@AMANDA_ROBOT 

Entre no nosso canal : https://telegram.me/Fakesofc
""".format(m.from_user.first_name), parse_mode='Markdown')
    
   ####Link####
   
@bot.message_handler(commands=['link'])
def link_command(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, " 😃 Este e o Link do Bot http://telegram.me/Amanda_Robot")
    
    ######calificar
    
    @bot.message_handler(commands=['calificar'])
def link_command(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, " Command Off-line! ")

###Atualizaçao###

@bot.message_handler(commands=['novidades'])
def updates_txt(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, " 😃  | Oque a De Novo? \n\n 😻 |  /cheiro Veja o Quanto voce esta Cheirando Hoje \n\n 💞 | /delicia Veja o Quanto o Bot ti acha Deliciosa (a) \n\n 💎 | /mais  Veja Novos Bots ")


######Delicia#####

@bot.message_handler(commands=["delicia"])
def delicia(m):
	if m.text == '/delicia' or m.text == '/delicia@JuliaRobot ':
		list = ["Deliciosa (o) "]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{} *Você e *{}%  *de* *{}* ".format(m.from_user.first_name, valor, resposta), parse_mode='Markdown')
		
#####Cheiroso###

@bot.message_handler(commands=["cheiro"])
def cheiro(m):
	if m.text == '/cheiro' or m.text == '/cheiro@JuliaRobot ':
		list = ["Cheirosa (o) "]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{} *Você e *{}%  *de* *{}* ".format(m.from_user.first_name, valor, resposta), parse_mode='Markdown')
		


###### Dono#####
@bot.message_handler(commands=['dono'])
def dono_command(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, " Canal do Criador @Fraviiu ")
    
    ###MaisBots###
    
 @bot.message_handler(commands=['mais'])
def mais_Bots(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, " 😻 | Aqui Estar Meus Projetos👇\n\n 💎 | https://t.me/Stickerdownrobot  -  *Com Esse Bot Você Mesmo Pode Estar Baixando Packs ou Unidades de Stickers*\n\n ♦ | https://t.me/FravinBot  -  *Com esse Bot Vai Ajuda Você a Gerenciar o Seu Supergroup e Dando-lhes Boas Vindas ao Grupo*\n\n🌸 | https://t.me/Amanda_Robot  -  *Amanda Ira Manda Lindas Frases ao seu Supergroup*\n\n💌 | *Forma Suas Mensagens em Links*\n\n 🌝 | https://t.me/SkSharedBot  -  *Com Esse Bot Voce Ira Divulgar Seu Canal / grupo Gratis Sem Precisa add em seu Canal ou Grupo*")

######canais###
    
    def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('▶ | Sad Station',
                                          url='https://telegram.me/Sad_Station'))
   markup.add(types.InlineKeyboardButton('💎 | Amador 69',
                                          url='https://telegram.me/amador69'))                        
   markup.add(types.InlineKeyboardButton('♦ | Tumblr',
                                          url='https://telegram.me/fakesofc'))
   markup.add(types.InlineKeyboardButton('🌝 | Canal do Criador',
                                          url='https://telegram.me/Fraviiu')) 
   markup.add(types.InlineKeyboardButton('💞 | Canal Official',
                                          url='https://telegram.me/FrasesJuliaRobot'))
                                          
    return markup


@bot.message_handler(commands=['canal'])
def canais(me):
    bot.reply_to(m,
                    'Canais Official do Bot💎',
                    reply_markup=gen_markup())
                    
      
      #####Lixo##"
      
 @bot.message_handler(commands=["lixomentro"])
def lixo(m):
	if m.text == '/lixomentro' or m.text == '/lixomentro@JuliaRobot ':
		list = ["Lixo (a) "]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{} *Você esta com *{}%  *de ser* *{}* ".format(m.from_user.first_name, valor, resposta), parse_mode='Markdown')
                    
  
  ###su
  
@bot.message_handler(commands=["sugerir"])
def sugerir(m):
	if m.text == '/sugerir' or m.text == '/sugerir@JuliaRobot ':
		list = ["Carregando..... "]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "Ola {} Voce Pode Usar o Bot @Fraviiubot Para manda Sua Sugestão ".format(m.from_user.first_name), parse_mode='Markdown')
		
		
		#####ctt
		
@bot.message_handler(commands=['contacto'])
def contacto(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, " Entra em Contato com o Criador : @Fraviin")
    
    
    ##status
    
@bot.message_handler(commands=["status"])
def status(m):
	if m.text == '/status' or m.text == '/status@JuliaRobot':
		list = ["Se De Boca Fechada Eu Incomodo Muita Gente, Imagina Se Eu Abrisse A Boca Pra Falar Umas Verdades Na Cara!😌👊💋🔥","• E foi com você que os meus sonhos em oração vieram a se transformar em futuro próximo 💍💏💒", "Minha estratégia é sempre dar mais corda, uns criam laços, outros se enforcam!😉😂", "aniversário de adolescente é uma bosta, só tem bebida e droga não tem nem pula-pula", "Não são as pessoas felizes que são gratas, as pessoas gratas que são felizes. 🙏😃", " Ame quem te ama e quem mereça seu amor😘👍"," Eu me apaixonei por suas qualidades e defeitos. Não teve jeito! 😍", "De Todas As Oportunidades Que a Vida Me Deu , A Possibilidade De Ter Você Ao Meu Lado Foi A Que Me Deixou Mais Feliz..😍", "Mais se o Mundo Êh Ah Guerra,Talvez Seu Sorriso Seja Ah Paz..'💙", " E eu ainda escolheria você, mesmo tendo todas as opções do mundo. 💜", " Meu maior medo é errar novamente dando papo de futuro pra quem é de momento..🥀", " 🍂✈☘ "Não Procure Ser O Melhor, Mas Sim O Mais Simples. Pq Até A Maior Arvore Da Floresta Começa Do Chão."🌙🚶🏻❤☘"," O seu destino só terá um final feliz, se você mesmo for o autor da própria história  ❤🍃🎒"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "[{}](telegram.me/juliaStatus)\n\n☝_Esta mensagem podera Ser Repetida a qualquer momento_☝".format(resposta), parse_mode='Markdown')
  	
  
  
bot.polling( )
