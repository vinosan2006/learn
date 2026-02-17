class AppSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, app_creator):
        if cls._instance is None:
            cls._instance = app_creator()
        return cls._instance
