import discord
import random
import os
import requests 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado con {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}, diseñado para intentar prevenir la contaminacion!')

@bot.command()
async def m_prog(ctx):
    lt_images = os.listdir("images/programadores")
    img_name = random.choice(lt_images)
    with open(f'images/programadores/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def m_anima(ctx):
    lt_images = os.listdir("images/animales")
    img_name = random.choice(lt_images)
    with open(f'images/animales/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def m_nigg(ctx):
    lt_images = os.listdir("images/hmnegro")
    img_name = random.choice(lt_images)
    with open(f'images/hmnegro/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

consejos = [ "Recuerda siempre utilizar bolsas reutilizables",
            "Recuerda botar la basura de forma organizada",
            "Recuerda no dejar basura tirada en la calle",
            "Recuerda elegir papel antes que el plastico",
            "Recuerda no botar cosas porque si" ]
@bot.command()
async def consejodia(ctx):
    conse = random.choice(consejos)
    await ctx.send(conse)

manuali = ["Puedes utilizar botellas de plastico para hacer materas y poder adornar las partes verdes de tu casa",
           "Puedes reutilizar tus calcetines viejos para hacer unas divertidas marionetas",
           "Puedes hacer abono utilizando una botella y metiendo todos los desechos de las comidas",
           "Puedes hacer un bolso a la moda utilizando cualquier pantalon viejo que no te sirva"]
@bot.command()
async def manualidades(ctx):
    manuali_s = random.choice(manuali)
    await ctx.send(manuali_s)

@bot.command()
async def especiespeligro(ctx):
    await ctx.send("Los animales que estan en peligro de extincion actualmente son pandas, tigres, elefantes, gorilas, osos polares, ballenas, rinocerontes, chimpancés, leopardos y delfines de agua dulce.")

@bot.command()
async def jpg_animalespeligro(ctx):
    lt_images = os.listdir("images/enpeligro")
    img_name = random.choice(lt_images)
    with open(f'images/enpeligro/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("Token")
