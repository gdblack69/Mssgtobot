# gunicorn.conf.py

bind = "0.0.0.0:8000"  # The IP address and port to bind the app to
workers = 3  # Number of worker processes to handle requests
worker_class = "sync"  # You can use "gevent", "eventlet", etc., depending on your needs
timeout = 30  # Timeout for worker requests in seconds
accesslog = "-"  # Set to "-" to log to stdout (or specify a log file)
errorlog = "-"  # Set to "-" to log to stderr (or specify a log file)
loglevel = "info"  # Set the log level to "debug", "info", "warning", etc.
