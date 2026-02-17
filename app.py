from app import create_app
from app.singleton import AppSingleton

# Create single app instance using Singleton + Factory
app = AppSingleton.get_instance(create_app)

if __name__ == "__main__":
    app.run(debug=True)
    