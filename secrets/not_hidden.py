# Keep this file separate

def db1_secrets():
    return {"host": "IpAddOrHostName",
            "port": 5432,
            "database": "db1_name",
            "user": "username",
            "pass": "password"}

def db2_secrets():
    return {"host": "localhost",
            "port": 5433,
            "database": "deb2_name",
            "user": "username",
            "pass": "password"}
