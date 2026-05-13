from flask import Flask, render_template
from dotenv import load_dotenv
import os
from config import Config

# ========== Carregar variáveis de ambiente ==================
load_dotenv()

# =========== Função de criação do app =============
def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates"
    )

    # ======= Carregar configurações =======
    app.config.from_object(Config)


    # ======== Registrar blueprints ==========
    from web.views.routers import main_blueprint
    app.register_blueprint(main_blueprint)

    # ======== Tratamento de erros ==========
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("erros/404.html"), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template("erros/500.html"), 500

    return app

