# C:\Users\ianes\Desktop\AS Cloud\app\auth\routes.py

from flask import render_template, redirect, url_for, flash, request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models import User
from .forms import RegistrationForm, LoginForm

auth_bp = Blueprint(
    'auth', __name__,
    template_folder='templates/auth'
)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password_hash=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Conta criada! Faça login.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            next_page = request.args.get('next') or url_for('index')
            return redirect(next_page)
        flash('Email ou senha inválidos.', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu.', 'info')
    return redirect(url_for('index'))
