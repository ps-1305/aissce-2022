#================================================={backend.py}=====================================================
import mysql.connector as sql

# patient_info TABLE STRUCTURE 
# id | f_name | l_name | age | sex | ward | doctor | status | days
# VARIABLES IN THIS FILE CORRESPONDING TO THE ABOVE HEADERS 
# id | name | name2 | age | sex | ward | doctor | status | days 


# ----------------------------------(login_screen.py) BACKEND------------------------------------------------------

# LOGIN FUNCTION
# PARAMETERS: username, password
# CONNECT MySQL DATABASE AND RETRIEVE DATA FROM usernames TABLE FOR COMPARISON
# RETURNS True IF PERFECT MATCH FOUND, False OTHERWISE 
def login(username, password):
    db = sql.connect(host='', user='', password='')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(f"SELECT * FROM usernames WHERE username='{username}' AND psswd='{password}';")
    if len(cursor.fetchall()) == 1:
        return True
    else:
        return False


# -------------------------------------------(app.py) BACKEND--------------------------------------------------------

# ADDING A PATIENT
# PARAMETERS: name, name2, age, sex, ward, doctor, status, days (DEFAULT VALUE = 1)
# CONNECT TO MySQL DATABASE AND CREATE THE patient_info TABLE IF IT DOES NOT EXIST
# ADD THE GIVEN DATA TO THE TABLE AND COMMIT TO THE QUERIES 
def addPatient(name, name2, age, sex, ward, doctor, status, days=1):
    db = sql.connect(host='', user='', password='')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS patient_info('
        'id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,'
        'f_name VARCHAR(10),'
        'l_name VARCHAR(10), '
        'age INTEGER, '
        'sex VARCHAR(6), '
        'ward VARCHAR(10), '
        'doctor VARCHAR(15), '
        'status VARCHAR(7), '
        'days INTEGER)',
    )
    cursor.execute(
        f"INSERT INTO patient_info(f_name,l_name, age, sex, ward, doctor, status, days) "
        f"VALUES ('{name}','{name2}',{age},'{sex}','{ward}','{doctor}','{status}',{days})")
    db.commit()
    db.close()


# SEARCHING A PATIENT 
# PARAMETERS: param, value
# CONNECT TO MySQL DATABASE AND SEARCH FOR THOSE RECORDS WHERE param = value USING THE select...from...where QUERY
# COMMIT TO THE QUERY, CLOSE THE DATABASE AND THEN RETURN THE DATA COLLECTED 
# SELECTIVE SEARCHING HAS BEEN CARRIED OUT BY MAKING A NEW WINDOW USING TopLevel() FUNCTION
def getInfo(param, value):
    try:
        db = sql.connect(host='', user='', password='')
        cursor = db.cursor()
        cursor.execute('USE alpha_healthcare')
        cursor.execute(
            f"SELECT * FROM patient_info WHERE {param}='{value}'"
        )
        row = cursor.fetchall()
        db.commit()
        db.close()
        return row
    except sql.errors.ProgrammingError:
        return []


# SEARCHING A PATIENT THROUGH ITS id AND RETURN A TUPLE (bool, bool OR record_found)
# PARAMETER: id 
# CONNECT TO THE MySQL DATABASE AND THEN SEARCH WITH THE id USING select...from...where QUERY
# FETCH ALL THE RECORDS FOUND AND SAVE TO THE row VARIABLE
# IF RECORD PRESENT, len(row) == 1 AND FUNCTION RETURNS (True, row)
# IF RECORD ABSENT, len(row) != 1 AND FUNCTION RETURNS (False, False)
# THESE TUPLES ARE USED FOR FURTHER CHECKING IN THE FRONT-END (@ LINE 140, app.py)
# ON THE FRONT-END, THIS FUNCTION IS FURTHER USED FOR UPDATING THE PATIENT 
def updatePatient_search(id):
    try:
        db = sql.connect(host='', user='', password='')
        cursor = db.cursor()
        cursor.execute('USE alpha_healthcare')
        cursor.execute(
            f"SELECT * FROM patient_info WHERE id={id}"
        )
        row = cursor.fetchall()
        db.commit()
        db.close()
        if len(row) == 1:
            return True, row
        else:
            return False, False
    except sql.errors.ProgrammingError:
        return False, False


# UPDATING A PATIENT
# PARAMETERS: id, name, name2, age, sex, ward, doctor, status, days
# CONNECT TO THE MySQL DATABASE AND UPDATE THE RECORD USING update...set QUERY
# COMMIT TO THE QUERY AND CLOSE THE DATABASE
# None RETURNED
def updatePatient(id, name, name2, age, sex, ward, doctor, status, days):
    db = sql.connect(host='', user='', password='')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(
        f"UPDATE patient_info SET f_name='{name}',"
        f"l_name = '{name2}',"
        f"age = {age},"
        f"sex = '{sex}',"
        f"ward = '{ward}',"
        f"doctor = '{doctor}',"
        f"status = '{status}',"
        f"days={days} WHERE id={id}"
    )
    db.commit()
    db.close()


# ADMITTING A PATIENT 
# PARAMETERS: name, name2, age, sex, ward, doctor, days
# USE THE addPatient() FUNCTION WITH THE STATUS SET TO 'Admit'
def admit(name, name2, age, sex, ward, doctor, days):
    addPatient(name, name2, age, sex, ward, doctor, status='Admit', days=days)


# DISCHARGING A PATIENT
# PARAMETERS: id
# CONNECT TO THE MySQL DATABASE AND CREATE A discharged_patient TABLE IF IT DOESN'T EXIST
# INSERT INTO THE discharged_patient TABLE THE INFORMATION OF THE PATIENT WHO IS DISCHARGED BY FILTERING
# THROUGH id USING insert into...select...from...where QUERY
# UPDATE THE STATUS OF THE PATIENT TO 'Dschrgd' (DISCHARGED) IN THE patient_info TABLE USING update...set...where QUERY
# RETURN THE INFO OF THE PATIENT DISCHARGED USING THE select...from...where QUERY
# COMMIT TO THE QUERY AND CLOSE THE DATABASE
def discharge(id):
    db = sql.connect(host='', user='', password='')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(f'CREATE TABLE IF NOT EXISTS discharged_patient('
                   'id INTEGER,'
                   'f_name VARCHAR(10),'
                   'l_name VARCHAR(10), '
                   'age INTEGER, '
                   'sex VARCHAR(6), '
                   'ward VARCHAR(10), '
                   'doctor VARCHAR(15), '
                   'p_status VARCHAR(7), '
                   'days INTEGER,'
                   'FOREIGN KEY(id) REFERENCES patient_info(id))')
    cursor.execute(f"INSERT INTO discharged_patient(id, f_name, l_name, age, sex, ward, doctor, p_status, days) "
                   f"SELECT id, f_name, l_name, age, sex, ward, doctor, status, days "
                   f"FROM patient_info "
                   f"WHERE id = {id}")
    cursor.execute(f"UPDATE patient_info SET status = 'Dschrgd' WHERE id = {id}")
    cursor.execute(f"SELECT * FROM discharged_patient WHERE id={id} ")
    row = cursor.fetchall()
    db.commit()
    db.close()
    return row


# BILLING A PATIENT
# PARAMETERS: ward, status, days
# CONNECT TO THE MySQL DATABASE AND RETRIEVE THE FEES PER DAY USING THE select...from...where QUERY
# CALCULATING THE TOTAL AMOUNT
# RETURNING THE DIFFERENT FORMS OF AMOUNTS CALCULATED AND THE TOTAL AMOUNT IN A TUPLE
# CHECKUP FEES == 200, ADMIT FEES == 1000, WARD FEES == AS PER TABLE AND DOCTOR FEES == 500
# COMMIT TO THE QUERY AND CLOSE THE DATABASE
def billing(ward, status, days):
    try:
        db = sql.connect(host='', user='', password='')
        cursor = db.cursor()
        cursor.execute('USE alpha_healthcare')
        cursor.execute(f"SELECT fees FROM ward_info WHERE ward= '{ward}'")
        row = cursor.fetchall()
        fees = row[0][0]
        # WARD AMOUNT FEES
        w_amt = fees * days
        # STATUS AMOUNT FEES
        s_amt = 0
        fees *= days
        if status == 'Admit':
            fees += 1000
            s_amt += 1000
        elif status == 'Checkup':
            fees += 200
            s_amt += 200
        db.commit()
        db.close()
        # WARD FEES, WARD AMOUNT TOTAL, STATUS AMOUNT TOTAL, TOTAL AMOUNT INCL DOCTOR FEES
        return row[0][0], w_amt, [status, s_amt], fees + 500
    except sql.errors.ProgrammingError:
        pass


# SHOWING ALL ENTRIES
# PARAMETERS: NONE 
# CONNECT TO THE MySQL DATABASE AND COLLECT ALL THE RECORDS INTO A VARIABLE rows
# rows IS A LIST OF TUPLES
# APPEND ALL THE RECORDS IN rows TO main WITH AN EXPLICIT CONVERSION OF THE TUPLES INTO LISTS
# RETURN THE main LIST 
def showAll():
    db = sql.connect(host='', user='', password='')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute('SELECT * FROM patient_info')
    rows = cursor.fetchall()
    main = []
    for row in rows:
        main.append(list(row))
    return main

# ---------------------------------END------------------------------------------------------
