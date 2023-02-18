import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28572325")

API_HASH = os.environ.get("API_HASH", "7ae1805ea0fd1d86b9c2a274e056e94c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6015682431:AAGOvArVxPqUJonBVMkj-p4t8hQ71GCGvLA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001767987588") 

DB_NAME = os.environ.get("DB_NAME","rnmflbot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://asubang:asubang@cluster0.dnjfe.mongodb.net/test")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1823080600').split()]

