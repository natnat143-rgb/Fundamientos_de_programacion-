import json

#Colocar ISBN de los libros
biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    " 978-84-128-0463-8": {
        "título": "Noches Blancas",
        "autor": ["Fiódor Dostoievski"],
        "géneros": ["Romance", "Drama"]
    },
    "978-84-911-1814-5": {
        "título": "La metamorfosis",
        "autor": ["Franz Kafka"],
        "géneros": ["Novela filosofica"]
    },
    
    "978-60-738-2633-4": {
        "título": "El mito de Sisifo",
        "autor": ["Albert Camus"],
        "géneros": ["Fioosofia histórica"]
    }
}
    #Seleccionar el libro deseado para buscarlo
isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)