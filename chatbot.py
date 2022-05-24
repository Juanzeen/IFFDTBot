from email import message
from pickletools import int4
import telebot

api_Key = "5379247247:AAFyoE6TC-VxdTiMsY--_S49BGCp7fUzp50" 
bot = telebot.TeleBot(api_Key)


@bot.message_handler(commands=["1"])
def op1(msg):
    txt = """Eu sou um bot feito com a linguagem de programação Python, fui desenvolvido para mostrar uma das milhões de coisas possíveis de se fazer com a programação. Ainda sou bem compacto, mas me aguardem no futuro, ainda vou dominar toda a espécie humana 👾☠🤬
    
    Aperte no /menu para voltar as opções iniciais ou digite qualquer coisa"""
    bot.send_message(msg.chat.id,txt)

@bot.message_handler(commands=["Programacao"])
def ansP(msg):
    bot.send_message(msg.chat.id,"Se você curtiu os projetos com programação tente descobrir mais sobre essa área, o IFF vai te dar uma base sólida para se aventurar sobre as diversas linguagens de programação que existem! Aproveita esse conhecimento todo e investe numa carreira de dev 😎\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["Arduino"])
def ansArd(msg):
    bot.send_message(msg.chat.id,"Então você é o carinha da eletrônica? Essa área é incrível e o arduino é um dos primeiros componentes que você terá contato, mas com curiosidade e disposição você pode se aventurar muito mais e desenvolver até mesmo robôs, só toma cuidado pra não explodir tudo 🤯\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["Arte"])
def ansArt(msg):
    bot.send_message(msg.chat.id,"Já que você gostou do lado artístico da feira, explore ainda mais essa área com inspirações na internet e também tente frequentar o maker, habilidades artísticas tem um ótimo relacionamento com a tecnologia! 😉\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["Hard"])
def ansHard(msg):
    bot.send_message(msg.chat.id,"Gostou de visualizar os componentes de um PC? Essa área é de muita importância para um TI, tente marcar presença na monitoria para ter contato com essas peças mais vezes e para adquirir experiência de montagem de computadores! Mas... já vai se preparando, vai ter que conserta o PC de todo mundo 😅\n\nAperte /menu para voltar a tela de opções.")
    
@bot.message_handler(commands=["2"])
def op2(msg):
    txt = """
    Escolha abaixo um dos temas da feira pra que a gente possa saber qual você mais gostou

    /Programacao Para os projetos envolvendo a área de desenvolvimento com programação

    /Arduino Para os projetos que envolveram a placa eletrônica arduino

    /Arte Para os projetos que trouxeram alguma coisa relacionada a arte com componentes inutilizados

    /Hard para os projetos que envolveram peças de hardware do computador"""

    bot.send_message(msg.chat.id, txt)



@bot.message_handler(commands=["3"])
def fortDev(msg):
    bot.send_message(msg.chat.id, "Vai lá no Insta e segue o Juanzeen então, cobra ele pra ele continuar trabalhando em mim e para desenvolver outros projetos! 😎 \n\nhttps://www.instagram.com/juanzeenn/ \n\nClique /menu para voltar a tela de opções.")

@bot.message_handler(commands=["4"])
def ipc(msg):
    bot.send_message(msg.chat.id, "Então você tá afim de conhecer o melhor canal do YouTube? Eu apresento ele pra você sem pensar duas vezes, é entrar nesse link e acompanhar os minino da informática e os futuros trabalhos deles, garanto que o conteúdo é de qualidade avançada! \n\nhttps://www.youtube.com/channel/UC9y46TGILn7-r9CTyGEMwoA \n\nClique /menu para voltar a tela de opções.")

@bot.message_handler(commands=["5s"])
def star5(msg):
    bot.send_message(msg.chat.id, "Muito obrigado por ter avaliado tão positivamente nossa feira! Ficamos muito gratos e felizes de ter entregado um bom trabalho! 😊\n\nAperte /menu para voltar a tela de opções.")
@bot.message_handler(commands=["4s"])
def star4(msg):
    bot.send_message(msg.chat.id, "Uuuuuuu quase 5 estrelas, esperamos conseguir melhorar para o próximo evento e entregar um conteúdo excelente para você! 😊\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["3s"])
def star3(msg):
    bot.send_message(msg.chat.id, "Muito obrigado pela sua avaliação, queremos entregar um trabalho ainda melhor pra você, então peço que entre em contato com os organizadores da feira e nos ajude para sabermos onde melhorar! 🙂\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["2s"])
def star2(msg):
    bot.send_message(msg.chat.id, "Esse não era o resultado que a gente esperava, mas pode ter certeza que nos esforçaremos muito para entregar um resultado melhor numa próxima oportunidade, fale com os organizadores para sabermos o que melhorar! 😉\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["1s"])
def star1(msg):
    bot.send_message(msg.chat.id, "Uma estrelinha só? 😢 Fale conosco para que a gente saiba onde melhorar e nos ajude a entregar uma melhor experiência da próxima vez, muito obrigado pela sua presença! 🙂\n\nAperte /menu para voltar a tela de opções.")

@bot.message_handler(commands=["5"])
def op3(msg):
    txt = """
    Deixa aqui aquela avaliação braba pra que a gente possa saber onde melhorar!
    
    /5s ⭐⭐⭐⭐⭐

    /4s ⭐⭐⭐⭐

    /3s ⭐⭐⭐

    /2s ⭐⭐

    /1s ⭐"""
    
    bot.send_message(msg.chat.id, txt)

@bot.message_handler(commands=["6"])
def bye(msg):
    bot.send_message(msg.chat.id, "Tchauzinho user,  fico feliz de ter conversado com você! Se quiser trocar uma ideia de novo depois é só aparecer aí que eu nunca canso de conversar! Abraços do IFFDTBot! 🤖\n\nClique /menu para voltar a tela de opções.")
    
def verify(msg):
    return True

@bot.message_handler(func=verify)
def answerP(msg):
    txt = """
        Olá user! Aqui é o FDT Chatbot! 🤖

     Sou um bot feito especialmente para essa feira que você está participando, sinta-se especial!
     Escolha uma das opções abaixo para poder ver minhas funções

     /1 Sobre mim 
     /2 Qual assunto da feira você mais gostou?
     /3 Fortalecer meu desenvolvedor
     /4 Descobrir o melhor canal do YouTube
     /5 Avaliar a FDT
     /6 Dar tchau 

     Só peço para que clique nas opções, eu ainda tenho muito a ser desenvolvido e não funciono sem essas opções 🙁
    
     A máfia 123 agradece sua presença desde já!
        """ 
    bot.send_message(msg.chat.id, txt) 

bot.polling()