import psycopg2


def insert_into_postgresql(database_name, table_name, results):
    '''
    Insert loan features and expected IRR into PostgresQL database.
    '''
    conn = psycopg2.connect(dbname=database_name, user='postgres', host='/tmp')
    c = conn.cursor()

    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS {}
            (
                id VARCHAR (50),
                sub_grade VARCHAR (50),
                term VARCHAR (50),
                amount VARCHAR (50),
                percent_fund VARCHAR (50),
                int_rate VARCHAR (50),
                irr VARCHAR (50),
                percent_diff VARCHAR (50)
            );
        '''.format(table_name)
    )

    for result in results:
        c.execute(
            ''' 
            INSERT INTO {}
            VALUES ({}, {}, {}, {}, {}, {}, {}, {});
            '''.format(table_name, *result)

        )

    conn.commit()
    conn.close()