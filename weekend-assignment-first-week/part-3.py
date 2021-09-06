import psycopg2
import psycopg2.extras

try:

#connecting to local database 
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'data-internship',
        user='postgres',
        password='nischal541',
        port = 5432
    )

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

# creating tables as specified in assignment
    create_query = ''' CREATE SCHEMA IF NOT EXISTS general;
                       CREATE TABLE IF NOT EXISTS general.users(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            dob DATE,
                            profession VARCHAR(100)
                        );
                      
                        CREATE TABLE IF NOT EXISTS general.address(
                            id SERIAL PRIMARY KEY,
                            user_id INT NOT NULL,
                            permanent_address VARCHAR(10),
                            temporary_address VARCHAR(10),
                            CONSTRAINT fk_user_id
                            FOREIGN KEY(user_id) 
                            REFERENCES general.users(id)
                            ON DELETE CASCADE
                        ); 
                       
                '''
    cursor.execute(create_query)
    print ("Table Creation Success !")

# using pyformat parameter binding and executemany() method    
    insert_users = ''' INSERT INTO general.users("name","dob","profession")
                        VALUES(%(name)s, %(dob)s, %(profession)s);
                    '''
    users = ({
                'name': 'Jane Henderson',
                'dob': '1989-09-19',
                'profession': 'Actor'
            },
            {
                'name': 'Alice Sprigg',
                'dob': '1991-11-12',
                'profession': 'Mechanic'
            },
            {
                'name': 'Dave Carr',
                'dob': '1995-03-28',
                'profession': 'Banker'
            },
            {
                'name': 'Morris Beckman',
                'dob': '2010-07-07',
                'profession': 'Receptionist'
            }
    )
    
    cursor.executemany(insert_users, users)

    insert_address = ''' INSERT INTO general.address("user_id","permanent_address","temporary_address")
                        VALUES  (%(user_id)s, %(permanent_address)s, %(temporary_address)s)
                    '''
    addresses = ({
                'user_id': 1,
                'permanent_address': 'Jhapa',
                'temporary_address': 'Koteshwor'  
            },
            {
                'user_id': 2,
                'permanent_address': 'Syanga',
                'temporary_address': 'Lalitpur'  
            },
            {
                'user_id': 4,
                'permanent_address': 'Kathmandu',
                'temporary_address': 'Illam'  
            },
            {
                'user_id': 3,
                'permanent_address': 'Dhading',
                'temporary_address': 'Gongabuu'  
            },
            
    )
    
    cursor.executemany(insert_address, addresses)
    print ("Dummy Data Insertion Success !")

#getting user_id from command line input to fetch data from the joined users and address table 
    print ("Data Fetch Operation by Command Line Inputs")
    user_id = int(input("Enter User ID: "))

    data_fetch_query = ''' select * from general.address a
                            inner join general.users u on a.user_id = u.id
                            where user_id = %s;
                        '''
    cursor.execute(data_fetch_query, [user_id])
    result = cursor.fetchmany()
    print("The fetch query result for provided user id is: \n "+ str(result[0]))

#getting profession from command line input to fetch data from the joined users and address table 
    profession = input("Enter Profession: ")

    data_fetch_query = ''' select * from general.address a
                            inner join general.users u on a.user_id = u.id
                            where profession = %s;
                        '''
    cursor.execute(data_fetch_query, [profession])
    result = cursor.fetchmany()
    print("The fetch query result for provided profession is: \n "+ str(result[0]))

#getting permanent_address from command line input to fetch data from the joined users and address table 
    permanent_address = input("Enter Permanent Address: ")

    data_fetch_query = ''' select * from general.address a
                            inner join general.users u on a.user_id = u.id
                            where permanent_address = %s;
                        '''
    cursor.execute(data_fetch_query, [permanent_address])
    result = cursor.fetchmany()
    print("The fetch query result for provided permanent_address is: \n "+ str(result[0]))
    
#altering table users to add gender column
    adding_gender_query = '''
                   alter table general.users
                    add column gender varchar(10);
    '''
    cursor.execute(adding_gender_query)
    print("Alter Table to add gender column successful !")
    
#calculating age from birth date column and filtering less than 18 aged rows

    age_delete_query = '''delete from general.users where id not in (
                            select id as "age" from general.users where 
                            date_part('year', age(dob))>18
                            );
                        '''
    cursor.execute(age_delete_query)
    print("Records with age less than 18 deleted!")
    connection.commit()

except Exception as e:
    print('Error: ' + str(e))

finally:
    connection.close()
    cursor.close()