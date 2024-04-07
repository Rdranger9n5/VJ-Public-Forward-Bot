from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "13152445")
    API_HASH = environ.get("API_HASH", "16417e529e92f501052ad676e1ab9c64")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7194104376:AAFKFzRDp7UVPUdigGzPCbwFdr2bv4TLvr4")
    STRING_SESSION = environ.get("STRING_SESSION", "AQAu6W8AktpkLeMfb9FyHSTvislHGcvtkKizDV6DabSJNunn06dWJH4fehXI4WmVaCwAmhwlWWswatc_p0_NJIFV71awwJ-Fn8NfgArQChJ2sWogn1QEzS5JTup3heERBUbSNGxnkKpoAalGBdm_FPQaY3MU8nVVHA-xUS6rBa9Wv1X7sxyaG3AnWQHokkNuw22zG_95Ixc9ouXQ7iREngCkYmBXDZ1mL3Y60deyqzTmR03ZwRWFsworCaX4TxfxwyVVG9dd2Jum2IEyePbE291TUhEjDHnF8BI3LEXzMQ1LfCP4SbPtfIihhOpWGSMf-Z66kUw1VkDITZxvf2N1BpDA8ec6SQAAAABXourJAA")
    SUDO_USERS = environ.get("SUDO_USERS", "5139420709")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
