from flask import Flask
from config import Config
from models.student import init_db
from routes.student_routes import student_bp

# Create Flask application instance
app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Initialize the MySQL database with the Flask app
init_db(app)

# Register the blueprint for student routes
app.register_blueprint(student_bp)

# Define a basic route for testing
@app.route('/')
def home():
    return "Welcome to the Student Management System!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
