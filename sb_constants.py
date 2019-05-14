import sys

embed_color = 0x562906
base_url = 'https://res.cloudinary.com/du9xmm6rh/image/upload/'
# "v1" assumes that the image was uploaded before Tuesday, May 17, 2033 11:33:20 PM GMT-04:00 DST
base_icon_url = base_url + 'v1/smash_icons/'


DB_ERROR_MSG = "Something went wrong with the database. Please try again, {}."

# return codes
RC_SUCCESS = 0
RC_CHANNEL_ONLY = 1
RC_COMMAND_DNE = 2
RC_OTHER = -1 

TEST_MODE = len(sys.argv) > 1 and (sys.argv[1] == "-t" or sys.argv[1] == "--test")

SECRET_CONFIG_FILE = ('./super_secret_config.test' if TEST_MODE else '/bin/smashbot/super_secret_config.prod') + '.json'

SNARKY_IPLAY_RESPONSES = [
    




]