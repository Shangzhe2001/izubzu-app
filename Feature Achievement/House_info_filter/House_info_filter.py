# Set-Ups 
from flask import Flask, request, jsonify, send_file, render_template
from werkzeug.utils import secure_filename
import joblib
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy import create_engine, inspect, select, text, and_, or_, func
from sqlalchemy import Table, MetaData

from datetime import datetime
import calendar

import json
import matplotlib.pyplot as plt

passwd = '200101'
w_engine = create_engine('postgresql+psycopg2://postgres:' + passwd + '@localhost:5432/Proj-App', echo=True)

m2 = MetaData(bind=w_engine)
m2.reflect()

house_info = Table("house_info", m2, autoload=True)

app = Flask(__name__)

# API for ASC expected_price
def ex_asc_f(Area, Negotiable, Available_date, Bedroom_no):
    A_date = datetime.strptime(Available_date, '%Y-%m-%d')
    stmt = select([house_info]).where(house_info.c.house_status == 'FOR RENT').\
        where(house_info.c.area == Area).\
        where(house_info.c.negotiable == Negotiable).\
        where(house_info.c.available_date < A_date).\
        where(house_info.c.number_of_bedrooms == Bedroom_no).\
        order_by(house_info.c.expected_price).limit(2)
    
    with w_engine.connect() as con:
        d = con.execute(stmt)
    
    return d.fetchall()

@app.route("/expected_price/asc")
def ex_asc():
    Area = request.args.get('Area') 
    Negotiable = request.args.get('Negotiable')
    Available_date = request.args.get('Available_date')
    Bedroom_no = request.args.get('Bedroom_no')

    s1 = ex_asc_f(Area, Negotiable, Available_date, Bedroom_no)

    c1,c2,c3,c4,c5,c6,c7,c8 = [],[],[],[],[],[],[],[]
    c9,c10,c11,c12,c13,c14,c15 = [],[],[],[],[],[],[]

    for i in range(len(s1)):
        c1.append(s1[i][0])
        c2.append(s1[i][1])
        c3.append(s1[i][2])
        c4.append(s1[i][3])
        c5.append(s1[i][4])
        c6.append(s1[i][5])
        c7.append(s1[i][6])
        c8.append(s1[i][7])   
        c9.append(s1[i][8])  
        c10.append(s1[i][9])  
        c11.append(s1[i][10])  
        c12.append(s1[i][11])  
        c13.append(s1[i][12])  
        c14.append(s1[i][13])  
        c15.append(s1[i][14]) 
    
    dic = {"house_title":c1,"area":c2,"room_size":c3,"house_location":c4,
    "postal_code":c5,"number_of_bedrooms":c6,"number_of_washrooms":c7,
    "max_tenant":c8,"available_date":c9,"expected_price":c10,"price_per_feet":c11,
    "negotiable":c12,"owner_email":c13,"owner_phone_number":c14,"house_status":c15}

    return dic


# API for DESC expected_price
def ex_desc_f(Area, Negotiable, Available_date, Bedroom_no):
    A_date = datetime.strptime(Available_date, '%Y-%m-%d')
    stmt = select([house_info]).where(house_info.c.house_status == 'FOR RENT').\
        where(house_info.c.area == Area).\
        where(house_info.c.negotiable == Negotiable).\
        where(house_info.c.available_date < A_date).\
        where(house_info.c.number_of_bedrooms == Bedroom_no).\
        order_by(house_info.c.expected_price.desc()).limit(2)
    
    with w_engine.connect() as con:
        d = con.execute(stmt)
    
    return d.fetchall()

@app.route("/expected_price/desc")
def ex_desc():
    Area = request.args.get('Area') 
    Negotiable = request.args.get('Negotiable')
    Available_date = request.args.get('Available_date')
    Bedroom_no = request.args.get('Bedroom_no')

    s1 = ex_desc_f(Area, Negotiable, Available_date, Bedroom_no)

    c1,c2,c3,c4,c5,c6,c7,c8 = [],[],[],[],[],[],[],[]
    c9,c10,c11,c12,c13,c14,c15 = [],[],[],[],[],[],[]

    for i in range(len(s1)):
        c1.append(s1[i][0])
        c2.append(s1[i][1])
        c3.append(s1[i][2])
        c4.append(s1[i][3])
        c5.append(s1[i][4])
        c6.append(s1[i][5])
        c7.append(s1[i][6])
        c8.append(s1[i][7])   
        c9.append(s1[i][8])  
        c10.append(s1[i][9])  
        c11.append(s1[i][10])  
        c12.append(s1[i][11])  
        c13.append(s1[i][12])  
        c14.append(s1[i][13])  
        c15.append(s1[i][14]) 
    
    dic = {"house_title":c1,"area":c2,"room_size":c3,"house_location":c4,
    "postal_code":c5,"number_of_bedrooms":c6,"number_of_washrooms":c7,
    "max_tenant":c8,"available_date":c9,"expected_price":c10,"price_per_feet":c11,
    "negotiable":c12,"owner_email":c13,"owner_phone_number":c14,"house_status":c15}

    return dic

# API for ASC price_per_feet
def psf_asc_f(Area, Negotiable, Available_date, Bedroom_no):
    A_date = datetime.strptime(Available_date, '%Y-%m-%d')
    stmt = select([house_info]).where(house_info.c.house_status == 'FOR RENT').\
        where(house_info.c.area == Area).\
        where(house_info.c.negotiable == Negotiable).\
        where(house_info.c.available_date < A_date).\
        where(house_info.c.number_of_bedrooms == Bedroom_no).\
        order_by(house_info.c.price_per_feet).limit(2)
    
    with w_engine.connect() as con:
        d = con.execute(stmt)
    
    return d.fetchall()

@app.route("/price_per_feet/asc")
def psf_asc():
    Area = request.args.get('Area') 
    Negotiable = request.args.get('Negotiable')
    Available_date = request.args.get('Available_date')
    Bedroom_no = request.args.get('Bedroom_no')

    s1 = psf_asc_f(Area, Negotiable, Available_date, Bedroom_no)

    c1,c2,c3,c4,c5,c6,c7,c8 = [],[],[],[],[],[],[],[]
    c9,c10,c11,c12,c13,c14,c15 = [],[],[],[],[],[],[]

    for i in range(len(s1)):
        c1.append(s1[i][0])
        c2.append(s1[i][1])
        c3.append(s1[i][2])
        c4.append(s1[i][3])
        c5.append(s1[i][4])
        c6.append(s1[i][5])
        c7.append(s1[i][6])
        c8.append(s1[i][7])   
        c9.append(s1[i][8])  
        c10.append(s1[i][9])  
        c11.append(s1[i][10])  
        c12.append(s1[i][11])  
        c13.append(s1[i][12])  
        c14.append(s1[i][13])  
        c15.append(s1[i][14]) 
    
    dic = {"house_title":c1,"area":c2,"room_size":c3,"house_location":c4,
    "postal_code":c5,"number_of_bedrooms":c6,"number_of_washrooms":c7,
    "max_tenant":c8,"available_date":c9,"expected_price":c10,"price_per_feet":c11,
    "negotiable":c12,"owner_email":c13,"owner_phone_number":c14,"house_status":c15}

    return dic

# API for DESC price_per_feet
def psf_desc_f(Area, Negotiable, Available_date, Bedroom_no):
    A_date = datetime.strptime(Available_date, '%Y-%m-%d')
    stmt = select([house_info]).where(house_info.c.house_status == 'FOR RENT').\
        where(house_info.c.area == Area).\
        where(house_info.c.negotiable == Negotiable).\
        where(house_info.c.available_date < A_date).\
        where(house_info.c.number_of_bedrooms == Bedroom_no).\
        order_by(house_info.c.price_per_feet.desc()).limit(2)
    
    with w_engine.connect() as con:
        d = con.execute(stmt)
    
    return d.fetchall()

@app.route("/price_per_feet/desc")
def psf_desc():
    Area = request.args.get('Area') 
    Negotiable = request.args.get('Negotiable')
    Available_date = request.args.get('Available_date')
    Bedroom_no = request.args.get('Bedroom_no')

    s1 = psf_desc_f(Area, Negotiable, Available_date, Bedroom_no)

    c1,c2,c3,c4,c5,c6,c7,c8 = [],[],[],[],[],[],[],[]
    c9,c10,c11,c12,c13,c14,c15 = [],[],[],[],[],[],[]

    for i in range(len(s1)):
        c1.append(s1[i][0])
        c2.append(s1[i][1])
        c3.append(s1[i][2])
        c4.append(s1[i][3])
        c5.append(s1[i][4])
        c6.append(s1[i][5])
        c7.append(s1[i][6])
        c8.append(s1[i][7])   
        c9.append(s1[i][8])  
        c10.append(s1[i][9])  
        c11.append(s1[i][10])  
        c12.append(s1[i][11])  
        c13.append(s1[i][12])  
        c14.append(s1[i][13])  
        c15.append(s1[i][14]) 
    
    dic = {"house_title":c1,"area":c2,"room_size":c3,"house_location":c4,
    "postal_code":c5,"number_of_bedrooms":c6,"number_of_washrooms":c7,
    "max_tenant":c8,"available_date":c9,"expected_price":c10,"price_per_feet":c11,
    "negotiable":c12,"owner_email":c13,"owner_phone_number":c14,"house_status":c15}

    return dic

# API for ASC room_size
def rs_asc_f(Area, Negotiable, Available_date, Bedroom_no):
    A_date = datetime.strptime(Available_date, '%Y-%m-%d')
    stmt = select([house_info]).where(house_info.c.house_status == 'FOR RENT').\
        where(house_info.c.area == Area).\
        where(house_info.c.negotiable == Negotiable).\
        where(house_info.c.available_date < A_date).\
        where(house_info.c.number_of_bedrooms == Bedroom_no).\
        order_by(house_info.c.room_size).limit(2)
    
    with w_engine.connect() as con:
        d = con.execute(stmt)
    
    return d.fetchall()

@app.route("/room_size/asc")
def rs_asc():
    Area = request.args.get('Area') 
    Negotiable = request.args.get('Negotiable')
    Available_date = request.args.get('Available_date')
    Bedroom_no = request.args.get('Bedroom_no')

    s1 = rs_asc_f(Area, Negotiable, Available_date, Bedroom_no)

    c1,c2,c3,c4,c5,c6,c7,c8 = [],[],[],[],[],[],[],[]
    c9,c10,c11,c12,c13,c14,c15 = [],[],[],[],[],[],[]

    for i in range(len(s1)):
        c1.append(s1[i][0])
        c2.append(s1[i][1])
        c3.append(s1[i][2])
        c4.append(s1[i][3])
        c5.append(s1[i][4])
        c6.append(s1[i][5])
        c7.append(s1[i][6])
        c8.append(s1[i][7])   
        c9.append(s1[i][8])  
        c10.append(s1[i][9])  
        c11.append(s1[i][10])  
        c12.append(s1[i][11])  
        c13.append(s1[i][12])  
        c14.append(s1[i][13])  
        c15.append(s1[i][14]) 
    
    dic = {"house_title":c1,"area":c2,"room_size":c3,"house_location":c4,
    "postal_code":c5,"number_of_bedrooms":c6,"number_of_washrooms":c7,
    "max_tenant":c8,"available_date":c9,"expected_price":c10,"price_per_feet":c11,
    "negotiable":c12,"owner_email":c13,"owner_phone_number":c14,"house_status":c15}

    return dic

# API for DESC room_size
def rs_desc_f(Area, Negotiable, Available_date, Bedroom_no):
    A_date = datetime.strptime(Available_date, '%Y-%m-%d')
    stmt = select([house_info]).where(house_info.c.house_status == 'FOR RENT').\
        where(house_info.c.area == Area).\
        where(house_info.c.negotiable == Negotiable).\
        where(house_info.c.available_date < A_date).\
        where(house_info.c.number_of_bedrooms == Bedroom_no).\
        order_by(house_info.c.room_size.desc()).limit(2)
    
    with w_engine.connect() as con:
        d = con.execute(stmt)
    
    return d.fetchall()

@app.route("/room_size/desc")
def rs_desc():
    Area = request.args.get('Area') 
    Negotiable = request.args.get('Negotiable')
    Available_date = request.args.get('Available_date')
    Bedroom_no = request.args.get('Bedroom_no')

    s1 = rs_desc_f(Area, Negotiable, Available_date, Bedroom_no)

    c1,c2,c3,c4,c5,c6,c7,c8 = [],[],[],[],[],[],[],[]
    c9,c10,c11,c12,c13,c14,c15 = [],[],[],[],[],[],[]

    for i in range(len(s1)):
        c1.append(s1[i][0])
        c2.append(s1[i][1])
        c3.append(s1[i][2])
        c4.append(s1[i][3])
        c5.append(s1[i][4])
        c6.append(s1[i][5])
        c7.append(s1[i][6])
        c8.append(s1[i][7])   
        c9.append(s1[i][8])  
        c10.append(s1[i][9])  
        c11.append(s1[i][10])  
        c12.append(s1[i][11])  
        c13.append(s1[i][12])  
        c14.append(s1[i][13])  
        c15.append(s1[i][14]) 
    
    dic = {"house_title":c1,"area":c2,"room_size":c3,"house_location":c4,
    "postal_code":c5,"number_of_bedrooms":c6,"number_of_washrooms":c7,
    "max_tenant":c8,"available_date":c9,"expected_price":c10,"price_per_feet":c11,
    "negotiable":c12,"owner_email":c13,"owner_phone_number":c14,"house_status":c15}

    return dic