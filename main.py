#developed by sans
#CHANGE LINES 8, 14 AND 37 OR LINE 10 IF YOU WANT.
import discord
from discord.ext import commands, tasks
from discord import Intents

bot = commands.Bot("!", intents=Intents.all())
role_id = Type_the_ID_of_the_role_to_be_assigned.

@tasks.loop(seconds=5)
async def check_activity():
    role = bot.guilds[0].get_role(role_id)
    file = open('role_members.txt', 'r')
    member_list = [str(member.id) for member in bot.get_all_members() if 'Write here what you want them to write in their status.' in str(member.activity)]
    member_ids = [line[:-1] for line in file.readlines()]
    file.close()
    for member_id in member_ids:
        if member_id not in member_list:
            member = bot.guilds[0].get_member(int(member_id))
            await member.remove_roles(role)
            member_ids.remove(member_id)
    with open('role_members.txt', 'w') as file:
        for member_id in member_ids:
            file.write(member_id + '\n')
    for member_id in member_list:
        if member_id not in member_ids:
            member = bot.guilds[0].get_member(int(member_id))
            await member.add_roles(role)
            with open('role_members.txt', 'a') as file:
                file.write(member_id + '\n')

            
@bot.event
async def on_ready():
    check_activity.start()

bot.run('YOUR_BOT_TOKEN')