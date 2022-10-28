import os

def processar_resposta(resposta):
    if resposta == '1':
        print(f'{os.linesep}Poxa, então vou te apresentar um pouco o jogo e os personagens e no final você me conta seu favorito, beleza?!{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}Que legal, então vamos ver um pouco sobre os personagens e no final você me conta seu favorito, beleza?!{os.linesep}')
    else:
        print('Digite uma opção válida, por favor!')

def processar_genero(genero):
    if genero == '1':
        print(f'{os.linesep}Show! Então vamos para os personagens masculinos{os.linesep}')
    elif genero == '2':
        print(f'{os.linesep}Boa escolha! Vamos então para as personagens femininas{os.linesep}')
    elif genero ==  '3':
        print('Até logo!')
    else:
        print('Por favor, escolha uma opção válida.')

def personagens_femininos(femininos):
    if femininos == '1':
        print(f'Fade, uma caçadora de recompensas turca, usa o poder dos pesadelos para capturar os segredos dos inimigos. Personificando o próprio terror, ela persegue os alvos e revela seus medos mais profundos para, depois, destruí-los na escuridão.')
    elif femininos == '2':
        print(f'Como uma verdadeira fortaleza chinesa, Sage traz segurança para si mesma e para a equipe aonde quer que vá. Capaz de reviver aliados e rechaçar investidas agressivas, ela oferece um centro de calmaria em meio ao caos da batalha.')
    elif femininos == '3':
        print(f'Viper, a química dos Estados Unidos, emprega uma variedade de dispositivos químicos venenosos para controlar o campo de batalha e prejudicar a visão do inimigo. Se as toxinas não matarem a presa, seus jogos mentais certamente o farão.')
    elif femininos == '4':
        print(f'Criada no coração do México, Reyna domina o combate individual, destacando-se a cada abate efetuado. Sua capacidade só é limitada por sua própria perícia, tornando-a bastante dependente de desempenho.')
    elif femininos == '5':
        print(f'Killjoy, uma alemã genial, defende o campo de batalha facilmente usando seu arsenal de invenções. Se o dano causado por seu equipamento não der cabo dos inimigos, os efeitos negativos de seus queridos robôs dão conta do recado.')
    elif femininos == '6':
        print(f'Representando a Coreia do Sul, sua terra natal, Jett tem um estilo de luta ágil e evasivo que permite que ela assuma riscos como ninguém. Ela corre em meio a qualquer confronto, cortando os inimigos antes mesmo que eles percebam quem ou o que os atingiu.')
    elif femininos == '7':
        print(f'Raze chega do Brasil em uma explosão de carisma e armas letais. Com seu estilo de jogo "porradeiro", ela é craque em desentocar inimigos entrincheirados e limpar espaços apertados com uma bela dose de BUUUM!')
    elif femininos == '8':
        print(f'Mandando um salve direto da Austrália, Skye e sua equipe de feras desbravam territórios hostis. Com seus poderes de cura e suas criações que partem pra cima dos inimigos, qualquer equipe ficará mais forte e mais segura tendo Skye como aliada.')
    elif femininos == '9':
        print(f'Astra, a Agente ganense, utiliza energias cósmicas para moldar o campo de batalha a seu bel-prazer. Com total domínio da sua forma astral e um talento estratégico nato, ela está sempre anos-luz à frente dos inimigos.')
    elif femininos == '10':
        print(f'Neon, nossa Agente filipina, avança em velocidades incríveis, descarregando surtos de radiância bioelétrica tão rapidamente quanto seu corpo consegue gerá-los. Ela corre à frente para pegar os inimigos de surpresa, abatendo-os mais rápido do que um raio.')
    elif femininos == '11':
        print('Vamos aos masculinos então?!')
    else:
        print('Escolha uma alternativa válida, por favor.')

def personagens_masculinos(masculinos):
    if masculinos == '1':
        print(f'Vindo do litoral indiano, Harbor entra em campo com a força da tormenta, empunhando tecnologia ancestral com domínio sobre a água. Ele libera corredeiras espumantes e ondas esmagadoras para proteger seus aliados e atacar aqueles que se opõem a ele.')
    elif masculinos == '2':
        print(f'Vindo diretamente dos EUA, o arsenal orbital de Brimstone garante que o esquadrão dele esteja sempre em vantagem. Sua capacidade de oferecer utilidade com precisão a distância faz dele um comandante inigualável na linha de frente.')
    elif masculinos == '3':
        print(f'Chegando com tudo diretamente do Reino Unido, o poder estelar de Phoenix reluz em seu estilo de luta, incendiando o campo de batalha com luz e estilo. Tendo ajuda ou não, ele entra na luta como e quando achar que deve.')
    elif masculinos == '4':
        print(f'Nascido sob o eterno inverno das tundras russas, Sova rastreia, encontra e elimina inimigos com eficiência e precisão implacáveis. Seu arco personalizado e suas habilidades inigualáveis de reconhecimento garantem que nenhuma presa escape.')
    elif masculinos == '5':
        print(f'Cypher, um vendedor de informações do Marrocos, é uma verdadeira rede de vigilância de um homem só que fica de olho em cada movimento dos inimigos. Nenhum segredo está a salvo. Nenhuma manobra passa despercebida. Cypher está sempre vigiando.')
    elif masculinos == '6':
        print(f'Breach, o homem-biônico sueco, dispara poderosos jatos cinéticos para forçar a abertura de um caminho pelo território inimigo. O dano e a interrupção que ele causa garantem que nenhuma luta seja justa.')
    elif masculinos == '7':
        print(f'Omen, uma lembrança fantasmagórica, caça nas sombras. Ele cega os inimigos, teleporta-se pelo campo e deixa a paranoia assumir o controle enquanto o adversário tenta descobrir de onde virá seu próximo ataque.')
    elif masculinos == '8':
        print(f'Yoru, nativo do Japão, abre fendas na realidade para infiltrar as linhas inimigas sem ser visto. Ele usa tanto artimanhas quanto táticas agressivas, e os alvos são abatidos sem saber de onde o ataque veio.')
    elif masculinos == '9':
        print(f'KAY/O é uma máquina de guerra construída com um único propósito: neutralizar Radiantes. Ele é capaz de suprimir habilidades inimigas, comprometendo a capacidade de contra-ataque dos adversários e dando a si próprio e a seus aliados uma vantagem essencial em combate.')
    elif masculinos == '10':
        print(f'Bem vestido e armado até os dentes, o criador de armas francês Chamber coloca os inimigos para correr com uma precisão mortal. Use e abuse do arsenal personalizado dele para segurar posições e abater inimigos de longe, criando a defesa perfeita para qualquer plano.')
    elif masculinos == '11':
        print('Vamos aos femininos então?!')    
    else:
        print(f'Escolha uma alternativa válida, por favor.')

def start():

    # Apresentar o bot
    print(
            f'Olá! Meu nome é chatinho, mas eu juro que sou legal, confia! hehe{os.linesep}')

    # Pedir o nome 
    nome = input('Qual o seu nome?\n')

    # Oferecer o menu de opções     
    resposta = input(
            f'Você joga Valorant?{os.linesep}[1] - Não :/{os.linesep}[2] - Sim :){os.linesep}')

    # Processar a resposta enviada
    processar_resposta(resposta)

    while True:
    #Apresentar personagens
        genero = input(
                f'Então me diga, {nome}, você quer conhecer primeiro os personagens {os.linesep}[1] - Masculinos{os.linesep}[2] - Femininos{os.linesep}[3] - Sair{os.linesep}')

        # Processar gênero
        processar_genero(genero)

        if genero == '2':
            while True:
            # Personagens Femininas
                femininos = input(
                    f'Vou te falar o nome delas e você escolhe a que mais curtir, okay?{os.linesep}[1] - Fade{os.linesep}[2] - Sage{os.linesep}[3] - Viper{os.linesep}[4] = Reyna{os.linesep}[5] - Killjoy{os.linesep}[6] - Jett{os.linesep}[7] - Raze{os.linesep}[8] - Skye{os.linesep}[9] - Astra{os.linesep}[10] - Neon{os.linesep}[11] - Sair{os.linesep}')

            # Processar personagens Femininos
                personagens_femininos(femininos)

                if femininos == '11':
                    break

        if genero == '1':
            while True:
            # Personagens Masculino 
                masculinos = input(
                f'Vou te falar o nome deles e você escolhe o que mais curtir, okay?{os.linesep}[1]- Harbor{os.linesep}[2] - Brimstone{os.linesep}[3] - Phoenix{os.linesep}[4] - Sova{os.linesep}[5] - Cypher{os.linesep}[6] - Breach{os.linesep}[7] - Omen{os.linesep}[8] - Yoru{os.linesep}[9] - Kayo/O{os.linesep}[10] - Chamber{os.linesep}[11] - Sair{os.linesep}')

            # Processar personagens Masculinos
                personagens_masculinos(masculinos)

                if masculinos == '11':
                    break

        if genero == '3':
            break
                
if __name__ == '__main__':
    start()