# C:\Users\ianes\Desktop\AS Cloud\app\cars\routes.py

from flask import render_template, redirect, url_for, flash, Blueprint, abort
from flask_login import login_required, current_user
from app import db
from app.models import Car
from .forms import CarForm

cars_bp = Blueprint(
    'cars', __name__,
    template_folder='templates/cars'
)

@cars_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_car():
    form = CarForm()
    if form.validate_on_submit():
        carro = Car(
            name=form.name.data,
            user_id=current_user.id,
            photo=form.photo.data,
            description=form.description.data,
            start_year=form.start_year.data,
            end_year=form.end_year.data,
            horsepower=form.horsepower.data,
            torque=form.torque.data,
            top_speed=form.top_speed.data,
            drive_type=form.drive_type.data,
            transmission=form.transmission.data
        )
        db.session.add(carro)
        db.session.commit()
        flash('Carro criado com sucesso!', 'success')
        return redirect(url_for('cars.list_cars'))
    return render_template('cars/create.html', form=form)

@cars_bp.route('/', methods=['GET'])
def list_cars():
    # mostra todos os carros (no futuro separar do seu e dos outros)
    carros = Car.query.all()
    return render_template('cars/list.html', carros=carros)


@cars_bp.route('/<int:car_id>', methods=['GET'])
def car_detail(car_id):
    carro = Car.query.get_or_404(car_id)
    return render_template('cars/detail.html', carro=carro)

@cars_bp.route('/<int:car_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_car(car_id):
    carro = Car.query.get_or_404(car_id)
    if carro.user_id != current_user.id:
        abort(403)
    form = CarForm(obj=carro)
    if form.validate_on_submit():
        carro.name         = form.name.data
        carro.photo        = form.photo.data
        carro.description  = form.description.data
        carro.start_year   = form.start_year.data
        carro.end_year     = form.end_year.data
        carro.horsepower   = form.horsepower.data
        carro.torque       = form.torque.data
        carro.top_speed    = form.top_speed.data
        carro.drive_type   = form.drive_type.data
        carro.transmission = form.transmission.data
        db.session.commit()
        flash('Carro atualizado com sucesso!', 'success')
        return redirect(url_for('cars.car_detail', car_id=carro.id))
    return render_template('cars/edit.html', form=form, carro=carro)

@cars_bp.route('/<int:car_id>/delete', methods=['GET'])
@login_required
def delete_car(car_id):
    carro = Car.query.get_or_404(car_id)
    if carro.user_id != current_user.id:
        abort(403)
    db.session.delete(carro)
    db.session.commit()
    flash('Carro excluído.', 'info')
    return redirect(url_for('cars.list_cars'))