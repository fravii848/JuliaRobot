#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("893774031:AAGl0ZYo7v868yF1sMKqusFccQE63voXclc")


@bot.message_handler(commands=["frase"])
def frase_command(m):
	if m.text == '/frase' or m.text == '/frase@JuliaRobot ' or m.text == 'Julia' :
		list = ["●Eu sei moça, dói sim. Mas a gente cresce floresce e planta amor em outro alguém 🌸🍃", "A Melhor Maneira De Resolver as Coisas É Ficar  De Pé Diante Do Mundo E Ficar De Joelhos diante de Deus💕🙌🏼🌹","Paraíso é uma praia, eu e você, seus beijos e seu cafuné… 💏🌅","Lua cheia, desliga o farol, namora comigo a espera do sol… 💏🌇","Eu acabei gostando de você muito mais do que pensei. 💬","Qualquer coisa aqui, se não fosse com você, me causaria tédio 🎶","E quando o sol chegar, a gente ama de novo, a gente liga pro povo, fala que ta namorando e casa semana que vem… 💑💕","Então vem, deixa eu te mostrar, que é ao meu lado que você tem que ficar. 👫💕","Beijar já é bom, com mordidas então… 👌😍","Se der saudade, me liga! O número é o mesmo e a vontade de você também.. 😔📞","Quando se trata de você, sei lá, é diferente. 💭","Cê topa fugir daqui? Ver o nascer do sol, longe de tudo. Só eu e você.  🍃☀🌅","Me traz o seu sossego, atrasa o meu relógio, acalma a minha pressa. 👌❤️","E se eu te pedir você vem? Te dou um espacinho na minha cama só pra cê me fazer bem 💑💘😍" , "Enxergue cada dia como uma nova chance ♻️", "Se o final valer a pena, o caminho nem importa.. 🏳", " Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼 ", " Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌", "Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","Você é mais forte do que pensa e vai ser mais feliz do que imagina.", "Procure a felicidade, não a opinião dos outros 🔮🌻" , "O melhor sorriso é aquele que te faz sorrir junto. ❣", "Eu era pedra, mas você me fez flor. 🌸" , "Que minha única mania seja sorrir, e meu único vicio seja a felicidade. ✨🌺","Prefiro sorrir. Me permito ser feliz. Porque sim. Por causa mim. ✨🌼"," Eu ando sorrindo pra vida e ela sorrindo pra mim. 🔮🌻","Vai crescer porque eu não nasci pra ser tua babá. 🙅👌","E quando você ver ela sorrindo pra outro, vai entender o quanto podia ter feito ela feliz e não fez.✌️👊","Vou dar amor para quem merece. 👊🏻","Chega garota para de drama, você queria amor e ele queria cama. 👊","Você acha que vai me deixar sem juízo, mas deixa eu te contar uma coisa: eu nunca tive nenhum ✌✌","A pior perca, é a perca de tempo! ","Não vou te bloquear, nem te excluir, nem nada do tipo. Quero que você esteja presente e veja, como eu sou mais feliz sem você, babaca 😘✌️","Não valorizou? Manda o próximo da fila por favor ✌","Segue teus planos pq nos dela você não tá mais. 😗✌","Liga pra mim nessa madrugada e diz que não consegue dormir porque está sentido minha falta. 💔 ","Melhor uma sacanagem sincera do que um amor forçado.👌","Adorei a indireta que vc postou, vou até curtir pra te irritar mais. 😗✔","Vou amar quem me ama, esquecer quem não me quis, e mostrar pra quem me odeia o prazer de ser feliz. 👊💥","Bobeia pra ver que eu te faço um estrago! 👌🚼🔞","O nosso santo bateu, o amor da sua vida sou eu. Tudo que é meu hoje é seu e o fim nem precisa rimar! 🎶💑"," Paciência não é uma das minhas virtudes.","“Logo quando você acha que conhece uma pessoa, você descobre que não sabe nada sobre ela.”"," Agradar a si, não aos outros.","Procure alguém que também te procure.","Nunca desista de algo que você não consegue passar um dia sem pensar.👌","Eu tenho fé, nada me abala. Eu tô ligado, aqui se faz, aqui se paga!","To numa fase da vida que se quiser me procurar pra conversar comigo tudo bem, mas se não quiser tudo bem também, tanto faz… 🍃","Momentos felizes merecem hora extra.","“Moça de alma colorida, pintou as suas dores com tintas e plantou flores em suas feridas”.🌸💭","Se eu te chamar pra fugir comigo, onde o sol se faz de abrigo e o mar é o paraíso, você vem? ☀🌊🍃","Vem cá. Me abraça. Não precisa falar nada.","Quer se afastar? Pode ir, só não espere que eu vá atrás. 😉","• Existem coisas pelas quais devemos esperar, outras que devemos correr atrás, e outras que nem valem a pena perder tempo. 📃☀","Os melhores apertos da vida, são os abraços. 💕","A gente nunca sabe quem vem pra","Pisando na grama, roubando rosas, as melhores ideias são as perigosas 🍁","Evite amor a todo custo, esse é meu lema. 📍👌🏻  ","Ela diz que quer um cara calmo, mas caras calmos nunca chamam sua atenção 🎶🌸","Nao troque o certo, pelo duvidoso. 🌹👊💜","Nós só precisamos de nós 💞","É só chegar e beijar, elas tão loucas, dançando em cima da mesa virando um litro na boca. 👌🍸🎵 ","A casa não caiu, muito menos desabou, tô firme e forte, se fudeu quem desacreditou. 🔫👌👊🎆 ","Jeitinho reservado, talvez até meio gelado. Quem vê já cria um rótulo, mas quem conhece sabe que nada sobre ela é facilmente decifrado. 🌸❄️","Eu largo tudo hoje se você me prometer que vai me amar amanhã 🎶😍","No meu coração, que era pedra, nasceu uma flor 🌸","A arma dos fracos é criticar os fortes. A arma dos fortes é ignorar os fracos!👌☀ ","Vou rabiscar estrelas no chão pra passear no céu. 🎇⭐️","Tudo vai, tudo é fase. 🍁 ","Quis que você fosse minha âncora, mas lembrei que fui feita pra ser sereia e não navio. ⚓️🐚🌊 ","Não temer, só sorrir 💝","Tanto motivo pra beber, imagina aê, se eu vou gastar uma dose pensando em você 🎶🍻 ","Deixa ser, deixa o amor ser sua saída, deixa o mar curar a ferida, deixa o sol iluminar a sua vida! ","Com seu amor, ninguém pode me derrubar  💗","De todos os cupins, baratas, pernilongos, gafanhotos, pulgas, abelhas, moscas, ratos, formigas.. Você foi a praga mais legal que eu já conheci 💗👫","Amigos são anjos que nos deixam em pé quando nossas asas esquecem de como voar. ✨👼😍","É, eu não paro de pensar em você. 😍💭","Se eu te perder, eu me perco. 😻","Às vezes eu penso em você, e do nada vêm aquele sorriso bobo. 🙆💕💭","Tão inteligente para escrever sobre o amor e tão burra para amar…👑","Ela é daquelas mina que não tá nem aí pra sua opinião, toca tua vida, se orienta vacilão. 😏👊 ","Sejamos como o sol que não visa nenhuma recompensa, nenhum elogio, não espera lucros nem fama, simplesmente brilha. 💭 ✨ ","Joga o sorriso no ar e faça toda a noite brilhar. 😁🌙💫 ","Fazer do teu abraço um abrigo…👫💑","Boa sorte. Boa vida. E te desejo uma maré de lembranças de mim. 🌊💥","A melhor maneira de curar um coração ferido, é deixar que outra pessoa ocupe ele novamente. 🙌🏻💑❣","Existem duas maneiras de mentir, com as palavras e com os sentimentos! 💭😔","Enxergue cada dia como uma nova chance ♻️","Se o final valer a pena, o caminho nem importa.. 🏳","Para uns ela era primavera. Para outros, ela era inverno.","Se ame um pouco mais a cada dia.","Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼","Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌","É preciso paz pra poder sorrir.","Desculpe por não me importar com o que você pensa"," estou ocupada sendo feliz 😘","Me viciei na alegria 🌸","Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","O que o mundo vai dizer quando o amor vencer? 🌺📸","Sem juízo pra não causar prejuízo 💥","Que a minha única mania seja sorrir e que meu único vício seja a felicidade 🍀","Ela nao vive de meios termos, meia saudade ou meio amor. Ela gosta de transbordar ☀️","Ela quer alguém pra amar da maneira certa 💚","Não era um vazio, era só um silêncio ✉️🗯🔕","É melhor a gente seguir em frente e aceitar as coisas como são 📌","Então viva uma vida que vai se lembrar 🌠🌇","Deus e essa mania bonita de cuidar tão bem do meu coração 😍","A gratidão muda tudo ❤️","Ela não tira o sorriso do rosto nem pra passar batom, cê acha que vai tirar por você ? 💋","Quem faz o bem, conquista paz interior. 🌸","Sorria sem câmera , converse sem celular, ajude sem platéia, ame sem condições 💙","Na vida tudo é possível a mente atrai o que você pensar 💭??💛","O mal olhado não é nada, perto da Luz que me guia 🙏🏻💡","To solteira, to vivendo nem amando nem sofrendo 🙌🏻🌸","Aumente o som do seu riso, e deixe surda sua dor. 🐚","Tenho o riso frouxo pra poder aguentar esses apertos no coração 💖","Sorrir já é um recomeço 🌼🙌🏻","Vai achando que eu ainda to encanada em você ✌" , "Prefiro sorrir. Me permito ser feliz. Porque sim. Por mim. ✡","Você não navegará ao futuro enquanto estiver ancorado ao passado 🌙⚓️"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "* {} *✨ [{}](https://t.me/joinchat/AAAAAFaqTfFbWe4ILHZvZw)\n\n☝_Esta mensagem podera Ser Repetida a qualquer momento_☝".format(m.from_user.first_name, resposta), parse_mode='Markdown')
		
		#####Apaixonado#####
		
@bot.message_handler(commands=["status"])
def status_command(m):
	if m.text == '/status' or m.text == '/status@JuliaRobot ' or m.text == 'Julia' :
		list = ["Enxergue cada dia como uma nova chance ♻️"," Se o final valer a pena, o caminho nem importa.. 🏳","Para uns ela era primavera. Para outros, ela era inverno.","Se ame um pouco mais a cada dia.", "Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼", "Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌", "É preciso paz pra poder sorrir.", "Desculpe por não me importar com o que você pensa, estou ocupada sendo feliz 😘", "Me viciei na alegria 🌸", "Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","O que o mundo vai dizer quando o amor vencer? 🌺📸","Sem juízo pra não causar prejuízo 💥","Que a minha única mania seja sorrir e que meu único vício seja a felicidade 🍀","Ela nao vive de meios termos, meia saudade ou meio amor. Ela gosta de transbordar ☀️","Ela quer alguém pra amar da maneira certa 💚", "Não era um vazio, era só um silêncio ✉️🗯🔕", "É melhor a gente seguir em frente e aceitar as coisas como são 📌", "Então viva uma vida que vai se lembrar 🌠🌇", "Deus e essa mania bonita de cuidar tão bem do meu coração 😍", "A gratidão muda tudo ❤️", "Ela não tira o sorriso do rosto nem pra passar batom, cê acha que vai tirar por você ? 💋", "Quem faz o bem, conquista paz interior. 🌸", "Sorria sem câmera , converse sem celular, ajude sem platéia, ame sem condições 💙", "Na vida tudo é possível a mente atrai o que você pensar 💭🌟💛", "O mal olhado não é nada, perto da Luz que me guia 🙏🏻💡", "To solteira, to vivendo nem amando nem sofrendo 🙌🏻🌸", "Aumente o som do seu riso, e deixe surda sua dor. 🐚", "Tenho o riso frouxo pra poder aguentar esses apertos no coração 💖", "Sorrir já é um recomeço 🌼🙌🏻", "Vai achando que eu ainda to encanada em você ✌", "Prefiro sorrir. Me permito ser feliz. Porque sim. Por mim. ✡", "Você não navegará ao futuro enquanto estiver ancorado ao passado 🌙⚓️", "É loucura odiar todas as rosas, porque uma te espetou. 🌹", "Prefiro sorrir. Me permito ser feliz. Porque sim. Por mim. ✡", "E de repente virou uma disputa de quem era mais frio, e o amor, morreu congelado. ❄️", "Roubar você pra mim é um crime que compensa. 💕", "Faça o certo, não o fácil. ✨", "Nunca se arrependa. Se foi bom, é maravilhoso. Se foi ruim é experiência… 💭", "Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo. 🌌", "Aquela paz que você só encontra em uma pessoa.. 💞", "Adoro fazer as pessoas sorrirem, mesmo eu não estando bem.", "As tuas dores, menina, não podem ser maiores do que a tua esperança.", "Você é o meu melhor momento, meu barulho, meu silêncio.. Você é o meu melhor lugar. 💓", "Não olhe pra trás. Não tem nada lá esperando por você.", "Queria um abraço teu, daqueles que a gente não fala nada, só sente…", "Nem todos os dias eu tenho vontade de rir, de conversar e de levar tudo na brincadeira.. 💬", "Ás vezes pra encontrar a paz, temos que perder o juízo. 🌈", "Mas é que o amor meu caro, faz a gente ver arco-íris em céu nublado. 💘💭", "Ela é brava como uma fera, mas o coração é cheio de amor. 💗", "Em um mundo onde só dão pedaços, eu insisto em procurar por inteiros… 💗💭", "Não demonstrar, não significa não sentir. 💭", "Por que você não sai um pouquinho da minha cabeça e vai passear? 👌", "Felicidade é quando a sua liberdade te preenche. 🌸🔮", "Seja o que for, sou mais o amor. 🌸", "Deixe ir. Se voltar, mande a merda. 👍", "Sorria sem câmera , converse sem celular, ajude sem platéia, ame sem condições. 💙", "O mundo não dá voltas em vão. 🍃", "Moço, ninguém é de ferro. Somos programados pra cair. 🍃", "Se o amor me rejeita, a farra me aceita. 🍻❤", "Manter a cabeça no lugar e não me abalar com besteira. 🌌", "Somos feitos de memórias que nem sempre foram vividas. 🍃", "E da vida só quero aquilo que é bonito, sincero e faz rir. 🌻"," Você fica quieto. Enquanto acontece uma guerra dentro de você."," Sou exigente com a beleza: ela tem que vir de dentro."," Por fora já desistiu. Por dentro sempre descobre algum motivo para recomeçar. 🌼🌻"," Riso solto, alma leve. 🍃"," Estou bem moço. Só preciso me acostumar com essa bagunça sentimental.🌸"," Tudo bem desmoronar por uns tempos. Não tem problema admitir que machuca. 🍃"," Você é uma daquelas chances boas que a vida não me daria duas vezes. ❤"," Meu riso é tão feliz contigo. ❤"," Amores fracos não merecem o meu tempo. 🌀🎶"," Ela aprendeu que todo amor pode acabar, menos o próprio. 💁"," Desapegue do passado e deixe o futuro te surpreender. 💥👊"," Ela é um poço de qualidade e defeito, e cada jeito dela é uma emoção. 🎶","Meu olho brilhava em cada palavra que você falava. ✨"," Porque eu te amo todos os dias, cada vez mais. Você foi minha vida, e eu fui apenas, um capítulo da sua."," A única forma de chegar ao impossível é acreditar que é possível. 👊"," A vida é uma grande, uma gigantesca confusão. Mas essa é também a beleza dela."," Se você virou a página, eu queimei o livro."," Deixe que vá. Quem desvaloriza o seu coração certamente não merece ficar.💭🌸"," Esquece e segue em frente, o tempo já é outro e eu também tô diferente. 😉"," Se ele não muda, mude-se dele. 🌸"," Ela cansou de se importar, agora ela faz por ela, e quem não curtir pode se retirar."," Andei por ai e me vi apaixonada pelas voltas que a vida dá… 🔄💖"," Quando lembrar de mim, de nós, lembra que não foi por minha vontade acabar assim. 💔"," Se você vai tentar, vá até o fim, caso contrário, nem comece."," Enxergue cada dia como uma nova chance. ♻️"," Tudo nessa vida tem uma razão pra acontecer."," Então ela sorriu… Porque sua felicidade dependia dela mesma e de mais ninguém.😄"," Fazia o possível e impossível pra te ver bem, o teu sorriso valia o meu também. 💛🔐"," Em um mundo onde só dão pedaços, eu insisto em procurar por inteiros…"," Ela é uma equação complexa. Não é o 2+2 que você tá acostumado. ❄🌼","Ela é a liberdade. Não se arrisque em prendê-la. 👽🌸"," Não sei ao certo, porém queria ele por perto. 💛"," Aquela coisa que nunca começou, nunca terminou mas nunca deixou de confundir sua mente. 😖👌"," As decepções fazem você abrir os olhos e fechar o seu coração. 🙍💔"," Erros podem ser perdoados. Atitudes podem ser repensadas. Mas algumas palavras poderão nunca ser esquecidas. ✨👊"," Não tenha medo de trocar o roteiro, você só descobre novos caminhos quando muda a direção!🍂"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, " [{}](https://t.me/joinchat/AAAAAFaqTfFbWe4ILHZvZw) \n\n[Compartilhar no WhatsApp](https://api.whatsapp.com/send?text={}) \n\n☝_Esta mensagem podera Ser Repetida a qualquer momento_☝".format(resposta), parse_mode='Markdown')
		
		
#########Start
		
def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('💞 | Canal Official',
                                          url='https://telegram.me/Fakesofc'))
    markup.add(types.InlineKeyboardButton('▶ | Sad Station',
                                          url='https://telegram.me/Sad_Station'))

    return markup


@bot.message_handler(commands=['start'])
def canal_command(m):
    bot.reply_to(m,
                    '🙊 | Este Bot Foi Criador Por : @Fraviin \n\n✅| Canal Do Bot Official : @Fakesofc\n\n 👇Meus Canais oficiais👇',
                    reply_markup=gen_markup())
                    
                    
#####
  	
  
  
bot.polling( )