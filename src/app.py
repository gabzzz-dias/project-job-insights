from flask import Flask
from . import routes_and_views


def create_app() -> Flask:
    app = Flask(__name__)
    routes_and_views.init_app(app)

    return app

# Agradecimentos ao Gabriel Miranda, da turma 10-B
# que me ajudou a entender algumas questões do projeto em que tive dúvidas.
# PR do Gabriel: github.com/tryber/sd-010-b-project-job-insights/pull/50
