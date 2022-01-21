import logging

FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format=FORMAT)

logging.debug("La fonction est bien execute")
logging.info("Message d'information")
logging.warning("Attention")
logging.error("Une erreur est arrive")
logging.critical("Erreur critique")
