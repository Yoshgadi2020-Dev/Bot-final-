import discord
import string
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)




@bot.command()
async def hello(ctx):
    await ctx.send("¡Hola! Soy Bio bot tu asistente de información sobre la biodiversidad y la contaminación, o escríbeme el comando !mem para recibir una imagen divertida.")

@bot.command()
async def limpiar(ctx):
    # Nota: El bot necesita tener permisos de "Gestionar Mensajes" en tu servidor para borrar textos
    await ctx.send("¡Claro! Estoy limpiando el chat para ti...")
    await ctx.channel.purge(limit=100)
    await ctx.send("¡Listo! He eliminado los últimos 100 mensajes del chat.")

@bot.command()
async def mem(ctx):
    try:
        with open('bio mem/mem1.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("¡Ups! No encontré la imagen en la carpeta 'bio mem/mem1.png'. Revisa que el nombre coincida.")


@bot.event
async def on_message(message):
    # Evita que el bot se responda a sí mismo
    if message.author == bot.user:
        return

    # Convertimos el mensaje a minúsculas
    msg = message.content.lower()

    # Ejemplo 1: Responder a saludos (Generales o específicos)
    if "hola bio bot" in msg or "hola" in msg:
        # Si además de saludar, hablan de contaminación:
        if "contaminación" in msg or "contaminacion" in msg:
            await message.channel.send(f"¡Hola {message.author.name}! ¿Sabías que la contaminación por plástico afecta a más de 800 especies marinas? 🌊")
        
        # Si SOLO dijeron hola o saludaron al bot:
        else:
            await message.channel.send(f"¡Hola {message.author.name}! Soy Bio Bot. ¿De qué te gustaría hablar hoy? Puedes preguntarme sobre cultivar, reciclar o regar plantas. 🌱")
        
        return # Terminamos aquí para que no siga buscando en los otros 'if'
        
    # Ejemplo 2: Responder a cultivar
    if "cultivar" in msg: # Quité el signo '?' para que responda aunque no lo pongan
        datos = [
            "🌱 *¡Cultivar reduce la huella de carbono!* Al cosechar tus propios alimentos o plantar en tu comunidad, disminuyes la necesidad de transportar comida en camiones desde largas distancias, lo que reduce las emisiones de CO₂.",
            "🐝 *¡Ayuda a la biodiversidad!* Cultivar plantas y flores en casa provee refugio y alimento a polinizadores vitales como las abejas y las mariposas, combatiendo la pérdida de biodiversidad urbana.",
            "🌍 *¡Combate la erosión y la contaminación!* Las raíces de las plantas sujetan la tierra, evitando que la lluvia erosione el suelo. Además, las plantas absorben contaminantes del aire y liberan oxígeno fresco.",
            "🥗 *¡Menos plástico!* Al cultivar tus vegetales, reduces drásticamente el consumo de plásticos de un solo uso que normalmente envuelven los alimentos en el supermercado."
        ]
        await message.channel.send(random.choice(datos))
        return

    # Ejemplo 3: Responder a reciclar
    if "reciclar" in msg:
        datos_reciclaje = [
            "♻️ *¡Ahorro de energía!* Fabricar una lata de aluminio a partir de aluminio reciclado requiere un 95% menos de energía que hacer una nueva desde cero.",
            "🌊 *¡Menos plástico en los océanos!* Cada año, unos 8 millones de toneladas de plástico terminan en los mares. Al reciclar, evitas que botellas y bolsas destruyan los ecosistemas marinos.",
            "🌳 *¡Salvando bosques!* Por cada tonelada de papel que se recicla, se salvan aproximadamente 17 árboles adultos y miles de litros de agua.",
            "🗑️ *¡Menos basura acumulada!* El reciclaje evita que los vertederos se saturen y que los desechos tarden cientos de años en degradarse, liberando gases de efecto invernadero."
        ] 
        await message.channel.send(random.choice(datos_reciclaje))
        return

    # Ejemplo 4: Responder a regar
    if "regar" in msg:
        datos_riego = [
            "💧 *¡El agua es vida, no la desperdicies!* El mejor momento para regar las plantas es temprano en la mañana o al atardecer. Así evitas que el agua se evapore rápido con el sol y la aprovechan al máximo.",
            "🌱 *¡Cuidado con el exceso!* Regar de más puede ahogar las raíces de las plantas al quitarles el oxígeno del suelo. ¡Es mejor tocar la tierra primero para ver si sigue húmeda!",
            "🍃 *¡Riega la base, no las hojas!* Al regar directamente la tierra en lugar de mojar las hojas, previenes la aparición de hongos y enfermedades en tus plantas.",
            "🌧️ *¡Aprovecha la lluvia!* Recolectar agua de lluvia para regar tus plantas es una de las mejores formas de ahorrar agua potable y reducir el consumo de recursos en tu hogar."
        ]
        await message.channel.send(random.choice(datos_riego)) 
        return

    # ¡IMPORTANTE! Si el mensaje no coincide con las palabras clave de arriba,
    # esta línea procesará los comandos (!hello, !limpiar, !mem) sin trabas.
    await bot.process_commands(message)

# Pon tu Token real aquí adentro
bot.run("TU TOKEN BOT")
