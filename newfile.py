from twitchio.ext import commands
import google.generativeai as genai

# Configuração da API e modelo Gemini
genai.configure(api_key="AIzaSyCIOfbNjiak6d7UqO0uZ2c1p9Zd93jgRIo")
model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat_gemini = model.start_chat(history=[])

# Classe do bot
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='4wf7psvn2ybepybbksw5vs6zv7cldh', prefix='!', initial_channels=['friendfyre'])

    @commands.command(name='gemini')
    async def gemini_command(self, ctx, *, mensagem):
        response = chat_gemini.send_message(mensagem)
        await ctx.send(f"Gemini: {response.text}")

bot = Bot()
bot.run()
