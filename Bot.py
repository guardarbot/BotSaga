import discord

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='NHO'))
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')


@client.event
async def on_message(message):
    if message.content.startswith('?test'):
        await client.send_message(message.channel, "Olá Mundo, estou vivo!")

    if message.content.startswith('!fale'):
        def check(msg):
            return msg.content.startswith('!fale')
        message = await client.wait_for_message(author=message.author, check=check)
        falar = message.content[len('!fale'):].strip()
        await client.send_message(message.channel, falar)

    if message.content.startswith('!Aliança'):
        user = message.author
        role = discord.utils.get(user.server.roles, name="Aliança")
        d1 = discord.utils.get(user.server.roles, name="Aliança")
        d2 = discord.utils.get(user.server.roles, name="Akatsuki")
        d3 = discord.utils.get(user.server.roles, name="Sunagakure")
        d4 = discord.utils.get(user.server.roles, name="Konohagakure")
        await client.remove_roles(user,d1)
        await client.remove_roles(user,d2)
        await client.remove_roles(user,d3)
        await client.remove_roles(user,d4)
        await client.add_roles(user, role)
        await client.send_message(message.channel, "Você foi alterado para Aliança!")
        await client.delete_message(message)



client.run('NDg3Mzk4MzYwOTk1NzI1MzIz.DnNErQ.elqyatb18kgzcLwm22iATuzSOzk')
