"""Учебное HTTP-приложение."""
from flask import Flask, jsonify


def create_app():
    """Создаёт экземпляр приложения."""
    application = Flask(__name__)

    @application.get("/health")
    def health():
        """Возвращает статус приложения."""
        return jsonify(status="unhealthy")

    @application.get("/")
    def index():
        """Возвращает сведения о службе."""
        return jsonify(service="devops-ci-app", version="1.0.0", status="running")

    return application


app = create_app()
