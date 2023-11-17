from src.core.log import log
from src.core.registar import register_app


try:
    app = register_app()

    log.info(
                """
                  █████▒ ▒█████   ██▀███   ███▄ ▄███▓  ██████ 
                ▓██   ▒ ▒██▒  ██▒▓██ ▒ ██▒▓██▒▀█▀ ██▒▒██    ▒ 
                ▒████ ░ ▒██░  ██▒▓██ ░▄█ ▒▓██    ▓██░░ ▓██▄   
                ░▓█▒  ░ ▒██   ██░▒██▀▀█▄  ▒██    ▒██   ▒   ██▒
                ░▒█░    ░ ████▓▒░░██▓ ▒██▒▒██▒   ░██▒▒██████▒▒
                 ▒ ░    ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░
                 ░        ░ ▒ ▒░   ░▒ ░ ▒░░  ░      ░░ ░▒  ░ ░
                 ░ ░    ░ ░ ░ ▒    ░░   ░ ░      ░   ░  ░  ░  
                            ░ ░     ░            ░         ░  
                """
            )

except Exception as e:
    log.error(f'❌ FastAPI start filed: {e}')
    raise Exception
