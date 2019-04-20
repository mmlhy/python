

def db_handler(conn_params):

    if conn_params['engine'] == 'file_storage':
        return conn_params['path']
