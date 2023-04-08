import discord 
import random 

# Переменная monetka - хранит так сказать монетку которые бот будет подкидывать и решать когда будет запускатся бот!
monetka = [1, 2]
choise = random.choice(monetka)

if choise == 1 :
    # Переменная intents - хранит привилегии бота
    intents = discord.Intents.default()
    # Включаем привелегию на чтение сообщений
    intents.message_content = True
    # Создаем бота в переменной client и передаем все привелегии
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
           return
        if message.content.startswith('$hello'):
            await message.channel.send("Hi!")
        elif message.content.startswith('$bye'):
            await message.channel.send("\\U0001f642")
        else:
            await message.channel.send(message.content)
    botyara = "СЮДА ТОКЕН ВАШЕГО БОТА/ УДАЛЯЕМ ДАННУЮ ПЕРЕМЕННУЮ И В КАВЫЧКАХ ВСТАВЛЯЕМ НАШ ТОКЕН В client.RUN"
    client.run(botyara)

else :
    print("Попробуй еще раз :).Монетка пала на число 2, а если число не 1 тоесть 2 то бот не запустится.")
