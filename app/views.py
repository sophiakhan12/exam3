# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect, url_for, flash
from jinja2  import TemplateNotFound

# App modules
from app import app, cursor, dbConn
# from app.models import Profiles

# App main route + generic routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/searchsuppliers')
def SearchSuppliers():
    return render_template('searchSuppliers.html')

@app.route('/suppliersearchresult', methods = ['GET'])
def SupplierSearchResult():
    city = request.args.get('city')
    sql = "select * from Suppliers where City=%s"
    cursor.execute(sql, city) 
    suppliersData = cursor.fetchall()
    return render_template('supplierSearchResult.html', suppliersData = suppliersData)

    
    