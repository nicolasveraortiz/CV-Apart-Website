import os
import smtplib
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap4

# Future Improvements

# from flask import abort, redirect, flash
# from datetime import date
# from flask_ckeditor import CKEditor
# from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import Integer, String, Text, ForeignKey
# from functools import wraps
# from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
bootstrap = Bootstrap4(app)

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        msg_sent = True
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        form = f"Subject: {subject}!\n\n{name}\n{email}\n{message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="clivionicolasveraortiz1@gmail.com"
                                , msg=form.encode("utf-8"))
        return render_template("contact.html", request=request, msg_sent=msg_sent)


@app.route("/services")
def services():
    return render_template("service.html")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")


@app.route("/facilities")
def facilities():
    return render_template("facilities.html")


@app.route("/room/<int:id>")
def show_info(id):
    departments = {
        1: {
            "title": "Departamento 1",
            "description": [
                "Departamento cómodo completamente amueblado",
                "Todos los electrodomésticos.",
                "Cocina-comedor y todas las herramientas de cocina (platos, vasos, utensilios, etc.)",
                "Con aire acondicionado frío/calor.",
                "Con Smart TV", "Conexión a Internet gratuita", "2 Habitaciones.",
                "Para 6 personas.",
                "Apto para menores.",
                "Baño completamente equipado."],
            "symbols": [
                "fa-solid fa-couch",
                "fa-solid fa-plug",
                "fa-solid fa-kitchen-set ",
                "fa-solid fa-snowflake",
                "fa-solid fa-tv",
                "fa-solid fa-wifi",
                "fa-solid fa-bed",
                "fa-solid fa-user",
                "fa-solid fa-children",
                "fa-solid fa-sink"
            ],
            "images": [
                "assets/img/cv-apart-photos/cvapart.jpg",
                "assets/img/cv-apart-photos/dpto1-beds.jpg",
                "assets/img/cv-apart-photos/dpto1-beds2.jpg",
                "assets/img/cv-apart-photos/dpto1-smbeds.jpg",
                "assets/img/cv-apart-photos/dpto1-tv.jpg",
                "assets/img/cv-apart-photos/dpto1-window-ls.jpg",
                "assets/img/cv-apart-photos/dpto1-corridor.jpg",
                "assets/img/cv-apart-photos/dpto1-bath.jpg",
                "assets/img/cv-apart-photos/dpto1-bath2.jpg"
            ]
        },
        2: {
            "title": "Departamento 2",
            "description": [
                "Departamento cómodo completamente amueblado",
                "Todos los electrodomésticos.",
                "Cocina-comedor y todas las herramientas de cocina (platos, vasos, utensilios, etc.)",
                "Con aire acondicionado frío/calor.",
                "Con Smart TV", "Conexión a Internet gratuita", "2 Habitaciones.",
                "Para 5 personas.",
                "Apto para menores.",
                "Baño completamente equipado."],
            "symbols": [
                "fa-solid fa-couch",
                "fa-solid fa-plug",
                "fa-solid fa-kitchen-set ",
                "fa-solid fa-snowflake",
                "fa-solid fa-tv",
                "fa-solid fa-wifi",
                "fa-solid fa-bed",
                "fa-solid fa-user",
                "fa-solid fa-children",
                "fa-solid fa-sink"
            ],
            "images": [
                "assets/img/cv-apart-photos/dpto2-beds.jpg",
                "assets/img/cv-apart-photos/dpto2-tv.jpg",
                "assets/img/cv-apart-photos/dpto2-smbeds.JPG",
                "assets/img/cv-apart-photos/dpto2-smbeds2.jpg",
                "assets/img/cv-apart-photos/dpto2-smbeds3.jpg",
                "assets/img/cv-apart-photos/dpto2-kitchen.jpg",
                "assets/img/cv-apart-photos/dpto2-room.jpg"
            ]
        },
        3: {
            "title": "Departamento 3",
            "description": [
                "Departamento cómodo completamente amueblado",
                "Todos los electrodomésticos.",
                "Cocina-comedor y todas las herramientas de cocina (platos, vasos, utensilios, etc.)",
                "Con aire acondicionado frío/calor.",
                "Con Smart TV", "Conexión a Internet gratuita", "1 Habitación.",
                "Para 4 personas.",
                "Apto para menores.",
                "Baño completamente equipado."],
            "symbols": [
                "fa-solid fa-couch",
                "fa-solid fa-plug",
                "fa-solid fa-kitchen-set ",
                "fa-solid fa-snowflake",
                "fa-solid fa-tv",
                "fa-solid fa-wifi",
                "fa-solid fa-bed",
                "fa-solid fa-user",
                "fa-solid fa-children",
                "fa-solid fa-sink"
            ],
            "images": [
                "assets/img/cv-apart-photos/dpto3-beds.JPG",
                "assets/img/cv-apart-photos/dpto3-beds2.JPG",
                "assets/img/cv-apart-photos/dpto3-smbed.JPG",
                "assets/img/cv-apart-photos/dpto3-kitchen.jpg",
                "assets/img/cv-apart-photos/dpto3-tv.JPG"
            ]
        },
        4: {
            "title": "Instalaciones",
            "description": ["Gran espacio verde",
                            "Estacionamiento Gratuito",
                            "Gran variedad de plantas",
                            "Parrilla Móvil",
                            "Parrilla Fija", "Piscina", "Ducha",
                            "Sillas", "Apto para menores",
                            "Espacio para compartir"],
            "symbols": [
                "fa-brands fa-pagelines",
                "fa-solid fa-square-parking",
                "fa-solid fa-leaf",
                "fa-solid fa-bacon",
                "fa-solid fa-drumstick-bite",
                "fa-solid fa-person-swimming",
                "fa-solid fa-shower",
                "fa-solid fa-chair",
                "fa-solid fa-children",
                "fa-solid fa-people-group"
            ],
            "images": [
                "assets/img/cv-apart-photos/flowers.jpg",
                "assets/img/cv-apart-photos/garden.jpg",
                "assets/img/cv-apart-photos/flowers2.jpg",
                "assets/img/cv-apart-photos/house-departments.jpg",
                "assets/img/cv-apart-photos/landscape.jpg",
                "assets/img/cv-apart-photos/landscape2.jpg",
                "assets/img/cv-apart-photos/landscape3.jpg",
                "assets/img/cv-apart-photos/next-pool.jpg",
                "assets/img/cv-apart-photos/pool-img.jpg",
                "assets/img/cv-apart-photos/pool-3.jpg",
                "assets/img/cv-apart-photos/pool-4.jpg",
                "assets/img/cv-apart-photos/pool-night.JPG",
                "assets/img/cv-apart-photos/pool-night2.JPG",
                "assets/img/cv-apart-photos/portatil-grill.jpg",
                "assets/img/cv-apart-photos/palm-trees.jpg",
                "assets/img/cv-apart-photos/grill.jpg",
                "assets/img/cv-apart-photos/grill2.jpg",
                "assets/img/cv-apart-photos/security.jpg",
                "assets/img/cv-apart-photos/flowers3.jpg",
                "assets/img/cv-apart-photos/pool-1.jpg",
                "assets/img/cv-apart-photos/pool-shower.jpg"
            ]
        }
    }

    requested_facility = departments[id]
    combined_data = [(description, symbols) for description, symbols in zip(requested_facility["description"],
                                                                            requested_facility["symbols"])]
    length_list = len(combined_data)
    return render_template("facility-info.html", requested_facility=requested_facility,
                           combinated_data=combined_data, lenght_list=length_list)


if __name__ == "__main__":
    app.run()

# Clivio Nicolás Vera Ortiz
