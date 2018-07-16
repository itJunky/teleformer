import sys
from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from config import api_id, api_hash


client = TelegramClient('session_name', api_id, api_hash)
client.start()

def list_dialogs():
  dialogs = client.get_dialogs()
  for d in dialogs:
    print(' ')
    if d.is_user: print('U - %d \t %s \t %s \t %s -\t %s'%(d.id, d.name, d.entity.phone, d.entity.mutual_contact, d.message.message))
    if d.is_channel: print('C %d \t %s'%(d.id, d.name))
    elif d.is_group: print('G %d \t %s'%(d.id, d.name))

list_dialogs()
