from flask import Flask
from flask import request
from ldap3 import Server, Connection, NTLM
from Crypto.Hash import MD4

app = Flask(__name__)

@app.route("/")
def index():
    user_value = request.args.get("user_value", "")
    if user_value:
        group_memb = membership(user_value)
    else:
        group_memb = ""
    return (
        """<form action="" method="get">
                Usuario: <input type="text" name="user_value">
                <input type="submit" value="Consulta">
            </form>"""
        + "Resultado: "
        + group_memb
        )

def membership(user_value):
    try:
        server = Server("garrahan.gov.ar") 

        with Connection(server, user="{}\\{}".format("garrahan.gov.ar", "test"), password="Test1234", authentication=NTLM) as conn:
            conn.search("dc=garrahan,dc=gov,dc=ar", "(&(sAMAccountName={}))".format(user_value),
                        attributes=['memberOf'])
            entry = conn.entries

        for group in entry[0]['memberOf']:
            if group.startswith('CN=Internet'):
                return group
    
    except IndexError: #If user doesn't exist
         return("No existe el usuario")

if __name__ == "__main__":
    app.run(debug=True)