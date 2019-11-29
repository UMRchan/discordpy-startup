from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client.on('ready', message =>
{
  client.user.setPresence({ game: { name: 'ピザ食べてます' } });  
  console.log('bot is ready!');
});

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
client.on('message', message =>
{
  if(message.isMemberMentioned(client.user))
  {
    message.reply( 'ピザ食べてるけど何か用？' );
    return;
  }
});
    


bot.run(token)
