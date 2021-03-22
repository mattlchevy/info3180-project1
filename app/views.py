"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
import os
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from app.model import Property
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property', methods=['GET', 'POST'])
def new_property():
    """ displays form for new property"""
    form = PropertyForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data 
        num_bedrooms = form.num_bedrooms.data
        num_bathrooms = form.num_bathrooms.data
        description = form.description.data
        location = form.location.data
        types = form.types.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        flash('Thank you for completing our Form!')
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user_property = Property(title, description, num_bedrooms, num_bathrooms, location, types, filename)
        db.session.add(user_property)
        db.session.commit()
        return redirect(url_for('properties'))
    return render_template('new_property.html', form=form)      

@app.route('/properties')
def properties():
    """ list of all properties in grid fashion"""

    db = connect_db()
    cur = db.cursor()
    cur.execute('select * from Property ')
    properties = cur.fetchall()
    return render_template('properties.html', properties=properties)


@app.route('/property/<int:propertyid>')
def property_page(propertyid):
    """ viewing individual property via property ID """
    return Property.query.get(int(propertyid))

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
