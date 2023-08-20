import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "22446339"))
    API_HASH = os.environ.get("API_HASH", "1349a75bb3c28d975ba425fb74b9d355"
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6538245113:AAGxvTOhB7KkF7KXh0O9i3_bjok1nRji4Rg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBuyjJNJzvB0UPXx9dFJoO9nboStjLt4pVyFzr-9zs0qeM0MyOutQTbTj9Cu9e5adoHTISkvIz4n0NGAGHX3RCJATILyOCkPzySD8dtHVSPkRSinyuK7y3X4OH4zGzF1BllYRJMhUbPK7rl_19yFmJE3DMT7gbQCPVq8LqQDoMtweUd01CiCcEP-RKd3PX3K8KMIWjjT1Av-G-Sn2xkwsU03-PXyqEd_eApccxDI6YVRf5p738IvXxA7DML80B9_b6Bmf42VNqoUSDzfeMoc1aLCJBcSxtLnUFLI98bqds7fV_CxoXtJOmmnOllEmB9tXv5OGqRwMz-fpLqLt95Mm9QYE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
