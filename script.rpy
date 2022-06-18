init python:
    romSer = False
    morSer = False
    romSer2 = False
    morSer2 = False
    naonada = False
    nada = False
    afogado = False
    espuma = False

define p = Character("Você")
define n = Character("")
define c = Character("Contador de Histórias")
define m = Character("Marinheiro")
define i = Character("???")
define s = Character("Sereia")
define sm = Character("Marion")
define pr = Character("Príncipe")
define pc = Character("Chris")
image sala = "images/sala inicial com livro.png"
image sala2 = "images/sala inicial sem livro.png"
image pagina1 = "images/página de livro.png"
image escurototal = "images/telapreta.png"
image contador = "images/Contador padrão.png"
image contadorbravo = "images/Contador bravo.png"
image contadordesapontado = "images/Contador desapontado.png"
image contadorcontente = "images/Contador feliz.png"
image contadorconfuso = "images/Contador confuso.png"
image barco1 = "images/barco ao amanhecer.png"
image barco2 = "images/barco céu claro mar verde.png"
image barco3 = "images/barco céu bem claro mar verde.png"
image barco4 = "images/barco céu bem claro mar azul.png"
image barco5 = "images/barco céu claro mar azul.png"
image barco6 = "images/barco céu tempestuoso.png"
image marescuro = "images/mar céu escuro.png"
image fundomar1 = "images/debaixo da água.png"
image fundomar2 = "images/mar com sombra.png"
image fundomar3 = "images/mar com sombra2.png"
image fundomar4 = "images/mar com sombra 3.png"
image fundomar5 = "images/mar com sombra pertinho.png"
image fundomar6 = "images/fundo do mar com sombra perto.png"
image fundomar7 = "images/mar com sombra e olhos perto.png"
image fundomar8 = "images/sombra olhos super escura.png"
image fundomar9 = "images/olhos no escuro.png"
image fundomar10 = "images/fechando os olhos.png"
image quarto = "images/quarto.png"
image marcalmoestrelas = "images/mar noite calma com estrelas.png"
image varandamanha = "images/varanda de manhã.png"
image varandadia = "images/varanda de céu claro.png"
image varandanoite = "images/varanda e estrelas a noite.png"
image parede = "images/parede.png"
image paredenoite = "images/paredenoite.png"
image sereia1 = "images/sereia/placeholders/fundovarandamanhecersurpreso.png"
image sereia2 = "images/sereia/placeholders/fundovarandamanhecersurpreso1.png"
image sereia3 = "images/sereia/placeholders/fundovarandamanhecersurpreso2.png"
image sereia4 = "images/sereia/placeholders/fundovarandamanhecersurpreso3.png"
image sereia5 = "images/sereia/placeholders/fundovarandamanhecersurpreso4.png"
image principe1 = "images/principe/placeholders/cena1.png"
image principe2 = "images/principe/placeholders/cena2.png"
image principe3 = "images/principe/placeholders/cena3.png"
image principe4 = "images/principe/placeholders/cena4.png"
image principe5 = "images/principe/placeholders/cena5.png"
image principe6 = "images/principe/placeholders/cena6.png"
image servaranda1 = "images/sereia/placeholders/ceuclarovarandacena.png"
image servaranda2 = "images/sereia/placeholders/ceuclarovarandacena1.png"
image servaranda3 = "images/sereia/placeholders/ceuclarovarandacena2.png"
image servaranda4 = "images/sereia/placeholders/ceuclarovarandacena3.png"
image servaranda5 = "images/sereia/placeholders/ceuclarovarandacena4.png"
image servaranda6 = "images/sereia/placeholders/ceuclarovarandacena5.png"
image servaranda7 = "images/sereia/placeholders/ceuclarovarandacena6.png"
image servaranda8 = "images/sereia/placeholders/ceuclarovarandacena7.png"
image servaranda9 = "images/sereia/placeholders/ceuclarovarandacena8.png"
image servaranda10 = "images/sereia/placeholders/ceuclarovarandacena9.png"
image servaranda11 = "images/sereia/placeholders/ceuclarovarandacena10.png"
image servaranda12 = "images/sereia/placeholders/ceuclarovarandacena11.png"
image servaranda13 = "images/sereia/placeholders/ceuclarovarandacena12.png"
image servaranda14 = "images/sereia/placeholders/ceuclarovarandacena13.png"
image servaranda15 = "images/sereia/placeholders/ceuclarovarandacena14.png"
image servaranda16 = "images/sereia/placeholders/ceuclarovarandacena15.png"
image floresta = "/images/floresta.png"
image noitesereia1 = "images/sereia/placeholders/ceuescurocena1.png"
image noitesereia2 = "images/sereia/placeholders/ceuescurocena2.png"
image noitesereia3 = "images/sereia/placeholders/ceuescurocena3.png"
image noitesereia4 = "images/sereia/placeholders/ceuescurocena4.png"
image noitesereia5 = "images/sereia/placeholders/ceuescurocena5.png"
image noitesereia6 = "images/sereia/placeholders/ceuescurocena6.png"
image noiteprin1 = "images/principe/placeholders/cenanoite1.png"
image noiteprin2 = "images/principe/placeholders/cenanoite2.png"
image noiteprin3 = "images/principe/placeholders/cenanoite3.png"
image praiafinal = "images/céu bem claro mar verde.png"
image poente = "images/mar por do sol.png"
image finalespuma = "images/sereia/placeholders/finalespuma.png"
image finalagua = "images/sereia/placeholders/finalagua.png"
image prinfinal1 = "images/principe/placeholders/cenapraia1.png"
image prinfinal2 = "images/principe/placeholders/cenapraia3.png"
image prinfinal3 = "images/principe/placeholders/cenapraia3.png"
image fim = "images/fim.png"
image over = "images/gameover.png"

# The game starts here.

label start:
label prologo:
    #colocar um efeito sonoro de trovão aqui
    play music "audio/piano na mansão.mp3"
    p "Uh, parece que irá chover. Só espero que esta casa velha aguente um temporal."
    p "Essa casa velha..."
    p "Lugar sujo."
    p "É tudo culpa minha."
    p "Eu me arrependo imensamente de ter concordado com tudo isto."
    p "Bem que sempre me disseram para não apostar nada, especialmente se sei que a chance de eu perder é grande."
    p "Tudo culpa de ter acreditado que seria divertido."
    p "E foi, na verdade."
    p "Mas agora eu estou aqui, nesse casebre velho sem energia elétrica, durante a noite, sem sinal de internet ou telefone, nem água encanada tem aqui."
    p "Aposto que só escolheram essa punição para o perdedor da aposta porque sabem que odeio o escuro."
    p "Minha sorte é que achei umas velas e uma caixa de fósforos super velha mais cedo."
    p "É estranho que nem tudo aqui esteja coberto de poeira, essa casa está abandonada desde quando meus avós eram jovens, até criancinhas ouvem histórias sobre fantasmas aqui."
    p "Eu devia ter dado dez reais como punição para o perdedor por ter tirado a pior pontuação, não aceitar a sugestão que o perdedor teria que passar uma noite inteira aqui nesta casa assombrada."

    #som de trovão

    p "Eu acho que vou continuar explorando a casa, quero garantir que eu não vá precisar dormir numa cama molhada."

    #som de passos e mudar cenas rápido (fazer depois)

    scene sala
    with fade

    p "Não tem cama com colchão. "
    p "Parece que sou só eu, um telefone apenas para chamadas de emergência, uma vela e um sofá com um gabinete velho de livros."
    p "Ainda faltam dez horas para minha punição acabar, talvez eu deva reavivar um velho hábito."
    p "Eu lembro que quando eu era criança, eu lia livros quase o tempo todo, era uma diversão e tanto."
    p "Mas, com as mudanças do mundo, passei à ler digitalmente, às vezes nem livros de fato lia mais. "
    p "Faz realmente um bom tempo desde que não pego um livro físico."
    p "Eu lembro na época da escola fundamental que alguns falavam sobre o cheiro de livro novo, sobre o prazer das folhas retinhas e como parecia um crime qualquer dobrinha."
    p "Às vezes até abrir demais era visto como algo ruim por danificar a lombada."
    p "Como migrei para livros digitais há anos, eu parei de me tocar com estas coisas."
    p "E ainda bem, porque talvez o EU daquela época entraria em colapso ao ver que aqui só uma quantidade absurda de livros extremamente velhos e caindo aos pedaços."
    p "Parece que realmente ninguém tem estado aqui em bem mais do que só décadas, talvez estes livros sejam mais velhos que a casa."
    p "Alguns estão até com a lombada faltante, todos estão amarelados e alguns eu tenho certeza que vão virar pó só de eu encostar neles."
    p "Mas no momento não tenho nada melhor para me distrair, na melhor das hipóteses eu vou dormir tranquilo enquanto leio e só vou acordar na hora de me tirarem daqui."
    p "Ainda restam pelo menos nove horas."
    #som de grude
    p "E eu não contava com o fato que estes livros parecem todos grudados na estante."
    p "..."
    p "Uns estão meio soltos, um deles deve sair."
    p "..."
    p "!!"
    p "... Tem literalmente um livro solto aqui na mesinha, por que estou me esforçando tanto?"
    p "Este não parece estar tão acabado, espero que esteja legível ao menos."

    scene sala2
    with dissolve

    p "É um livro de contos de fadas."
    p "Não é bem o que eu estava esperando, mas é melhor que nada."
    p "Não faz mal se eu ler... Está velho e puído, mas é algo."
    n "Você começa à ler o livro puído. Diversos contos de fadas estão presentes no índice, mas estão quase ilegíveis."
    p "..."
    p "O jeito é começar pelo primeiro."
    p "..."

    scene pagina1
    with dissolve

    p "..."
    p "Letra escrita à mão com desenhos?"
    p "Eu não sei se critico a caligrafia ou se eu fico feliz de ver que é um livro único."
    p "..."
    p "Isso é meio triste. Este livro é único e está se estragando."
    p "Talvez eu leve pra casa pra consertar."
    n "Você começa à ler o livro."
    p "Longe, muito longe, nas profundezas do mar, ficava o palácio do rei do mar..."
    p "Ele era viúvo e sua mãe reinava com ele... O rei tinha seis... Filhas..."
    p "... Por que eu estou sentindo tanto sono de repente?"
    p "... Tudo bem..."
    p "..."

    scene escurototal
    with fade

    p "... Seis filhas, as princesas... Do mar..."
    p "..."
    n "Você cai no sono."
    n "..."
    n "... Uh..."
    n "Um instante, caro sonhador."
    c "Agora sim."
    show contador
    with dissolve
    c "Agora podemos começar."
    c "Não se acanhe ou assuste, eu sou o Contador de Histórias."
    c "Desperte, sonhador."
    hide contador
    with dissolve
    n "Você desperta"
    scene sala2
    with fade
    p "!!!"
    p "O que foi isso?! Que sonho estranho!"
    c "Foi um sonho, mas eu diria que foi bem normal."
    p "Quem está aí?!"
    show contador
    with dissolve
    c "Eu estou, estive desde sempre, na verdade."
    p "Quem... Não, melhor! O quê é você?!"
    hide contador
    show contadorbravo
    c "Essa é uma pergunta muito rude de se fazer."
    p "Desculpa?! Não é sempre que eu vejo um rabisco falante!"
    hide contadorbravo
    show contadordesapontado
    c "..."
    c "Rabisco?"
    c "Eu não era exatamente um bom artista em vida, mas se referir à mim por RABISCO doeu..."
    p "(... Nossa, agora estou me sentindo mal.)"
    p "(... Talvez eu devesse pedir desculpas.)"
    p "Olha... Ahn... Seu...? Desenho...? Desculpe por te chamar de rabisco."
    hide contadordesapontado
    show contador
    p "..."
    c "..."
    hide contador
    show contadorcontente
    c "Desculpas aceitas, jovem."
    p "(Isso foi uma mudança de humor bem rápida.)"
    p "Mas, como devo te chamar? E quem é você?"
    c "Me chame apenas de Contador de Histórias, meu nome de verdade já não importa mais."
    p "..."
    hide contadorcontente
    show contador
    c "Bom, já que me apresentei, fico feliz que tenha acordado do seu pequeno sonho dentro de um sonho."
    p "Ô, ô, ô! Espera! Como assim, sonho dentro de um sonho?"
    c "De modo bem simples, você ainda está sonhando."
    hide contador
    show contadorbravo
    c "E não me peça para te acordar, porque eu não vou!"
    c "Não até você desfazer a bagunça que fez."
    p "Que bagunça que eu fiz?!"
    hide contadorbravo
    show contadorconfuso
    p "... ?!"
    c "Como assim? Você não se lembra?"
    p "... De quê?!"
    c "Você entrou nessa casa presumidamente assombrada, falou mal dela e tirou um livro de seu respectivo lugar."
    c "Você não levou à sério a parte de ASSOMBRADA."
    p "..."
    hide contadorconfuso
    show contador
    c "Tudo bem, não importa. O que importa é que... O livro que você tinha em mãos... É o trabalho de minha vida e agora ele está danificado por água."
    hide contador
    with dissolve
    n "Você olha o livro aberto em suas mãos, água de uma goteira borrou as páginas ao ponto de ficarem irreconhecíveis."
    p "... Desculpe."
    p "... Espere aí!"
    p "Alguém está ditando minhas ações!"
    show contadorcontente
    with dissolve
    c "Ah, sou eu, afinal, eu sou o Contador de Histórias! E no momento que você entrou nesta casa, você se tornou um personagem de minhas tramas."
    p "..."
    c "..."
    p "Eu vou pra casa agora mesmo."
    hide contadorcontente
    show contadorconfuso
    c "Eu acabei de dizer que controlo suas ações, como espera fugir?"
    p "..."
    n "Você se ergue."
    hide contadorconfuso
    show contadordesapontado
    c "Está bem! Eu menti para chamar sua atenção!"
    c "Mas você ainda não pode sair, isto é um fato..."
    p "Não é outra de suas mentiras?"
    c "É..."
    p "..."
    c "Mas, por favor, espere, eu preciso de ajuda!"
    p "..."
    p "Estou ouvindo."
    hide contadordesapontado
    show contadorcontente
    c "Obrigado, irei contar meu problema."
    c "Todos que entram nessa casa e leêm o Codex Fabula ficam presos em um sonho lúcido e o único jeito de acordar dele é refazendo o livro."
    p "..."
    hide contadorcontente
    show contador
    c "Nesse momento, faz muitos anos desde que morri e ninguém leu o Codex Fabula, então estou amaldiçoado à vagar como um fantasma, rezando que um dia alguém viesse e tomasse meu posto."
    p "E eu sou o próximo fantasma?"
    c "Teoricamente, se você morrer sem passar o livro adiante, você pode se considerar um fantasma."
    p "..."
    p "E o que eu tenho de fazer? Ou melhor, como eu reescrevo o Codex Fabula?"
    hide contador
    show contadorcontente
    c "É simples, você só precisa entrar no livro."
    p "... Você quer dizer ler o livro, não é?"
    c "Não, eu disse entrar no livro. Literalmente."
    p "... E como faz isso?"
    c "Você toca no livro onde quer ir e começa à ler, é óbvio."
    p "... E como eu reescrevo, se vou estar dentro dele?"
    hide contadorcontente
    show contador
    c "Essa é a parte difícil. Ou melhor, a parte perigosa."
    p "?"
    c "Uma vez dentro do livro, você irá assumir um papel temporário. Lá dentro você terá de garantir que o final seja o mesmo que o conto original."
    n ""
    p "... O mesmo? Mas se são pessoas diferentes que reescreveram o Codex Fabula, significa que sempre vai ter uma diferença ou outra, não é?"
    c "Correto. Porém é perigoso que muitas diferenças ocorram... Muitos dos antigos Sonhadores ficaram presos para sempre em seus sonhos, pois morreram ou tomaram um final dentro do Codex Fabula em suas mãos."
    p "Isso é meio assustador."
    c "Eu tive a mesma reação que você. E antes que pergunte, existe sim um meio de desfazer a maldição do Codex Fabula, eu apenas não sei como, mas tenho uma teoria."
    c "O primeiro Sonhador foi o primeiro que escreveu esse copilado, ele ficou para sempre dentro do Codex, imortal, adicionando novas histórias que vieram nas memórias de novos Sonhadores."
    c "Talvez o desejo dele fosse copilar todos os Contos de Fadas do mundo, os que existiam e os que irão existir."
    p "..."
    p "Eu não vou dizer o que realmente acho dessa motivação."
    c "Tudo bem, eu não tenho uma opinião positiva também."
    c "O importante é que agora você precisa ir, precisa ir consertar os finais das histórias se quiser voltar para sua vida."
    p "Espere."
    p "Se eu morrer lá dentro, eu morro aqui?"
    c "Evidentemente."
    p "... Entendi. Bom, então eu só tenho de fazer o fluxo normal continuar, não é?"
    c "Isso mesmo. A cada capítulo que terminar, você acordará do sonho. Mas, da próxima vez que dormir, você retornará à ele num novo capítulo."
    p "Entendi."
    c "Mais uma coisa, não deixe o Codex Fabula se perder ou ser destruído enquanto estiver nas histórias. Se isto acontecer, você, eu e todos os outros, ficaremos presos para sempre."
    p "... Sempre?"
    c "Sim, pois o Codex Fabula existe em dois mundos como um par de telefones recebendo sinais. Se perder um dos lados, a linha será cortada e não será possível ligar para casa. Entendeu?"
    p "Entendi..."
    c "..."
    hide contador
    show contadorcontente
    n ""
    c "Vejo que você estava lendo A Pequena Sereia. É um conto trágico."
    p "Trágico? É uma história de amor pra crianças, não é?"
    hide contadorcontente
    show contadordesapontado
    c "É, de fato, um conto feito para crianças, mas não deixa de ser trágico."
    c "Bom, é hora de você ir. Estarei te assistindo, caso precisar de uma interferência muito forte, eu poderei te ajudar."
    hide contadordesapontado
    show contadorcontente
    c "Boa sorte, Sonhador."
    hide contadorcontente
    with dissolve
    p "... Vou tentar, Contador de Histórias."
    n ""
    stop music
    scene escurototal
    with fade
    p "Será que ele falou a verdade?"
    p "Só vendo para saber."

    jump contodia1

    # CAPÍTULO UM COMEÇA AQUI
label contodia1:

    play music "audio/piano-suave-navio.mp3"
    n ""
    scene barco1
    with dissolve
    n ""
    p "... Uau..."
    p "... Isso é mesmo o oceano?"
    p "É um barco!"
    p "Então sifnifica que eu vou estar substituíndo o príncipe?"
    p "..."
    p "Cruz e credo, eu não quero beijar um peixe."
    m "Ei, você, rato afogado!"
    p "Eu?"
    m "Você mesmo, comece à limpar o convés, a festa de aniversário do Príncipe precisa de um lugar limpo!"
    p "... Acho que prefiro beijar um peixe..."
    m "Vamos, pare de reclamar e vá logo!"
    p "Ah! Sim, sim senhor!"
    p "..."
    p "É, eu não sou o príncipe, já é algo."
    scene escurototal
    with fade
    n "Você passa a manhã inteira limpando o convés. Quando termina, o sol está alto."
    scene barco2
    with dissolve
    n ""
    p "Shuuush! Isso demorou mais do que eu queria, mas menos do que eu esperava."
    p "Bom, acho que tudo que tenho que fazer é esperar a festa, se me lembro bem a Sereia deve aparecer nessa hora."
    n "Você começa à esperar."
    n ""
    scene barco2
    with dissolve
    p "..."
    p "Isso está demorando."
    n ""
    scene barco3
    with dissolve
    n ""
    p "..."
    n ""
    scene barco4
    with dissolve
    n ""
    p "..."
    n "Você decide esperar ainda mais um pouco."
    scene barco5
    with dissolve
    n ""
    n "Diversas comidas foram postas e um lugar aberto, fogos de artifício foram preparados, mas sem sinal do Príncipe."
    n "Você está começando à se questionar se o mundo lá fora está passando ao mesmo tempo que agora."
    n ""
    m "Abram alas! O Príncipe vem aí!"
    p "!!"
    p "Finalmente! Agora só preciso esperar pela Sereia e..."
    stop music

    # som de trovão
    play music "audio/afogando.mp3"
    p "Espera, um trovão em meio à céu aberto? Como isso é possível?"
    scene escurototal
    with fade
    n ""
    p "Espere?! O que aconteceu?"
    p "Por que de repente tudo...?!"
    scene barco6
    with dissolve
    p "... Ah, estou começando à entender..."
    p "Esse livro provavelmente muda as coisas de acordo com o usuário! Ou o antigo escritor fez uma meleca."
    p "Se ao menos eu tivesse lido mais..."
    p "Espere, eu posso ler!"
    n "No momento que você iria abrir o Codex Fabula em sua bolsa, o navio balança."
    p "Melhor eu não fazer isso agora, não posso perder esse livro."
    n "O mar está cada vez mais revolto."
    n "E de repente... Numa forte onda, você escorrega por cima do guarda-corpo e cai ao mar."
    n ""
    scene escurototal
    with fade
    n ""
    scene fundomar1
    with fade
    n ""
    p "(Eu não consigo nadar!)"
    p "(Será que é assim que vou morrer? Vou para sempre ser um fantasma nesse livro?)"
    p "(Não! Eu preciso conseguir sair daqui!)"
    menu:
        "Debater-se":
            $nada = True
            n "Você se debate, mas as ondas são fortes demais."

        "Permanecer inerte":
            $naonada = True
            n "Você fica inerte, mas as ondas não perdoam."
    n ""
    scene fundomar2
    with dissolve
    n ""
    p "(O que é aquilo?!)"
    menu:
        "Tentar nadar na direção contrária.":
            $afogado = True
            n "Você consegue nadar para longe da criatura, inevitavelmente se afundando mais ainda."
            p "..."
            n "A força do mar é forte demais para que você retone à superfície agora."
            n "Pouco a pouco, o ar escapa de seus pulmões."
            n "Sua consciência aos poucos se esvai."
            n "..."
            stop music
            scene escurototal
            with dissolve
            jump gameover

        "Tentar nadar para cima.":
            n "Você tenta nadar para a superfície."
            n "Porém a sombra parece estar mais próxima."
    scene fundomar3
    with dissolve
    p "(É assim que vou morrer?! Devorado?!)"
    scene fundomar4
    with dissolve
    p "(Contador de Histórias! Eu preciso de sua ajuda!)"
    n ""
    scene fundomar5
    with dissolve
    p "(... Eu não estou mais conseguindo respirar...)"
    scene fundomar6
    with dissolve
    p "(Alguém...)"
    scene fundomar7
    with dissolve
    p "(Me...)"
    scene fundomar8
    with dissolve
    p "(Salve...)"
    scene fundomar9
    with dissolve
    p "(Por favor...)"
    scene fundomar10
    with dissolve
    p "(...)"
    n ""
    scene escurototal
    with dissolve
    stop music
    n ""
    scene quarto
    with fade
    n ""
    play music "audio/oo.mp3"
    p "..."
    p "... Estou respirando! Eu não morri!"
    p "E onde eu estou...? Um quarto?"
    p "... Espere..."
    scene escurototal
    with pixellate
    p "Se me lembro bem..."
    scene fundomar7
    with pixellate
    p "... Tinha uma coisa na água que me encarou de perto."
    p "Significa que talvez seja a Sereia desse conto."
    scene quarto
    with pixellate
    p "Já que estou aqui num quarto que..."
    n "Você se levanta da cama e vai até a janela."
    scene marcalmoestrelas
    with fade
    p "Dá para ver o mar daqui, pela altura... Deve ser um castelo ou algo assim."
    p "Certo, significa que eu e o Príncipe fomos salvos, não é?"
    p "..."
    p "Não é?"
    p "... Contador de Histórias? Se está aí me ouvindo, me responda."
    p "..."
    scene quarto
    with fade
    p "É, talvez eu deva tentar ler o livro, assim posso descobrir os caminhos que devo tomar."
    n "Você pega o livro em sua bolsa, porém ele não abre."
    n "Você aplica um pouco de força, nada acontece."
    p "... Que diabos é isso! Vai me dizer que não consigo ler o livro enquanto ele está sendo reescrito por mim?"
    p "Droga!"
    n "Você se senta de volta na cama."
    p "Tudo bem, eu só preciso... Achar o Príncipe e a Sereia."
    p "Acho que só."
    p "Por agora... Eu vou dormir. Amanhã eu vou me aventurar pelo castelo e a praia, talvez eu ache algo."
    n "Você se deita na cama para dormir e espera o amanhecer."
    scene escurototal
    with dissolve
    stop music
    n "A noite passa."
    n "Você não sonhou nada."
    n "Logo que desperta, você decide reconhecer a área em busca do Príncipe ou a Sereia."
    scene varandamanha
    with dissolve
    play music "audio/dia1.mp3"
    p "(Terei de tomar cuidado enquanto ando por aqui. Apesar de eu ter sido transportado para um mundo de fantasia, é estranho que ninguém tenha questionado meu nome ou aparência.)"
    p "(...)"
    p "(Contador de Histórias, isto é mais uma de suas artimanhas? É porque você escreveu essa história de modo resumido?)"
    p "..."
    p "... Sem resposta, como sempre."
    n "Você ouve passos apressados pelo corredor."
    p "!!"
    n "Virando na direção deles, você percebe uma pessoa se aproximando em sua direção."
    show sereia1
    with dissolve
    i "!!"
    i "...! !! ? !!"
    show sereia2
    hide sereia1
    i "... ??"
    p "(... Ele está tentando falar algo?)"
    p "Ah, desculpe, mas eu não estou escutando você."
    show sereia3
    hide sereia2
    i "..."
    i "...?"
    i "..."
    p "(Sujeito estranho.)"
    show sereia4
    hide sereia3
    p "... Você consegue fazer linguagem de sinais?"
    i "..."
    p "... Sabe escrever?"
    show sereia5
    hide sereia4
    p "..."
    i "..."
    p "Espera, eu vou buscar papel e caneta para você."
    i "..."
    n "Quando você menos esperava, o rapaz se curva um pouco para você e se retira."
    hide sereia5
    with dissolve
    p "... Sujeito estranho."
    p "Bom, não posso parar minha busca agora. Preciso encontrar o Príncipe e, ou, a Sereia."
    p "..."
    p "ESPERE AÍ!"
    p "Se me lembro bem, a Sereia perde sua voz quando vem para a superfície...!"
    p "Eu encontrei a Sereia!"
    p "... E ela é um homem?"
    p "Não vou questionar, deve ser um gosto pessoal do Contador de Histórias."
    p "Bom, eu agora devo encontrar o Príncipe e unir os dois, certo?"
    p "Se eu correr, talvez eu alcance ele!"
    p "Se eu estabelecer amizade com a Sereia, eu posso juntá-los, corrigir o final e ir para casa!"
    p "Pra que lado ele foi mesmo?"

    menu:
        "Ir para a Direita":
            $romSer = True
            p "Irei por aqui."
            n "Você sai em disparada."
            show parede
            with fade
            show parede
            with fade
            show parede
            with fade
            p "... Acho que perdi ele de vista."
            p "Tudo bem."
            n ""
            n "Quando você se vira para ir embora, você sente a sensação de estar sendo observado, mas nenhuma pessoa se faz presente."
            n "De repente, uma figura vem em sua direção."

        "Ir para a Esquerda":
            $morSer = True
            p "Irei por aqui."
            n "Você sai em disparada."
            show parede
            with fade
            show parede
            with fade
            show parede
            with fade
            p "... Acho que perdi ele de vista."
            p "Tudo bem."
            n ""
            n "Quando você se vira para ir embora, você avista uma figura se aproximando de você."

    show principe1
    with dissolve
    i "Oh, que bom que já levantou. Como se sente?"
    p "(Oh não, seria esse rapaz o príncipe?)"
    p "(Espere, se for ele, meu trabalho está quase completo!)"
    p "Eu me sinto bem. O que aconteceu ontem?"
    i "Você quer dizer há uma semana."
    p "Uma semana?!"
    show principe2
    hide principe1
    i "Sim, faz uma semana desde a tempestate repentina."
    i "Em meu nome, uma vez que ocorreu durante meu aniversário, desejo pedir desculpas à ti."
    p "(Aniversário? Eu sabia! Ele é o Príncipe!)"
    p "(Como esperado de minha mente brilhante! Eu estarei em casa assim que juntar esses dois!)"
    show principe4
    hide principe2
    p "(... Eu disse algo de errado?)"
    pr "Você parece perdido em pensamentos.."
    p "(Ah, eu não disse nada.)"
    p "Ah, mil perdões, vossa alteza!"
    show principe6
    hide principe4
    pr "Menos, menos dessa formalidade, você está aqui como um convidado."
    pr "Se estava em minha festa, certamente é alguém de estima alta na sociedade."
    show principe1
    hide princepe6
    pr "E por isso me perdoe por indagar sobre suas origens."
    p "Sem nenhum problema."
    n "Você diz seu nome e de onde vem."
    show principe4
    hide principe1
    pr "... Eu realmente nunca ouvi falar de você ou de onde veio."
    show principe2
    hide principe4
    pr "Porém, chega de tais formalidades. Enquanto estivermos de visita nesse palácio de verão, é livre para me chamar por Chris."
    p "Chris?"
    pr "Sim, Chris é meu nome. O navio virou próximo à este palácio, então resolvi que ficaria de férias por aqui. Por isso não tema em usar meu nome."
    p "... Certo."
    show principe5
    hide principe2
    pc "Ora, vamos, pare com essa hesitação toda!"
    p "... Desculpe!"
    pc "Por favor, não se desculpe."
    p "..."
    show principe4
    hide principe5
    pc "... Perdão."
    p "Tudo bem."
    p "Não! Espere!"
    pc "Huh?"
    p "Tem uma outra pessoa que estava no navio, não tem?"
    pc "Outra pessoa?"
    p "É, um garoto que não fala e tem cabelo longo."
    show principe3
    hide principe5
    pc "Ah, você está se referindo ao Marion? Ele chegou há um dia atrás."
    pc "Estava desacordado na praia, provavelmente estava no navio também."
    pc "É um rapaz muito bom, eu acho que vocês se darão bem!"
    p "Marion? Ele que te disse esse nome?"
    show principe4
    hide principe3
    pc "... Na verdade, não."
    pc "Marion não sabe escrever ou fazer sinais para formar palavras."
    pc "Então quando eu perguntei seu nome, ele apontou o mar. Eu testei vários nomes e ele desistiu de me fazer adivinhar quando eu disse esse nome."
    p "Então tem uma chance de não ser o nome real dele, não é?"
    pc "A chance existe. Eu acho que o caso dele é um mutismo temporário, caso contrário ele já saberia se comunicar de outras formas, não acha?"
    p "É plausível."
    show principe3
    hide principe4
    pc "Heh! Que seja, por que não vamos nós três passar um tempo juntos? A tarde eu pretendia levar ele para cavalgar comigo, você pode vir junto!"
    p "(Que chance única!)"
    p "Sim, eu aceito."
    pc "Perfeito! Passarei após o almoço para buscar vocês! Até a vista!"
    hide principe1
    hide principe3
    hide principe6
    with dissolve
    p "(ISSO!)"
    p "(Eu tenho o momento perfeito para unir eles!)"
    p "(Me sinto como se tivesse ganho na loteria.)"
    p "Bom... Vamos esperar, então."

    if romSer == True:
        p "Porém... Eu ainda sinto como se alguém estivesse me observando..."
        p "Isso é de dar calafrios."
        p "... Espero que seja só o Contador de Histórias."
        p "Agora vou procurar um jeito de me comunicar com Marion."
    if morSer == True:
        p "Agora vou procurar um jeito de me comunicar com Marion."

    n "Você volta ao corredor principal."
    scene varandamanha
    with fade
    n "E começa à matutar sobre como entrará em contato com Marion."
    p "Ao menos eu sei que ele parece conseguir fazer linguagem corporal."
    p "É algo à se pensar."
    n ""
    jump contodia1parte2

label contodia1parte2:

    scene varandadia
    with dissolve
    n ""
    p "..."
    p "Eles vão vir me buscar, não é?"
    p "... Ou eles foram sem mim."
    p "O que não é má ideia, meu plano é que eles fiquem juntos, não é?"
    n "Você ouve passos se aproximando."

    if romSer == True:
        n "E a mesma sensação de ser observado também."
        p "..."
        p "... Marion?"
        show servaranda2
        with dissolve
        p "(Eu sabia.)"
        p "Olá, Marion."
        show servaranda10
        hide servaranda2
        sm "...?"
        p "Ah, você quer saber como eu sei seu nome? Chris me falou."
        show servaranda12
        hide servaranda10
        sm "!"
        p "Pelo que ele disse, pode não ser seu nome."
        p "Você quer tentar me dizer seu nome?"
        show servaranda14
        hide servaranda12
        sm "..."
        p "... Disse algo errado?"
        show servaranda9
        hide servaranda14
        sm "--."
        p "... Posso te fazer uma outra pergunta?"
        show servaranda7
        hide servaranda9
        sm "..."
        n "Você se aproxima um pouco de Marion para sussurrar:"

        menu:
            "Foi você que me salvou no oceano?":
                show servaranda8
                hide servaranda7
                sm "!!"
                p "... Você tem minha gratidão."
            "Você é uma sereia, e por isso não consegue falar, não é?":
                show servaranda5
                hide servaranda7
                sm "..."
                p "Eu acertei, não é?"
                show servaranda16
                hide servaranda5
                sm "...!"
                p "Calma, eu não vou contar para ninguém!"
                show servaranda15
                hide servaranda16
                p "Eu juro. Se te alivia, meu objetivo não é interferir no que quer que você esteja fazendo aqui."
        p "(Até que dá para entender um pouco ele...)"

    if morSer == True:
        p "Ah? Chris voltou?"
        show servaranda5
        with dissolve
        p "Ah, é você!"
        sm "..."
        p "... Algum problema?"
        show servaranda6
        hide servaranda5
        sm "..."
        p "Olha, vamos começar com o pé direito."
        n "Você diz seu nome."
        p "O Príncipe me disse que você se chama Marion."
        show servaranda7
        hide servaranda6
        p "... Mas eu entendi que esse talvez não seja seu nome."
        p "Posso te fazer uma pergunta?"
        show servaranda7
        hide servaranda9
        sm "..."
        n "Você se aproxima um pouco de Marion para sussurrar:"
        menu:
            "Foi você que me salvou no oceano?":
                show servaranda8
                hide servaranda7
                sm "!!"
                p "... Você tem minha gratidão."
                sm "..."
            "Você é uma sereia, e por isso não consegue falar, não é?":
                show servaranda5
                hide servaranda7
                sm "..."
                p "Eu acertei, não é?"
                show servaranda3
                hide servaranda5
                sm "--."
                p "Calma, eu não vou contar para ninguém!"
                show servaranda5
                hide servaranda3
                p "Eu juro, eu quero te ajudar."
                show servaranda6
                hide servaranda3
        p "(Na verdade, é bem fácil entender ele.)"

    p "... Então, você veio me buscar por causa de cavalgar com o Chris, certo?"
    show servaranda1
    sm "!!!"
    p "Ótimo! Então vamos, vai ser uma tarde divertida!"
    p "(Eu espero, porque até onde eu me lembro, eu não sei cavalgar.)"
    hide servaranda1
    scene varandadia
    with dissolve
    p "Vamos lá."
    scene escurototal
    with fade
    n "Você segue Marion pelo palácio."
    n "Apesar do Príncipe ter dito que a Sereia está aqui há só um dia, ele parece muito familiarizado com o local, como se já tivesse visto este palácio inúmeras vezes."
    n "Nenhuma vez ele se virou para checar como você estava, como se esperasse que você soubesse o caminho também."
    p "(... Eu me lembro vagamente que deveria doer para andar na terra.)"
    p "(Marion parece não sentir dor nenhuma...)"
    p "(Suspeito...)"
    scene floresta
    with fade
    n "Você se reune com Chris na borda de terra do palácio. A floresta é de pinheiros fragrantes, digno de um conto de fadas."
    p "(Suspeito que pinheiros não crescem perto do mar, mas se essa é a história que o Fantasma antes de mim escreveu, não vou julgar.)"
    n "Chris te ajudou à montar em um cavalo, mas no fim você decidiu apenas acompanhar os dois."
    n "Eventualmente, parece que ambos se esqueceram que você estava com eles e começaram à falar entre si."
    n "Ou melhor, Chris começou à falar enquanto Marion só concorda ou discorda com a cabeça."
    pc "E no fim, eles voam para o sul quando o inverno chega."
    p "(Apesar de Marion estar ouvindo Chris atentamente, parece que ele já ouviu isso muitas vezes...)"
    pc "Só você mesmo para me ouvir falando nestes assuntos, não é mesmo?"
    n "Marion assente com a cabeça."
    pc "... Marion, você é realmente um bom ouvinte, um bom amigo."
    p "(Ele está aqui há só um dia, não é? Será que o Chris mentiu sobre isso?)"
    pc "Eu bem que gostaria de poder estar sempre com alguém como você."
    n "Você percebe que Marion sorri, mas desvia o olhar entristecido. Parece que ele já ouviu essa conversa antes e sabe exatamente o que Chris dirá em seguida."
    pc "Por isso que você é como um irmão para mim."
    p "(... Shuuush, isso é pior que a temida Zona da Amizade.)"
    pc "Porque eu sinto como se nós nos conhecessemos há bem mais tempo."
    p "(Opa!)"
    pc "Há pelo menos um mês..."
    p "(... Continua, não enrola, eu preciso saber!)"
    pc "Faz cerca de um mês que eu sinto a sensação que tenho quando você está por perto. Bom, do jeito que você é quietinho, eu devo não ter percebido."
    n "Marion assente com a cabeça vigorosamente."
    pc "Eu sabia! Sabia que já te conhecia antes!"
    n "Marion gesticula com a mão, fazendo o movimento de passá-la para trás."
    p "(Será que isso significa que faz bem mais de um mês?)"
    pc "... Você quer que voltemos ao palácio?"
    p "(Chris realmente não é muito brilhante...)"
    n "Marion abaixa a cabeça derrotado, mas não diz nada. Depois de um tempo, ele concorda."
    pc "... A gente ficou bem pouco, mas eu imagino que você esteja cansado."
    n "Marion assentiu, um pouco triste."
    pc "Tudo bem, vamos voltar então."
    p "É, eu também estou sentindo cansaço."
    n "Vocês decidem voltar para o palácio."
    scene escurototal
    with dissolve
    n ""
    stop music
    n "Assim que chegam, Marion te dá um tapinha nas costas."
    n "É como se ele quisesse falar algo, mas nada diz."
    n "O resto de seu dia é sem mais eventos, pois os dois se retiraram para atividades que não te envolvem."
    p "(No fim isso seja uma boa oportunidade para entrar em contato com o Contador de Histórias.)"
    scene varandanoite
    with dissolve
    play music "audio/noite.mp3"
    n ""
    p "Muito bem."
    p "Contador de Histórias, eu estou tendo uma dificuldade no momento."
    p "..."
    p "Eu esperava que você me respondesse, sabia?"
    p "..."
    p "Talvez se eu..."
    p "... Se eu tentasse conhecer um pouco melhor a situação de dentro?"
    p "Isso mesmo."
    n ""
    jump encontronoturno

label encontronoturno:

    menu:
        "Ir atrás de Marion":
            $romSer2 = True
            p "Marion no fim das contas é o protagonista desta história."
            p "Se tem alguém que tenho de ficar de olho, é ele."
            p "... Vamos nessa."
            if romSer == True:
                p "Apesar que o Marion certamente já sabe onde estou."
                p "Desde que vi ele pela primeira vez, parece que tem algo me assistindo."
                p "E pelo que ouvi hoje, ele parece ser do tipo silencioso que observa muito antes de agir."
                p "... Tipo um tubarão."
            if morSer == True:
                p "No fim das contas, se eu conseuir entender ele, eu posso traduzir tudo para o Chris."
                p "E aí, final feliz."
            n "Você vai atrás de Marion."
            scene varandanoite
            with fade
            n ""
            p "Marion? Você está aí?"
            show noitesereia6
            with dissolve
            sm "..."
            p "Que bom te ver de novo."
            sm "..."
            p "... Tem algo te incomodando?"
            p "(É claro que tem algo incomodando ele.)"
            if romSer == True:
                p "(... Olhando ele agora, ele parece bem vulnerável.)"
                p "... Marion?"
                show noitesereia2
                hide noitesereia6
                sm "..."
                sm "... Perdão."
                p "(!!)"
                p "Você consegue falar?!"
                sm "Apenas porque só você está me ouvindo agora."
                sm "Eu soube no instante que te vi que você era mais um dos vários Sonhadores."
                p "..."
                p "(O Contador de Histórias não me avisou que eles seriam conscientes de minha passagem, ou de outros!)"
                p "... Eu não sei do que você está falando."
                sm "Sabe. Por favor, não tente me fazer de bobo, eu vi vários como você antes."
                show noitesereia1
                hide noitesereia2
                sm "Vocês veem, aparecem de repente no navio e eu sempre salvo vocês. De repente vocês acordam e ficam muito interessados em minha vida e a do Chris."
                sm "... Sendo bem sincero, eu não aguento mais."
                sm "Vocês... Não entendem o que é reviver isso todas as vezes."
                p "Marion..."
                sm "Seja o que for que você esteja buscando, por favor, encontre logo e saia. Me deixe em paz."
                show noitesereia3
                hide noitesereia2
                sm "Vocês... Não sabem o que é estar com quem você ama... E ser tirado disso todas as vezes."
                sm "... Se você realmente não pode sair, só não termine a história."
                sm "Se você fizer a história prosseguir... Eu..."
                sm "... Eu nem sequer consigo te falar o que pode acontecer."
                p "Marion, não era para você ter consciência que é... Um personagem em um livro, não é?"
                sm "... Eu sei. Mas eu sou o primeiro capítulo deste livro... Tantos passaram por mim que eu comecei à ter lembranças vestigiais. Ninguém além de mim tem essas lembranças."
                show noitesereia4
                hide noitesereia3
                sm "No começo eu tentei ver se o Chris se lembrava de algo... Mas ele sempre, sempre diz as mesmas coisas."
                sm "E junto dos demais personagens, minha voz é inexistente."
                p "... Marion, você entende que eu preciso ir para casa, não é?"
                sm "Pois que vá, só não prossiga a história."
                n "Um barulho é ouvindo."
                sm "... !! ..."
                n "E Marion perdeu sua voz novamente. Incapaz de se comunicar com você, ele se vai."
                hide noitesereia1
                hide noitesereia4
                with dissolve
                p "... Uou."
                p "Depois dessa... Eu acho que vou dormir..."
            if morSer == True:
                p "(Ele parece bem triste, é estranho.)"
                p "Marion, pode confiar em mim."
                show noitesereia5
                hide noitesereia6
                sm "..."
                sm "Posso mesmo?"
                p "(O QUÊ?!)"
                p "Você... Consegue falar?"
                sm "Apenas porque só você está me ouvindo agora."
                sm "Eu reconheço... Magia, quando vejo. E ela está te envolvendo como um lençol."
                p "..."
                p "(O Contador de Histórias não me avisou disso!)"
                p "É... Magia! Como a que te transformou em humano!"
                sm "... É, é mais ou menos isso."
                show noitesereia1
                hide noitesereia5
                sm "Por isso que só você é capaz de me ouvir."
                p "..."
                p "(Que explicação meia boca... Parece que ele está escondendo algo, mas não sei o que é.)"
                sm "Sim, tem algo me incomodando. Você."
                p "Eu?"
                sm "Sim, o fato que tem magia em você me... Deixa inquieto."
                p "..."
                sm "Seja o que for que veio fazer aqui, só não entre em meu caminho."
                p "... Caminho?"
                sm "Eu não sou obrigado à lhe dar detalhes sobre."
                show noitesereia6
                hide noitesereia1
                sm "Apenas não interfira e volte para sua casa."
                p "Marion..."
                n "Marion dá às costas e se vai."
                hide noitesereia6
                with dissolve
                p "... Eu sei que eu deveria dormir, mas estou... Com bastante pavor."

        "Ir atrás de Chris":
            $morSer2 = True
            p "Se Chris é o interesse romântico, eu deveria saber do que ele gosta."
            p "Isso pode me ajudar à ajudar o Marion."
            p "E se ele se sair bem, eu me saio bem também."
            n "Você vai atrás de Chris."
            show noiteprin1
            with dissolve
            pc "Boa noite, não consegue dormir?"
            p "Não é isso, eu vim aqui perguntar sobre..."
            pc "O Marion, não é?"
            if romSer == True:
                p "Sim..."
                pc "..."
                p "... Vocês hoje conversaram coisas que me fazem pensar que ele sabe bem mais do que aparenta."
                show noiteprin3
                hide noiteprin1
                pc "... Eu tenho certeza disso."
                pc "E às vezes acho que tem alguma ligação com eu ter certeza que o conheço há bem mais de um dia, semana ou mês."
                pc "É como se eu o conhecesse há anos... Mas não sei onde colocar esse tipo de memória."
                p "..."
                p "Eu na verdade ia dizer que ele parece... Uh... Interessado em você."
                pc "Eu estou ciente disto. Porém como um príncipe, não devo me deixar levar por um sentimento criado em minha cabeça, quando na realidade só vi esse rapaz por um dia."
                p "... Acaso se lembra de quem te salvou do naufrágio no navio?"
                pc "..."
                pc "Você vai me dizer que foi o Marion, não é?"
                p "... Como sabia?"
                pc "Tive essa impressão."
                pc "Seja como for, não importa o que diga, meus deveres ainda estão acima de qualquer sentimento."
                p "..."
                pc "Tenha uma boa noite."
                n "Chris se vai."
                hide noiteprin3
                with dissolve
                p "..."
                p "Algo não está certo..."
                p "Será que é porque ele sentiu a sensação de estar sendo vigiado...?"
                p "... Marion, seja o que você estiver tramando... É assustador."
            if morSer == True:
                p "É sobre ele sim."
                pc "..."
                p "Já reparou como ele parece sempre saber o que você vai dizer?"
                show noiteprin2
                hide noiteprin1
                pc "Uau, para ser honesto, nunca reparei."
                pc "Bom, isso só deve significar que nós somos como irmãos, não é? Afinal, se ele me conhece tão bem assim..."
                p "(... Marion, você tem um gosto por rapazes meio lentos, eu sinto pena de você.)"
                p "Eu na verdade ia dizer que ele parece... Uh... Interessado em você."
                pc "É claro que está, eu sou o príncipe dessas terras, é claro que vai ter pessoas interessadas em serem minhas amigas."
                p "... Ah..."
                p "(... Agora eu perdi no argumento.)"
                p "Você se lembra de como foi salvo do naufrágio?"
                show noiteprin3
                hide noiteprin2
                pc "..."
                pc "Eu me lembro de alguém cantando quando despertei na praia, mas não vi ninguém."
                pc "Porém aquela voz... Eu me apaixonei por aquela voz."
                pc "Se eu soubesse o dono dessa voz..."
                p "(E Marion é mudo. Droga, não adianta eu dizer que ele é o salvador.)"
                pc "Bom, eu não deveria divagar nesses assuntos."
                pc "..."
                pc "Seja como for, eu tive a impressão que você ia me dizer que Marion é a pessoa por trás de meu salvamento."
                p "..."
                pc "Mas isso não faria sentido, ele apareceu naufragado dias depois que eu retornei."
                p "..."
                pc "Seja como for, não sinta ciumes dele, vocês dois podem ser meus amigos."
                p "Não é bem isso, mas você tem minha gratidão."
                pc "... Olhe, se é sobre um romance, eu tenho meus deveres como príncipe e... Sendo sincero, eu conheço vocês por menos de uma semana."
                pc "Tenha uma boa noite."
                p "Você também."
                n "Chris se vai."
                hide noiteprin3
                with dissolve
                p "Unir esses dois... Vai ser quase impossível."
                p "Como eu vou alcançar o final assim?"
    n "Você decide ir para seu quarto dormir."
    scene quarto
    with fade
    n "E pela primeira vez, você parece dormir tranquilo."
    scene escurototal
    with fade
    n ""
    stop music
    jump festa

label festa:
    play music "audio/valsa.mp3"
    n "Os dias correram ao longo de uma semana, sem maiores eventos."
    if romSer == True:
        n "Marion é um pouco estranho com seu hábito de observar as pessoas de longe."
        if romSer2 == True:
            n "Ele na verdade está te observando, se você irá interferir na históra, como ele disse para você não fazer."
            n "É minimamente assustador."
        if morSer2 == True:
            n "Mas, é como Chris disse, deve ser só o hábito dele."
            n "Definitivamente não há nada para se preocupar."
            n "Mas Chris parece triste com algo, deve ser o tal peso da coroa."
    if morSer == True:
        n "Chris parece bem mais próximo de Marion, porém algo parece estar incomodando ele."
        n "Apenas é difícil saber o quê."
        if romSer2 == True:
            n "Pode ser o tal sentimento de conhecer Marion há muito tempo, mas existir um dever bem maior em mãos."
            n "Isso é realmente doloroso."
        if morSer2 == True:
            n "Provavelmente ele ainda está incomodado com aquela conversa."
            n "Ou deve ser o tal dever da coroa."
    n "O importante é que hoje é um dia de festa."
    n "Provavelmente um novo aniversário."
    n "É estranho que tenham escolhido o cais, mas é bem mais seguro que outra festa de navio."

    scene praiafinal
    with dissolve
    m "Ouviu as boas novas, rato afogado?"
    p "(Rato afogado?)"
    p "(Esse cara de novo...)"
    p "Que boas novas?"
    m "Anunciaram o noivado de nosso príncipe com uma princesa de um reino próximo."
    p "..."
    p "(... Oh não.)"
    p "(Finalmente entendi o que o Contador de Histórias queria dizer com esse conto ser uma tragédia.)"
    p "(Espere... Isso só significa que Marion vai voltar à ser uma sereia, não é?)"
    p "... Meus parabéns para ele, eu acho."
    m "E para todos nós!"
    p "(Preciso encontrar eles! O quanto antes!)"
    n "Você corre em direção ao palácio."
    scene parede
    with fade
    n ""
    scene parede
    with fade
    n ""
    if romSer == True:
        p "Onde eles estão?"
        p "Por que eu não consigo alcançar eles...?"
        if romSer2 == True:
            scene varandadia
            with fade
            n ""
            show servaranda15
            with dissolve
            sm "A história prosseguiu."
            p "Marion!"
            sm "... E agora que ele está noivo dela, eu estou destinado ao final."
            p "... Só significa que você vai retornar ao mar, não é?"
            sm "Antes fosse. Antes fosse..."
            sm "Mas, tudo bem, você se manteve na linha por essa semana..."
            sm "Eu só vou ter de esperar por alguns anos até que eu possa ver Chris novamente."
            p "... Me desculpe."
            sm "... Não é bem culpa sua. Cedo ou tarde esse dia chegaria. Eu peço apenas que quando esse pesadelo acabar, você escreva essa história como se nosso tempo juntos fosse mais longo."
            p "... Darei meu melhor."
            sm "... Te vejo na festa."
            n "Marion se vai."
            hide servaranda15
            with dissolve
            p "... Me desculpa..."
        if morSer2 == True:
            scene varandadia
            with fade
            n ""
            show servaranda15
            with dissolve
            sm "... Aconteceu o que eu temia."
            p "Marion!"
            p "Você fala!"
            sm "Apenas porque apenas você pode me ouvir agora."
            p "... Mas por quê?"
            sm "Eu vou explicar em breve..."
            sm "... E agora que ele está noivo dela, eu já sei o que me aguarda."
            p "... Só significa que você vai retornar ao mar, não é?"
            sm "Antes fosse. Antes fosse..."
            sm "... Meu pai, minha avó e minhas irmãs... Certamente vão tentar me tirar dessa."
            sm "Mas, eu não vou seguir o plano deles... Como sempre faço."
            p "... Como assim, como você sempre faz?"
            sm "... Vamos dizer que ser o protagonista de uma história tem suas vantagens."
            p "... O tempo todo você sabia..."
            sm "... Sim. Eu sabia. Sabia inclusive que você não era desse mundo, então as regras dele não se aplicam à você."
            sm "A razão que só você me escuta, é que não importa o que você diga que me ouviu dizer, ninguém pode me ouvir, então não há razões para acreditarem em você."
            sm "... Por favor, cuide bem do Chris quando a históra acabar antes de você voltar para casa."
            p "Me desculpa..."
            n "Marion se vai."
            hide servaranda15
            with dissolve
            p "... Se ele é consciente... Significa que ele assisiu tudo isso? Inúmeras vezes?"
            p "... Agora entendi o motivo que o Contador de Histórias disse que era uma maldição."
    if morSer == True:
        p "Onde eles estão?"
        p "Por que eu não consigo alcançar eles...?"
        if romSer2 == True:
            scene varandadia
            with fade
            n ""
            show servaranda15
            with dissolve
            sm "A história prosseguiu."
            p "Marion!"
            sm "... E agora que ele está noivo dela, eu estou destinado ao final."
            p "... Só significa que você vai retornar ao mar, não é?"
            sm "Antes fosse. Antes fosse..."
            sm "Mas, tudo bem..."
            sm "Eu só vou ter de esperar por alguns anos até que eu possa ver Chris novamente."
            p "... Me desculpe."
            sm "... Não é culpa sua. Cedo ou tarde esse dia chegaria."
            p "... Darei meu melhor."
            sm "... Te vejo na festa."
            n "Marion se vai."
            hide servaranda15
            with dissolve
            p "... Me desculpa..."
        if morSer2 == True:
            scene varandadia
            with fade
            n ""
            show servaranda15
            with dissolve
            sm "... Aconteceu o que eu temia."
            p "Marion!"
            p "Você fala?!"
            sm "Apenas porque aqueles de fora deste mundo podem me ouvir... Mas eu explico depois."
            sm "... E agora que ele está noivo dela, eu já sei o que me aguarda."
            p "... Só significa que você vai retornar ao mar, não é?"
            sm "Antes fosse. Antes fosse..."
            sm "... Meu pai, minha avó e minhas irmãs... Certamente vão tentar me tirar dessa."
            sm "Mas, eu não vou seguir o plano deles... Como sempre faço."
            p "... Como assim, como você sempre faz?"
            sm "... Vamos dizer que ser o protagonista de uma história tem suas vantagens."
            p "... O tempo todo você sabia..."
            sm "... Sim. Eu sabia."
            sm "A razão que só você me escuta, é que não importa o que você diga que me ouviu dizer, ninguém pode me ouvir, então não há razões para acreditarem em você."
            sm "... Por favor, cuide bem do Chris quando a históra acabar antes de você voltar para casa."
            p "Me desculpa..."
            sm "... No fim eu me diverti bastante. Te vejo na festa."
            n "Marion se vai."
            hide servaranda15
            with dissolve
            p "... Se ele é consciente... Significa que ele assisiu tudo isso? Inúmeras vezes?"
            p "... Agora entendi o motivo que o Contador de Histórias disse que era uma maldição."
    n "Com tristeza e pesar no coração, você vai até o cais para atender a festa."
    scene praiafinal
    with fade
    n ""
    stop music
    n ""
    jump finalcomum

label finalcomum:
    play music "audio/final.mp3"
    scene poente
    with dissolve
    p "... É um por do sol lindo. É uma pena que seja a última vez que eu vá ver eles..."
    p "No fim, a voz da princesa é a que ele ouviu."
    p "... Então nunca houve chance para Marion...?"
    p "E no fim... Eu condenei Marion para um destino cruel."
    p "Eu... Vou falar com Marion."
    if romSer == True:
        if romSer2 == True:
            jump finalROM
        if morSer2 == True:
            jump finalNEU
    if morSer == True:
            if morSer2 == True:
                jump finalMOR
            if romSer2 == True:
                jump finalNEU
label finalROM:
    show finalespuma
    with dissolve
    p "Marion..."
    sm "Eu estava te esperando, Sonhador."
    sm "..."
    sm "... No fim ele se casou com a princesa, como a história deve seguir..."
    sm "Haverá um dia em que possamos ficar juntos?"
    sm "... Eu já tive tantos nomes, tantas formas..."
    sm "Marina, Ariel, Rielle, Marion..."
    sm "Não importa como me escrevam, sempre me lembrarão por eu ter tido compaixão pela princesa e ter poupado a vida do príncipe."
    p "... O que quer dizer com isso?"
    sm "Durante a festa, você não teve como ver, pois é único de mim por ser o protagonista..."
    sm "Minhas irmãs vieram com uma faca da Bruxa do Mar. Disseram que se eu matasse o príncipe, eu poderia voltar à ser uma sereia."
    sm "E eu sempre recuso, pois não desejo causar dor à princesa."
    sm "... Por que você teve de me escrever gentil em meu coração, Pai?"
    p "Pai?"
    sm "... É como gosto de chamar o meu autor."
    sm "Eu estou contantemente mudando pelas mãos dos autores e dos vários que entraram nesse mundo, mas meu cerne é sempre intacto."
    sm "Eu sou amor. Amor que não é egoísta."
    p "... Marion..."
    sm "... Mas você sabia disso... Sabia e... Não me ouviu."
    show finalagua
    hide finalespuma
    p "Marion..."
    sm "... Eu não minto, que tenho vontade de te afogar e te condenar à assistir essa história se repetir..."
    if naonada == True:
            sm "Especialmente porque vi que você não é capaz de nadar."
    if nada == True:
            sm "Porque mesmo que você saiba nadar, você não é capaz de competir contra as ondas."
    menu:
        "Afastar-se":
            $espuma = True
            n "Você se afasta, temente pela informação de Marion."
            n "Ele, por outro lado, parece mais irritado com essa atitude."
            sm "... E pelo modo que está agindo... Algo me diz que eu não devo ter compaixão por você."
            sm "É, eu não deveria ter te salvo naquele acidente..."
            sm "Felicite-se, Sonhador."
            sm "Eu me tornarei espuma e você se tornará parte dos fantasmas que perderam suas vidas dentro deste conto maldito."
            scene poente
            n "Marion te agarra fortemente contra o peito e se atira no oceano."
            scene fundomar1
            with fade
            n "Enquanto o ar vai te escapando dos pulmões, você consegue sentir que Marion está cada vez mais te puxando para o fundo."
            n "Será impossível de voltar para a superfície."
            n "Aos poucos você percebe que o corpo de Marion está se dissolvendo."
            n "Um choro dolorido parece estar escapando dele, condenado à mais um ciclo de sofrimento."
            n "E você estará com ele para testemunhar isto."
            stop music
            scene escurototal
            with dissolve
            jump gameover

        "Permanecer no lugar":
            n "Você fica firme em seu lugar, inalterado pela provocação de Marion."
            p "(No fundo, eu sei que ele não é capaz de fazer isso. A menos que eu dê um motivo.)"
            p "(Chegamos até aqui, não posso demonstrar ter medo dele.)"

    show finalespuma
    hide finalagua
    sm "Mas, eu não o farei."
    sm "Pelo simples fato que confiei em você para cuidar do Chris quando eu me for e que reescreva uma história melhor que o Sonhador anterior."
    sm "Eu vejo que você simpatizou comigo... Então por isso eu estou confiando em você."
    sm "Adeus, Sonhador."
    p "... Adeus, Marion."
    sm "Eu não vou dizer para você não chorar."
    p "É porquê nem todas as lágrimas são ruins...?"
    sm "Não. É porque apenas aqueles que possuem uma alma, são capazes disso."
    sm "Sereias não choram, e por isso sua dor é imensurável."
    p "... Eu prometo, Marion, eu prometo escrever uma versão onde você e Chris... Possam ficar juntos."
    sm "Obrigado. Só... Não precisa colocar a Bruxa do Mar como vilã, no fim, ela me advertiu que era tolice minha vir até aqui."
    n "Você e Marion se abraçam."
    n "Quando os últimos raios de sol começam à desaparecer, vocês se soltam e Marion se atira ao mar."
    hide finalespuma
    with dissolve
    n "Seu rosto é sereno enquanto seu corpo se desfaz em espuma marinha."
    n "Uma brisa suave toca seu rosto na testa, é gelado, porém gentil como um beijo de um bom amigo."
    p "... Vá em paz, Marion."
    n "Quando você se volta para trás, você consegue ver Chris se aproximando."
    n "Ele passa direto por você e observa a espuma."
    show prinfinal1
    with dissolve
    n ""
    pc "... Ele já foi, não é?"
    p "... Já."
    pc "... Ele foi em paz?"
    p "... Sim."
    show prinfinal2
    hide prinfinal1
    pc "... Confio em você."
    pc "Afinal, ele certamente deveria confiar, para te deixar ver ele partir."
    p "... Então você também sabia?"
    pc "... Não ao certo, mas eu tinha a impressão que sim."
    show prinfinal3
    hide prinfinal2
    pc "... Eu espero que um dia... Alguém nos escreva juntos."
    p "... Eu o farei."
    n "Você sente um calor em sua mochila."
    pc "Obrigado..."
    n "Ao verificar o que é, você toca no Codex Fabula, descobrindo que essa era a fonte de calor."
    n "E o mundo se dissolve ao seu redor."
    stop music
    play music "audio/devolta.mp3"
    scene sala2
    with pixellate
    p "Espere!"
    p "... Eu voltei..."
    c "Bem vindo de volta."
    show contador
    with dissolve
    c "Fico feliz que esteja bem."
    p "..."
    c "... Eu olhei tudo."
    show contadordesapontado
    hide contador
    c "... Sinto muito."
    p "Por isso que você disse que era uma tragédia...?"
    c "Sim. Eu, assim como meu antigo tutor e outros... Todos nós mantivemos a Sereia morrendo."
    p "Marion! O nome dele é Marion!"
    c "... Marion? Oh, era esse o nome que eu tinha dado para ele?"
    p "..."
    p "Ele me pediu para que eu reescrevesse a história para ser feliz..."
    c "..."
    p "Eu posso fazer isso?"
    c "... Pode, uma vez que acordar desse sonho lúcido e ir para sua vida normal."
    p "... Como eu faço?"
    show contadorconfuso
    hide contadordesapontado
    c "Do jeito tradicional, basta você pegar um lápis e papel e, quando estiver pronto, recolocar no Codex Fabula."
    p "E como eu quebro a maldição do Codex Fabula?"
    c "Eu já disse que não sei ao certo."
    p "..."
    p "Eu vou dar um final feliz para eles... Eu prometi para ele."
    p "Há quanto tempo isso acontece?"
    show contadordesapontado
    hide contadorconfuso
    c "... Hans Christian Andersen, o autor da Pequena Sereia, publicou pela primeira vez esse conto em 1837. A partir daí, bastava que alguém que conhecesse esse conto entrar em contato com o Codex Fabula que ele seria adicionado às suas páginas."
    p "... Isso é quase duzentos anos... Duzentos anos..."
    c "... Vá. Eu quero que você escreva sua versão."
    show contadorcontente
    hide contadordesapontado
    c "E dê para ele um final feliz."
    c "Irei te puxar para fora desse sonho."
    c "Até a próxima vez que dormir."
    p "Até a próxima vez, Contador de Histórias."
    hide contadorcontente
    with dissolve
    scene escurototal
    with pixellate
    n "Com um respirar fundo, você se sente sendo colocado em sono novamente."
    n "Mas agora, você sabe que chegou ao final desta jornada e poderá retornar à sua vida."
    show fim
    with dissolve
    n ""
    stop music
    n ""
    n "Pressione qualquer tecla, ou clique em qualquer lugar, para voltar ao menu principal."

    return

label finalMOR:
    show finalespuma
    with dissolve
    p "Marion..."
    sm "Eu estava te esperando."
    sm "..."
    sm "... No fim ele se casou com a princesa, como a história deve seguir..."
    sm "Haverá um dia em que possamos ficar juntos?"
    sm "Não importa a forma ou nome, sempre me lembrarão por eu ter tido compaixão pela princesa e ter poupado a vida do príncipe."
    p "... O que quer dizer com isso?"
    sm "Eu já te disse que minha família iria interferir, mas eu não iria seguir o plano deles. O plano é que se eu matar o príncipe, eu poderia voltar à ser uma sereia."
    sm "E eu sempre recuso, pois não desejo causar dor à princesa."
    sm "... Por que eu nunca posso descontar minha raiva?"
    sm "Eu estou contantemente mudando pelas mãos dos autores e dos vários que entraram nesse mundo, mas meu cerne é sempre intacto."
    sm "... O cerne de uma criança que sente compaixão pelo próximo, porque isso é o correto."
    p "... Marion..."
    sm "Por favor, cuide bem do Chris quando eu me for. Ao menos diga para ele que eu o via como bem mais que um amigo ou irmão."
    sm "Eu vejo que você simpatizou comigo... Então por isso eu estou confiando em você."
    sm "Adeus, Sonhador."
    p "... Adeus, Marion."
    sm "Eu não vou dizer para você não chorar."
    p "É porquê nem todas as lágrimas são ruins...?"
    sm "Não. É porque apenas aqueles que possuem uma alma, são capazes disso."
    sm "Sereias não choram, e por isso sua dor é imensurável."
    p "... Eu prometo, Marion, eu prometo que vou cuidar do Chris... E de você."
    sm "Obrigado. Só... Se lembre que a Bruxa do Mar não foi ruim comigo, no fim, ela me advertiu que era tolice minha vir até aqui."
    sm "Obrigado. Você não ter interferirido, mesmo que doa... Me permite ter uma alma."
    sm "E eu sinto alívio quando sei que posso chorar, assim como vocês."
    p "Te darei uma alma desde o começo."
    sm "... Eu acredito que sim."
    n "Você e Marion se abraçam."
    n "Quando os últimos raios de sol começam à desaparecer, vocês se soltam e Marion se atira ao mar."
    hide finalespuma
    with dissolve
    n "Seu rosto é sereno enquanto seu corpo se desfaz em espuma marinha."
    n "Uma brisa suave toca seu rosto na testa, é gelado, porém gentil como um beijo de um bom amigo."
    p "... Vá em paz, Marion."
    n "Quando você se volta para trás, você consegue ver Chris se aproximando, porém antes que ele pudesse dizer algo, você sente um forte calor em sua bolsa."
    n "Ao verificar o que é, você toca no Codex Fabula, descobrindo que essa era a fonte de calor."
    n "E o mundo se dissolve ao seu redor."
    stop music
    play music "audio/devolta.mp3"
    scene sala2
    with pixellate
    p "Espere!"
    p "... Eu voltei..."
    c "Bem vindo de volta."
    show contador
    with dissolve
    c "Fico feliz que esteja bem."
    p "..."
    c "... Eu olhei tudo."
    show contadordesapontado
    hide contador
    c "... Sinto muito."
    p "Por isso que você disse que era uma tragédia...?"
    c "Sim. Eu, assim como meu antigo tutor e outros... Todos nós mantivemos a Sereia morrendo."
    p "Marion! O nome dele é Marion!"
    c "... Marion? Oh, era esse o nome que eu tinha dado para ele?"
    p "..."
    p "Ele me pediu para tomar conta do Chris... Significa que ele quer que eu mude a história?"
    c "..."
    p "Eu posso fazer isso?"
    c "... Pode, uma vez que acordar desse sonho lúcido e ir para sua vida normal."
    p "... Como eu faço?"
    show contadorconfuso
    hide contadordesapontado
    c "Do jeito tradicional, basta você pegar um lápis e papel e, quando estiver pronto, recolocar no Codex Fabula."
    p "E como eu quebro a maldição do Codex Fabula?"
    c "Eu já disse que não sei ao certo."
    p "..."
    p "Eu vou dar um final feliz para eles... Eu prometi para ele."
    p "E mesmo se eu não puder dar, eu vou tentar. Eu não me importo, existem muitas versões de contos de fadas por aí, inclusive uma em que eles ficam juntos! Eu colocarei no Codex Fabula!"
    p "Há quanto tempo isso acontece?"
    show contadordesapontado
    hide contadorconfuso
    c "... Hans Christian Andersen, o autor da Pequena Sereia, publicou pela primeira vez esse conto em 1837. A partir daí, bastava que alguém que conhecesse esse conto entrar em contato com o Codex Fabula que ele seria adicionado às suas páginas."
    p "... Isso é quase duzentos anos... Duzentos anos..."
    c "... Vá. Eu quero que você escreva sua versão."
    show contadorcontente
    hide contadordesapontado
    c "E dê para ele um final feliz."
    c "Irei te puxar para fora desse sonho."
    c "Até a próxima vez que dormir."
    p "Até a próxima vez, Contador de Histórias."
    hide contadorcontente
    with dissolve
    scene escurototal
    with pixellate
    n "Com um respirar fundo, você se sente sendo colocado em sono novamente."
    n "Mas agora, você sabe que chegou ao final desta jornada e poderá retornar à sua vida."
    show fim
    with dissolve
    n ""
    stop music
    n ""
    n "Pressione qualquer tecla, ou clique em qualquer lugar, para voltar ao menu principal."

    return

label finalNEU:
        show finalespuma
        with dissolve
        p "Marion..."
        sm "Eu estava te esperando."
        sm "..."
        sm "... No fim ele se casou com a princesa."
        sm "Haverá um dia em que possamos ficar juntos?"
        sm "Não importa a forma ou nome, sempre me lembrarão por eu ter tido compaixão pela princesa e ter poupado a vida do príncipe."
        p "... O que quer dizer com isso?"
        sm "Minha família não quer que eu morra, então eles tem um plano: O plano é que se eu matar o príncipe, eu poderia voltar à ser uma sereia."
        sm "E eu sempre recuso, pois não desejo causar dor à princesa."
        sm "... Assim como deve ser. Só porque você está em dor, nada justifica causar dor aos outros."
        p "... Marion..."
        sm "Por favor, cuide bem do Chris quando eu me for. Ao menos diga para ele que eu o via como bem mais que um amigo ou irmão."
        sm "Eu vejo que você simpatizou comigo... Então por isso eu estou confiando em você."
        sm "Adeus, Sonhador."
        p "... Adeus, Marion."
        sm "Eu não vou dizer para você não chorar."
        p "É porquê nem todas as lágrimas são ruins...?"
        sm "Não. É porque apenas aqueles que possuem uma alma, são capazes disso."
        sm "Sereias não choram, e por isso sua dor é imensurável."
        p "... Eu prometo, Marion, eu prometo que vou cuidar do Chris... E de você."
        sm "Obrigado. Só... Se lembre que a Bruxa do Mar não foi ruim comigo, no fim, ela me advertiu que era tolice minha vir até aqui."
        sm "Obrigado. Você não ter interferirido, mesmo que doa... Me permite ter uma alma."
        sm "E eu sinto alívio quando sei que posso chorar, assim como vocês."
        p "Te darei uma alma desde o começo."
        sm "... Eu acredito que sim."
        n "Você e Marion se abraçam."
        n "Quando os últimos raios de sol começam à desaparecer, vocês se soltam e Marion se atira ao mar."
        hide finalespuma
        with dissolve
        n "Seu rosto é sereno enquanto seu corpo se desfaz em espuma marinha."
        n "Uma brisa suave toca seu rosto na testa, é gelado, porém gentil como um beijo de um bom amigo."
        p "... Vá em paz, Marion."

        if romSer == True:
            if morSer2 == True:
                n "Quando você se volta para trás, você consegue ver Chris se aproximando."
                n "Ele passa direto por você e observa a espuma."
                show prinfinal1
                with dissolve
                n ""
                pc "... Ele já foi, não é?"
                p "... Já."
                pc "... Ele foi em paz?"
                p "... Sim."
                show prinfinal2
                hide prinfinal1
                pc "... Confio em você."
                pc "Afinal, ele certamente deveria confiar, para te deixar ver ele partir."
                p "... Então você também sabia?"
                pc "... Como eu te disse, eu tinha a impressão que eu o conhecia antes."
                show prinfinal3
                hide prinfinal2
                pc "Ele deve ter mais memórias, senão memórias mais vívidas, do que eu..."
                pc "... Eu espero que um dia... Alguém nos escreva juntos."
                pc "... Pois eu, de tantas vezes estar com Marion, ou suas várias outras formas e nomes, me apaixonei por ele."
                pc "... E agora... Eu só o verei quando outra pessoa vier."
                p "... Eu o farei."
                pc "Fará?"
                p "Eu escreverei um final feliz para vocês dois. É uma promessa."
                n "Você sente um calor em sua bolsa."
                pc "... Obrigado... Por favor, faça também que nosso tempo juntos seja mais longo."
        if morSer == True:
            if romSer2 == True:
                n "Quando você se volta para trás, você consegue ver Chris se aproximando."
                n "Ele passa direto por você e observa a espuma."
                show prinfinal1
                with dissolve
                n ""
                pc "... Ele já foi, não é?"
                p "... Já."
                pc "... Ele foi em paz?"
                p "... Sim."
                show prinfinal2
                hide prinfinal1
                pc "... Confio em você."
                pc "Afinal, ele certamente deveria confiar, para te deixar ver ele partir."
                p "... Então você também sabia?"
                pc "... Eu nunca tive certeza até agora."
                show prinfinal3
                hide prinfinal2
                pc "... Porque dói."
                pc "... Eu espero que um dia... Quando essa história recomeçar, possamos finalmente ficarmos juntos."
                pc "... Pois eu, de tantas vezes estar com Marion, ou suas várias outras formas e nomes, me apaixonei por ele."
                pc "... E agora... Eu só o verei quando outra pessoa vier."
                p "... Eu o farei."
                pc "Fará?"
                p "Eu escreverei um final feliz para vocês dois. É uma promessa."
                n "Você sente um calor em sua bolsa."
                pc "... Obrigado... Por favor, faça também que nosso tempo juntos seja mais longo."
        n "Ao verificar o que é, você toca no Codex Fabula, descobrindo que essa era a fonte de calor."
        n "E o mundo se dissolve ao seu redor."
        stop music
        play music "audio/devolta.mp3"
        scene sala2
        with pixellate
        p "Espere!"
        p "... Eu voltei..."
        c "Bem vindo de volta."
        show contador
        with dissolve
        c "Fico feliz que esteja bem."
        p "..."
        c "... Eu olhei tudo."
        show contadordesapontado
        hide contador
        c "... Sinto muito."
        p "Por isso que você disse que era uma tragédia...?"
        c "Sim. Eu, assim como meu antigo tutor e outros... Todos nós mantivemos a Sereia morrendo."
        p "Marion! O nome dele é Marion!"
        c "... Marion? Oh, era esse o nome que eu tinha dado para ele?"
        p "..."
        p "Ele me pediu para tomar conta do Chris... Significa que ele quer que eu mude a história?"
        c "..."
        p "Eu posso fazer isso?"
        c "... Pode, uma vez que acordar desse sonho lúcido e ir para sua vida normal."
        p "... Como eu faço?"
        show contadorconfuso
        hide contadordesapontado
        c "Do jeito tradicional, basta você pegar um lápis e papel e, quando estiver pronto, recolocar no Codex Fabula."
        p "E como eu quebro a maldição do Codex Fabula?"
        c "Eu já disse que não sei ao certo."
        p "..."
        p "Eu vou dar um final feliz para eles... Eu prometi para ele."
        p "E mesmo se eu não puder dar, eu vou tentar. Eu não me importo, existem muitas versões de contos de fadas por aí, inclusive uma em que eles ficam juntos! Eu colocarei no Codex Fabula!"
        p "Há quanto tempo isso acontece?"
        show contadordesapontado
        hide contadorconfuso
        c "... Hans Christian Andersen, o autor da Pequena Sereia, publicou pela primeira vez esse conto em 1837. A partir daí, bastava que alguém que conhecesse esse conto entrar em contato com o Codex Fabula que ele seria adicionado às suas páginas."
        p "... Isso é quase duzentos anos... Duzentos anos..."
        c "... Vá. Eu quero que você escreva sua versão."
        show contadorcontente
        hide contadordesapontado
        c "E dê para ele um final feliz."
        c "Irei te puxar para fora desse sonho."
        c "Até a próxima vez que dormir."
        p "Até a próxima vez, Contador de Histórias."
        hide contadorcontente
        with dissolve
        scene escurototal
        with pixellate
        n "Com um respirar fundo, você se sente sendo colocado em sono novamente."
        n "Mas agora, você sabe que chegou ao final desta jornada e poderá retornar à sua vida."
        show fim
        with dissolve
        n ""
        stop music
        n ""
        n "Pressione qualquer tecla, ou clique em qualquer lugar, para voltar ao menu principal."

        return
label gameover:
    if afogado == True:
        scene over
        with dissolve
        n "Parece que você encontrou um terrível destino de ficar para sempre como um fantasma nas águas do mar."
        n "A Sereia sempre salvará o Príncipe primeiro, se fugir dela, será difícil que ela te salve."
        n "Porém você ainda pode tentar consertar esse erro."
        n ""
        return
    if espuma == True:
        scene over
        with dissolve
        n "Tão próximo de terminar, traiu a confiança que Marion depositou em você."
        n "Alguém que presencia tantos ciclos de dor, morderá a mão que o ajuda, se crer que ela causa sua dor."
        n "Porém, ainda há tempo de consertar este erro."
        n ""
        return
