import discord
from discord.ext import commands
import asyncio
import random
import os
from dotenv import load_dotenv

load_dotenv()  

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event 
async def on_ready():
    print(f"TheWolrdInviteBot connecte en tant que {bot.user}")

@bot.command(name="invite")
async def create_invite(ctx, *, cible=None):
    if not ctx.guild.me.guild_permissions.create_instant_invite:
        await ctx.send("Pas les permissions")
        return

    try:
        invite = await ctx.channel.create_invite(max_age=86400, max_uses=10, reason="Invitation par TheWorldInviteBot")
    except discord.Forbidden:
        await ctx.send("Permissions manquantes")
        return
    except discord.HTTPException:
        await ctx.send("Erreur de creation")
        return
    
    if cible is None:
        destinataire = ctx.author
        try:
            await destinataire.send(f"Rejoins **{ctx.guild.name}** (salon {ctx.channel.mention}) : {invite.url}")
            await ctx.send(f"Lien d'invitation envoye a {destinataire.mention}!")
        except discord.Forbidden:
            await ctx.send("Le fou il a bloque ses MP")
        except Exception as e:
            await ctx.send(f"Erreur:{e}")
        return

    if cible in ["@everyone", "everyone"]:
        await ctx.send("Tu vas envoyer un message prive a tous les membres du serveur. Confirme avec oui dans les 30 secondes.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() == "oui"

        try:
            await bot.wait_for("message", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Commande annulee.")
            return

        membres = [m for m in ctx.guild.members if not m.bot]
        await ctx.send(f"Envoi a {len(membres)} membres...")

        success = 0
        echec = 0
        for membre in membres:
            try:
                await membre.send(f"Rejoins **{ctx.guild.name}** (salon {ctx.channel.mention}) : {invite.url}")
                success += 1
                await asyncio.sleep(0.5)
            except discord.Forbidden:
                echec += 1
            except Exception:
                echec += 1
        await ctx.send(f"Termine : {success} envoyes, {echec} echoues.")
        return

    try:
        member_converter = commands.MemberConverter()
        destinataire = await member_converter.convert(ctx, cible)
    except commands.BadArgument:
        await ctx.send("Membre invalide. Utilise !invite @membre ou !invite everyone")
        return

    try:
        await destinataire.send(f"Rejoins **{ctx.guild.name}** (salon {ctx.channel.mention}) : {invite.url}")
        await ctx.send(f"Lien envoye a {destinataire.mention}!")
    except discord.Forbidden:
        await ctx.send("Le fou il a bloque ses MP")
    except Exception as e:
        await ctx.send(f"Erreur:{e}")

@bot.command(name="winvite")
async def send_winvite(ctx, *, cible=None):
    FIXED_LINK = "https://discord.gg/vaZmw57N"
    
    if cible is None:
        destinataire = ctx.author
        try:
            await destinataire.send(f"Rejoins **{ctx.guild.name}** avec ce lien : {FIXED_LINK}")
            await ctx.send(f"Lien winvite envoye a {destinataire.mention}!")
        except discord.Forbidden:
            await ctx.send("Le fou il a bloque ses MP")
        except Exception as e:
            await ctx.send(f"Erreur:{e}")
        return

    if cible in ["@everyone", "everyone"]:
        await ctx.send("Tu vas envoyer un message prive a tous les membres du serveur. Confirme avec oui dans les 30 secondes.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() == "oui"

        try:
            await bot.wait_for("message", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Commande annulee.")
            return

        membres = [m for m in ctx.guild.members if not m.bot]
        await ctx.send(f"Envoi a {len(membres)} membres...")

        success = 0
        echec = 0
        for membre in membres:
            try:
                await membre.send(f"Rejoins **{ctx.guild.name}** avec ce lien : {FIXED_LINK}")
                success += 1
                await asyncio.sleep(0.5)
            except discord.Forbidden:
                echec += 1
            except Exception:
                echec += 1
        await ctx.send(f"Termine : {success} envoyes, {echec} echoues.")
        return

    try:
        member_converter = commands.MemberConverter()
        destinataire = await member_converter.convert(ctx, cible)
    except commands.BadArgument:
        await ctx.send("Membre invalide. Utilise !winvite @membre ou !winvite everyone")
        return

    try:
        await destinataire.send(f"Rejoins **{ctx.guild.name}** avec ce lien : {FIXED_LINK}")
        await ctx.send(f"Lien winvite envoye a {destinataire.mention}!")
    except discord.Forbidden:
        await ctx.send("Le fou il a bloque ses MP")
    except Exception as e:
        await ctx.send(f"Erreur:{e}")

@bot.command(name="ninvite")
async def send_ninvite(ctx, *, cible=None):
    FIXED_LINK = "https://discord.gg/QnewqHfK"
    
    if cible is None:
        destinataire = ctx.author
        try:
            await destinataire.send(f"Rejoins **{ctx.guild.name}** avec ce lien : {FIXED_LINK}")
            await ctx.send(f"Lien ninvite envoye a {destinataire.mention}!")
        except discord.Forbidden:
            await ctx.send("Le fou il a bloque ses MP")
        except Exception as e:
            await ctx.send(f"Erreur:{e}")
        return

    if cible in ["@everyone", "everyone"]:
        await ctx.send("Tu vas envoyer un message prive a tous les membres du serveur. Confirme avec oui dans les 30 secondes.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() == "oui"

        try:
            await bot.wait_for("message", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Commande annulee.")
            return

        membres = [m for m in ctx.guild.members if not m.bot]
        await ctx.send(f"Envoi a {len(membres)} membres...")

        success = 0
        echec = 0
        for membre in membres:
            try:
                await membre.send(f"Rejoins **{ctx.guild.name}** avec ce lien : {FIXED_LINK}")
                success += 1
                await asyncio.sleep(0.5)
            except discord.Forbidden:
                echec += 1
            except Exception:
                echec += 1
        await ctx.send(f"Termine : {success} envoyes, {echec} echoues.")
        return

    try:
        member_converter = commands.MemberConverter()
        destinataire = await member_converter.convert(ctx, cible)
    except commands.BadArgument:
        await ctx.send("Membre invalide. Utilise !ninvite @membre ou !ninvite everyone")
        return

    try:
        await destinataire.send(f"Rejoins **{ctx.guild.name}** avec ce lien : {FIXED_LINK}")
        await ctx.send(f"Lien ninvite envoye a {destinataire.mention}!")
    except discord.Forbidden:
        await ctx.send("Le fou il a bloque ses MP")
    except Exception as e:
        await ctx.send(f"Erreur:{e}")

# Commandes amusantes
@bot.command(name="8ball")
async def eight_ball(ctx, *, question):
    responses = [
        "C'est certain.",
        "Sans aucun doute.",
        "Oui, absolument.",
        "Tu peux compter dessus.",
        "Probablement.",
        "Mieux vaut ne pas te le dire maintenant.",
        "Je ne peux pas prédire maintenant.",
        "Concentre-toi et demande à nouveau.",
        "N'y compte pas.",
        "Très douteux.",
        "Non.",
        "Jamais."
    ]
    reponse = random.choice(responses)
    await ctx.send(f"🎱 Question : {question}\nRéponse : {reponse}")



@bot.command(name="quote")
async def quote(ctx):
    citations = [
        "« La vie est un combat, faut pas baisser les bras. » – Booba",
        "« J'écris ma vie sur un bout de papier, pour que mes enfants sachent d'où ils viennent. » – Rohff",
        "« Le succès n'est pas définitif, l'échec n'est pas fatal : c'est le courage de continuer qui compte. » – (inspiré de Winston Churchill, mais souvent cité dans le rap)",
        "« Dans la rue, on apprend plus qu'à l'école. » – 113",
        "« Faut savoir saisir les opportunités quand elles se présentent. » – NTM",
        "« J'ai pas de compte en banque, mais j'ai des principes. » – IAM",
        "« Le respect ne s'achète pas, il se gagne. » – Kery James",
        "« On rêve tous de réussir, mais peu sont prêts à sacrifier. » – Lacrim",
        "« La haine mène à rien, l'amour mène à tout. » – Soprano",
        "« Parfois, il faut perdre pour comprendre ce qui compte vraiment. » – Damso",
        "« J'écris pour ceux qui n'ont pas de voix. » – Sinik",
        "« La vie est une roue, un jour t'es en bas, un jour t'es en haut. » – La Fouine",
        "« Le temps est précieux, ne le gaspille pas. » – Shay",
        "« Faut rester focus sur ses objectifs. » – Gradur",
        "« L'argent ne fait pas le bonheur, mais ça aide. » – PNL",
    ]
    await ctx.send(random.choice(citations))

@bot.event
async def on_member_join(member):
    if member.bot:
        return
    
    guild = member.guild

    invite_channel = guild.system_channel
    if invite_channel is None:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).create_instant_invite:
                invite_channel = channel
                break
    if invite_channel is None:
        print(f"Pas de salon sur {guild.name}")
        return

    try:
        invite = await invite_channel.create_invite(max_age=0, max_uses=0, reason=f"Invitation pour {guild.name}")
    except discord.Forbidden:
        print(f"Pas assez de permissions dans #{invite_channel.name} sur {guild.name}")
        return
    except discord.HTTPException as e:
        print(f"Erreur de creation:{e}")
        return
    
    try:
        await member.send(f"C'est partie pour l'aventure sur **{guild.name}**!!!! \n" f"Partage ca vite fais {invite.url}")
        print(f"Lien envoye a {member} (ID:{member.id})")
    except discord.Forbidden:
        print(f"orhhhhhhhh {member} le fou a bloque ses MP")
    except Exception as e:
        print(f"Erreur d'envoi a {member}:{e}")

bot.run(TOKEN) 