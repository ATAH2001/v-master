from os import getenv
from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

TOKEN = environ.get("TOKEN")
API_ID = int(environ.get("API_ID","25611385"))
API_HASH = environ.get("API_HASH","554bd8ef864e807884fe9ba48536e6b2")
API_ID1 = int(environ.get("API_ID1","25611385"))
API_HASH1 = environ.get("API_HASH1","554bd8ef864e807884fe9ba48536e6b2")
sudoers = [int(x) for x in environ.get("sudoers", "").split()]
LOG_GROUP_ID = environ.get("LOG_GROUP_ID","-1001622606659")
BASE_DB = environ.get("BASE_DB","mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
MONGO_URL = environ.get("MONGO_URL","mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
ARQ_API_URL = environ.get("ARQ_API_URL","https://arq.hamker.in")
ARQ_API_KEY = environ.get("ARQ_API_KEY","VXIWBI-DIQJVN-YSWZLO-TNYZIS-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ح ف ب غ س ك و م ا ت / ! . ذ ق ف ش").split())
F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")
BOT_PREFIX = environ.get("BOT_PREFIX",".")