from gui import start_app
import logging
logger=logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    filename="data.log",
    format='%(asctime)s - %(levelname)s - %(message)s'
) 

if __name__ == "__main__":
    logging.info("Start aplikace")
    start_app()
    logging.info("Konec aplikace") # Musím dodělat tlačítko pro ukončení aplikace, aby se tohle do logů zapsalo
