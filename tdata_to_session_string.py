from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession, CreateNewSession
from telethon.sessions import StringSession

import asyncio


async def main():
    api = API.TelegramDesktop.Generate()
    # Load TDesktop client from tdata folder
    tdataFolder = "$PATH"
    tdesk = TDesktop(tdataFolder)

    # Check if we have loaded any accounts
    assert tdesk.isLoaded()

    # flag=UseCurrentSession
    #
    # Convert TDesktop to Telethon using the current session.
    client = await tdesk.ToTelethon(session="telethon.session", flag=CreateNewSession)
    # Connect and print all logged-in sessions of this client.
    # Telethon will save the session to telethon.session on creation.
    print(api)
    await client.connect()
    await client.PrintSessions()
    print(StringSession.save(client.session))


asyncio.run(main())
