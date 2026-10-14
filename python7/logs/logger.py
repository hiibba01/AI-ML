#configuring logging
import logging

logging.basicConfig(
    filename='app.log',  #app.log file will be created and content will be written in it
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True

)
