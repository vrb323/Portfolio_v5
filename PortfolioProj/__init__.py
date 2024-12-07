load_dotenv()
app = Flask('__main__', static_folder='jobs/static', template_folder='jobs/templates')

from jobs import views
