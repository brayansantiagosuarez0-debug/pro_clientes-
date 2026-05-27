from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "este es el proyecto de clientes a desarrollar"}


@app.get("/clientes")
def obtener_clientes():
    clientes = [
        {"id": 1, "nombre": "Andrés Morales",  "email": "andres.morales@email.com",  "ciudad": "Bogotá",       "telefono": "300-111-2233"},
        {"id": 2, "nombre": "Laura Gómez",     "email": "laura.gomez@email.com",     "ciudad": "Medellín",     "telefono": "311-222-3344"},
        {"id": 3, "nombre": "Carlos Ruiz",     "email": "carlos.ruiz@email.com",     "ciudad": "Cali",         "telefono": "322-333-4455"},
        {"id": 4, "nombre": "Valentina Cruz",  "email": "valentina.cruz@email.com",  "ciudad": "Cartagena",    "telefono": "333-444-5566"},
        {"id": 5, "nombre": "Diego Herrera",   "email": "diego.herrera@email.com",   "ciudad": "Barranquilla", "telefono": "344-555-6677"},
        {"id": 6, "nombre": "Camila Torres",   "email": "camila.torres@email.com",   "ciudad": "Bucaramanga",  "telefono": "355-666-7788"},
        {"id": 7, "nombre": "Sebastián López", "email": "sebastian.lopez@email.com", "ciudad": "Manizales",    "telefono": "366-777-8899"},
    ]
    return {"status": "success", "total": len(clientes), "data": clientes}
