from discord.ext import commands
import discord
import random

TOKEN = "MY BOT TOKEN"
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="&", intents=intents)

member_list_of_100up = ["Kuroko", "狼玥", "殘夢", "彤芸", "流星雨", "漓", 
                      "烤紅薯", "托菲", "黑糖布丁", "抹茶湯圓", "閃電", 
                      "CiCi", "AZ", "Ann", "鳥子", "寒久", "娜娜", "曉亮", 
                      "Wolf", "雪兒", "祈言", "四葉草", "lib", "AwA"]

member_list_of_50to100 = ["肴紀", "哭馬", "貓咪君", "aiR", "kzn", "M A O",
                        "CoRN", "凜", "LK", "七年", "紫影", "Emi", "OuO",
                        "餅餅", "皮塔", "沙特", "卡B", "染沫", "YuYu瑜",
                        "燁凌", "洛", "森カリオペ", "LarK", "柳橙", "bok", 
                        "lunar", "冰糖", "紫鞋", "ㄐㄐ", "哈嚕", "茶喵", 
                        "酸奶", "小溪"]

member_list_of_below50 = ["komi","炒麵麵包","亭亭","安喬","妤","海橙","櫻桃",
                        "棉花糖","piao","保麗龍","罐罐喵","火鍋芋頭","茶葉",
                        "鯰魚","Fukuma","草莓","蓮子","re","青蛙","烏鴉","奈",
                        "NN","幽吉","滄嵐","^_^","A君","一粟","初","惞","龍雲",
                        "oreo","SZz","yubi","葡萄柚","殤","牧","浣熊","公雞",
                        "揪汰","28>30","考拉","柳橙原汁","雪沫","橘","佳奈",
                        "蛋糕","離夢","玟","鳩月","麵條","燕語","鯛魚燒","奏大好",
                        "海夢","晨綻","Tk","程","5v","茶會","YN","白","辞","夜裘",
                        "泡芙","Iwill","長冶","獨子","NoNo","亞瑟","yumi","Snowy",
                        "大和撫子","玖","C","Takina","月、","幸運星","阿櫻","夜梓",
                        "天音之溢","西呱","海鹽奶酪","bok","YHN","水水","白淺","幽靈",
                        "是右心","AA","五二","歪歪","絲亞","愛莉醬","ゆき","楓"]

@client.command()
async def nna周年抽獎1(ctx):
    await ctx.send(random.choice(member_list_of_100up))

@client.command()
async def nna周年抽獎2(ctx):
    await ctx.send(random.choice(member_list_of_50to100))

@client.command()
async def nna周年抽獎3(ctx):
    await ctx.send(random.choice(member_list_of_below50))

client.run(TOKEN)
