from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from test.save_data_to_es import send_to_elasticsearch

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=['http://localhost:8111'])


app.add_url_rule('/api/elastic', 'send_to_elasticsearch', send_to_elasticsearch, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True)