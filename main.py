from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional
from pydantic import Field

# Creamos la instancia de la aplicación FastAPI
app = FastAPI()

# Lista para almacenar los libros en memoria
books = []

# Modelo de datos para los libros
class Book(BaseModel):
    id: int
    titulo: str
    autor: str
    paginas: int = Field(..., gt=0, description="El número de páginas debe ser mayor que cero")
    editorial: Optional[str]

# Endpoint raíz
@app.get("/")
def index():
    return {"message": "Practica API ejemplo"}

# Endpoint para obtener un libro por ID
@app.get("/books/{id}")
def mostrar_books(id: int):
    for book in books:
        if book.id == id:
            return {"data": book}
    # Si no encontramos el libro, retornamos un error
    return {"error": "Libro no encontrado"}, 404

# Endpoint para insertar un libro
@app.post("/booksInsert")
def insertar_book(book: Book):
    books.append(book)
    return {"message": f"Libro '{book.titulo}' insertado"}
