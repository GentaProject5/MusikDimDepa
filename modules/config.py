import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("25989336"))
API_HASH = getenv("af53cce8dc3b6fb2e4ae0c17e9d646df")
BOT_USERNAME = getenv("v1Bnubot")
BOT_TOKEN = getenv("6091391494:AAHOIxGlD6tNFB3TGgKGGUlVDkjvuPNuuOo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("BQDDV4QAZcN35eLhfXbWWF-NJ5yJAgaetIlK5FMksPK1GF076VuGQ6_tY-fRbqk__Me0f0tCHrk5CtFLM8QnjUSzSVNZhlja9sQGfHW2975PYQzyocgfPD4zeIL8p2Nvcx7QNTyf3W9wVuRpUJpxUwP76WCtnsGbUmoB6L59EvZhyrZpiA9KewIQ6TCkK3QW56g89lIAn8pEMynW4sVdi_CBQ-Zn-cOTuawBSCWhmS2ASPbN6D9ZQGy2kaK_ixIMRu85lzVXTFivwitRCWyUnbz4DiI0kL3XEXvrVwLu1_y5qOKj4w743_LTTbUEY8run1hq_wcQ_o28CoDDf4puj50tGNQxiAAAAAByxTHIAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1925525960").split()))
aiohttpsession = aiohttp.ClientSession()
