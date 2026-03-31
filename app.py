from app import AppFactory
from app.singleton import AppSingleton
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

# Create single app instance using Singleton + Factory
app = AppSingleton.get_instance(AppFactory.create_app)

# Prometheus metric
PAGE_VIEWS = Counter('page_views_total', 'Total Page Views')

# Middleware to count requests
@app.before_request
def count_requests():
    PAGE_VIEWS.inc()

# Metrics endpoint for Prometheus
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)