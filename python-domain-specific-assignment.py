import psycopg2
import psycopg2.extras

try:

#q1. connecting to local database and creating tables
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'data-internship',
        user='postgres',
        password='nischal541',
        port = 5432
    )

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


    create_query = ''' CREATE SCHEMA IF NOT EXISTS hospital;
                       CREATE TABLE IF NOT EXISTS hospital.doctor_specialization(
                            id SERIAL PRIMARY KEY,
                            specialization_type VARCHAR(100) NOT NULL
                        );
                        CREATE TABLE IF NOT EXISTS hospital.patient(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            date_of_birth DATE NOT NULL DEFAULT '2000-01-01',
                            gender VARCHAR(100) NOT NULL
                        );
                        CREATE TABLE IF NOT EXISTS hospital.doctor(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            specialization INT NOT NULL,
                            phone_number VARCHAR(10),
                            CONSTRAINT fk_specialization
                            FOREIGN KEY(specialization) 
                            REFERENCES hospital.doctor_specialization(id)
                        ); 
                        CREATE TABLE IF NOT EXISTS hospital.appointment(
                            id SERIAL PRIMARY KEY,
                            doctor_id INT NOT NULL,
                            patient_id INT NOT NULL,
                            fee FLOAT NOT NULL,
                            diagnosis VARCHAR(100),
                            CONSTRAINT fk_doctor
                            FOREIGN KEY(doctor_id) 
                            REFERENCES hospital.doctor(id),
                            CONSTRAINT fk_patient
                            FOREIGN KEY(patient_id) 
                            REFERENCES hospital.patient(id)
                        );
                '''
    cursor.execute(create_query)

#q2.INSERT the following data in the tables. Use both execute() and executemany() methods with parameter binding.
#this sql queries are inserted using execute() method without parameter binding
    insert_single = '''INSERT INTO hospital.doctor_specialization 
                        VALUES (1, 'Anaesthesiologist'),(2, 'Surgeon'),(3, 'Psychiatrist');

                    INSERT INTO hospital.doctor(name, specialization, phone_number) 
                      VALUES ('Lionel Smart', 1, 2811232323),
                      ('Michelle Sanders', 2, 1899912310),
                      ('Pretti Patel', 3, 7980123982),
                      ('Sadiq Khan', 1, 7983129813),
                      ('Chaz Smith', 2, 2039820398);
                    '''
    cursor.execute(insert_single)

#the below queries use pyformat parameter binding and are executed by executemany() method    
    insert_query = ''' INSERT INTO hospital.patient(name, date_of_birth, gender) 
                      VALUES (%(name)s, %(dob)s, %(gender)s);
                    '''
    data = ({
                'name': 'Jane Henderson',
                'dob': '1989-09-19',
                'gender': 'Female'
            },
            {
                'name': 'Alice Sprigg',
                'dob': '1991-11-12',
                'gender': 'Female'
            },
            {
                'name': 'Dave Carr',
                'dob': '1995-03-28',
                'gender': 'Male'
            },
            {
                'name': 'Morris Beckman',
                'dob': '2001-07-07',
                'gender': 'Male'
            }
    )
    
    cursor.executemany(insert_query, data)

    insert_final = ''' INSERT INTO hospital.appointment(doctor_id, patient_id, fee, diagnosis) 
                      VALUES (%(doctorId)s, %(patientId)s, %(fee)s, %(diagnosis)s);
                    '''
    appointments = ({
                'doctorId': 1,
                'patientId': 2,
                'fee': 1000,
                'diagnosis': None
            },
            {
                'doctorId': 1,
                'patientId': 4,
                'fee': 1000,
                'diagnosis': 'Headache'
            },
            {
                'doctorId': 4,
                'patientId': 3,
                'fee': 2000,
                'diagnosis': None
            },
            {
                'doctorId': 2,
                'patientId': 1,
                'fee': 1500,
                'diagnosis': 'Backpain'
            }
            
    )
    
    cursor.executemany(insert_final, appointments)
    
#q3.GET the count of patients born after 1990.
    date_filter_query = '''
                            select count(*) from hospital.patient  where date_of_birth>= '1990-01-01'; 
                        '''
    cursor.execute(date_filter_query)
    result = cursor.fetchone()
    print("The count of patients born after 1990 is: "+ str(result[0]))
    
#q4.GET the appointments made with “Surgeon” specialized doctors.
    appointment_query = '''
                    select a.*, da.specialization_type from hospital.appointment as a
                    inner join hospital.doctor as d on a.doctor_id = d.id
                    inner join hospital.doctor_specialization as da on d.specialization = da.id
                    where da.specialization_type = 'Surgeon';
    '''
    cursor.execute(appointment_query)
    appointment_result = cursor.fetchmany()
    print("The Appointments made with “Surgeon” specialized doctors are: ")
    print(appointment_result)
    
#q5.UPDATE fees of appointments and reduce them by 25%.

    fee_update_query = '''update hospital.appointment
                          set fee = fee-0.25*fee;
                        '''
    cursor.execute(fee_update_query)

#q6.UPDATE phone_number of Chaz Smith to 1231292310.
    phone_number_update_query = '''update hospital.doctor 
                                set phone_number = '1231292310'
                                where name='Chaz Smith';
                                '''
    cursor.execute(phone_number_update_query)

#q7.DELETE all doctors who are specialized as “Psychiatrist”.
    delete_query = '''delete from hospital.doctor where id not in (select d.id from hospital.doctor as d
                      inner join hospital.doctor_specialization as da on d.specialization = da.id 
                      where da.specialization_type != 'Psychiatrist'); 
                    '''
    cursor.execute(delete_query)
    connection.commit()

except Exception as e:
    print('Error: ' + str(e))

finally:
    connection.close()
    cursor.close()