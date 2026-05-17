from flask import Blueprint, jsonify
from app.core.engine import PUAPIEngine
from config import Config

# Create a Blueprint for our API routes
api_bp = Blueprint('api', __name__)

# Initialize our core engine with the config we created
engine = PUAPIEngine(config=Config)

@api_bp.route('/api/data', methods=['GET'])
def get_universal_data():
    """
    The single RESTful endpoint for the PU-API.
    When a user visits this URL, the engine fetches and aggregates EVERYTHING.
    """
    response = engine.get_all_data()
    
    # Return the aggregated dictionary as clean JSON
    return jsonify(response)