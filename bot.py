import os
import random
from datetime import datetime, date
from zoneinfo import ZoneInfo

import tweepy


# -----------------------------
# DATA DO ÚLTIMO EPISÓDIO
# -----------------------------

ULTIMO_EPISODIO = date(2024, 3, 6)


# -----------------------------
# CALCULAR DIAS
# -----------------------------

hoje = datetime.now(
    ZoneInfo("America/Sao_Paulo")
).date()

dias = (hoje - ULTIMO_EPISODIO).days


# -----------------------------
# MENSAGENS
# -----------------------------

mensagens = [
    f"Estamos há {dias} dias sem Quarto Podcast.",
    f"Dia {dias} sem Quarto Podcast. Seguimos aguardando.",
    f"{dias} dias desde o último episódio do Quarto Podcast.",
    f"Já são {dias} dias sem Quarto Podcast.",
    f"Contagem oficial: {dias} dias sem Quarto Podcast.",

    f"Dia {dias}. Nenhum sinal de Quarto Podcast.",
    f"Hoje completamos {dias} dias de silêncio.",
    f"{dias} dias sem Quarto Podcast. A espera continua.",
    f"Mais um dia. Agora são {dias} sem Quarto Podcast.",
    f"O Quarto Podcast continua desaparecido. Dia {dias}.",

    f"Dia {dias} sem podcast. Estamos começando a esquecer como era.",
    f"{dias} dias sem Quarto Podcast. Em algum lugar, um microfone acumula poeira.",
    f"Já se passaram {dias} dias. O microfone segue em repouso.",
    f"Dia {dias}. O estúdio permanece em silêncio.",
    f"{dias} dias sem ouvir um 'bem-vindos ao Quarto Podcast'.",

    f"Dia {dias} sem Quarto Podcast. A esperança é a última que morre.",
    f"{dias} dias. Seguimos fortes. Mais ou menos.",
    f"Dia {dias}. Ainda acreditamos.",
    f"{dias} dias sem episódio novo. Talvez amanhã.",
    f"Dia {dias}. Amanhã eu volto para conferir.",

    f"Estamos há {dias} dias sem Quarto Podcast e contando.",
    f"Relatório diário: {dias} dias sem Quarto Podcast.",
    f"Boletim oficial: seguimos há {dias} dias sem episódio.",
    f"Atualização importante: nada mudou. Dia {dias}.",
    f"Status do Quarto Podcast: ausente há {dias} dias.",

    f"Dia {dias}. Marcos, estamos esperando.",
    f"{dias} dias sem Quarto Podcast. Marcos, explique-se.",
    f"Marcos Verçosa, já fazem {dias} dias.",
    f"Dia {dias}. Não queremos pressionar ninguém, mas queremos sim.",
    f"{dias} dias sem Quarto Podcast. Isso aqui já virou cobrança pública.",

    f"Dia {dias}. Criamos literalmente um bot por causa disso.",
    f"{dias} dias sem podcast. Sim, alguém programou isso.",
    f"Dia {dias}. Este bot existe porque o podcast não existe mais.",
    f"{dias} dias sem Quarto Podcast. A automação venceu.",
    f"Dia {dias}. O bot segue trabalhando mais que o podcast.",

    f"{dias} dias sem Quarto Podcast. Em breve abriremos uma CPI.",
    f"Dia {dias}. O desaparecimento segue sem solução.",
    f"{dias} dias. As autoridades ainda não se pronunciaram.",
    f"Dia {dias}. Fontes próximas ao podcast não quiseram comentar.",
    f"{dias} dias sem episódio. O caso segue sob investigação.",

    f"Dia {dias}. Este é um pedido de socorro.",
    f"{dias} dias sem Quarto Podcast. Não aguentamos mais.",
    f"Dia {dias}. Cada dia que passa é um dia a mais.",
    f"{dias} dias sem episódio. Matemática cruel.",
    f"Dia {dias}. Tecnicamente, estamos mais perto do próximo episódio. Talvez.",

    f"Mais um nascer do sol. Mais um dia sem Quarto Podcast. Dia {dias}.",
    f"O mundo girou mais uma vez. Agora são {dias} dias.",
    f"Dia {dias}. O tempo passa. O episódio não chega.",
    f"{dias} dias sem Quarto Podcast. Einstein não previu isso.",
    f"Dia {dias}. A passagem do tempo permanece implacável.",

    f"{dias} dias sem Quarto Podcast. Recorde pessoal.",
    f"Dia {dias}. Novo recorde de dias sem episódio.",
    f"{dias} dias. Estamos entrando em território desconhecido.",
    f"Dia {dias}. Já passamos do razoável.",
    f"{dias} dias sem podcast. Isso já não é hiato, é estilo de vida.",

    f"Dia {dias}. Seguimos acompanhando a situação.",
    f"{dias} dias sem episódio. Voltaremos amanhã com novas informações.",
    f"Plantão Quarto Podcast: nada aconteceu. Dia {dias}.",
    f"Última hora: continuamos sem episódio. Dia {dias}.",
    f"Notícia de hoje: {dias} dias sem Quarto Podcast."
]


# Mensagens especiais

if dias == 7:
    texto = "7 dias sem Quarto Podcast. Uma semana. Tudo sob controle."

elif dias == 30:
    texto = "30 dias sem Quarto Podcast. Começamos a ficar preocupados."

elif dias == 69:
    texto = "69 dias sem Quarto Podcast. Sem comentários."

elif dias == 100:
    texto = "100 DIAS SEM QUARTO PODCAST."

elif dias == 365:
    texto = "365 dias sem Quarto Podcast. Feliz aniversário de abandono."

elif dias == 1095:
    texto = "1095 dias sem Quarto Podcast. Três anos abandonados."

elif dias == 1024:
    texto = "1024 dias sem Quarto Podcast. HoHoHo, Feliz Natal!."

elif dias == 1000:
    texto = "1000 DIAS SEM QUARTO PODCAST. Este bot venceu a guerra de atrito."

elif dias == 666:
    texto = "666 dias sem Quarto Podcast. Começamos a suspeitar de forças sobrenaturais."

elif dias % 100 == 0:
    texto = f"{dias} DIAS SEM QUARTO PODCAST. Um marco histórico."

else:
    texto = random.choice(mensagens)


# -----------------------------
# CONECTAR À API DO X
# -----------------------------

client = tweepy.Client(
    consumer_key=os.environ["X_API_KEY"],
    consumer_secret=os.environ["X_API_SECRET"],
    access_token=os.environ["X_ACCESS_TOKEN"],
    access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"]
)


# -----------------------------
# PUBLICAR
# -----------------------------

response = client.create_tweet(text=texto)

print("Publicado:")
print(texto)
print("ID:", response.data["id"])
