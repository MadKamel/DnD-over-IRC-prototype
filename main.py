import irc

channel = "#madkameldnd"
server = "irc.freenode.net"
nickname = "testuser"

client = irc.IRC()
client.connect(server, channel, nickname, "DnD Over IRC Test User")