## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME   =   getenv ( "SESSION_NAME"  ،  "AgA9huBtxv4mijmlBEivyOB1K9GK3BrYZ5FQahMfnYV5Denp_LkHrbqgYl1yLy_MZSWkIXIv68LWHMFgNMVWzrcI-Qgif0tHQoYabi3aCbsDxnyzMR5pP2qvcNDcQGUNLEm4dcmwKvrtvinz-vbHcWqZB4Q7xrzQEVn75s5M3onHGuN4r5we5U_7KCG8AmFijY9sXIpNnb5cZMLytJiIa7DP-ssfgoHxWo0NbQJLC0twnHOlBgrcPitlrPLObsHZKwcTDA-qsoSoMv2DVRC56z8nvDLdnuCqme22vsOyQmn6kSTEXguJAuTwSKeY-YFEQDlnE3LSI2d8XvKWnD4fuqyEAAAAATkj3t8A" )
BOT_TOKEN  =  getenv ( "BOT_TOKEN" ، "5497740291:AAFgiT5ePHpYbE-s9HzT7J3eJCPWdEtkedQ" )
BOT_NAME  =  getenv ( "BOT_NAME" ، "ُMُْUُSٍُIُC_ُAُLُMُْEُْM" )
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME  =  getenv ( "OWNER_NAME" ، "mem" )
OWNER_USERNAME  =  getenv ( "OWNER_USERNAME" ، "@N_J_9" )
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME  =  getenv ( "BOT_USERNAME" ، "@UU_TLBot" )
OWNER_ID  =  getenv ( "OWNER_ID" ، "2077885450" )
ASSISTANT_NAME  =  getenv ( "ASSISTANT_NAME" ، "U_U_9U" )
GROUP_SUPPORT  =  getenv ( "GROUP_SUPPORT" ، "X_8_00" )
UPDATES_CHANNEL  =  getenv ( "UPDATES_CHANNEL" ، "X_8_00" )
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS  =  قائمة ( خريطة ( int ، getenv ( "SUDO_USERS" ، "2077885450" ). split ()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
