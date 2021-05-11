# read database connection url from the enivron variable we just set.
import psycopg2
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

cmd_create_action_table = """CREATE TABLE actions (
                              action VARCHAR(255) NOT NULL,
                              path VARCHAR(255) NOT NULL,
                              status BOOLEAN NOT NULL DEFAULT FALSE
                             )
                          """

con = None
try:
    # create a new database connection by calling the connect() function
    con = psycopg2.connect(database="dc3ocvbn0f13vv", user = "dmgssjxsfjwrbz", password = "899e7532b3c6fee46cc02717e9806e9308c318103a138bdcf760d4ce80cfce74", host = "ec2-54-224-120-186.compute-1.amazonaws.com", port = "5432")

    #  create a new cursor
    cur = con.cursor()

    # copy file into the table just created
    with open('fac.csv', 'r') as f:
        next(f)  # Skip the header row.
    # f , <database name>, Comma-Seperated
    cur.copy_from(f, 'cmd_create_action_table', sep=',')
    # Commit Changes
    con.commit()
    # Close connection
    conn.close()
    f.close()

    cur.execute(cmd_create_action_table)

    # close the communication with the HerokuPostgres
    cur.close()
except Exception as error:
    print('Could not connect to the Database.')
    print('Cause: {}'.format(error))

finally:
    # close the communication with the database server by calling the close()
    if con is not None:
        con.close()
        print('Database connection closed.')
