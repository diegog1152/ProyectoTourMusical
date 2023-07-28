import json

class Review:
    def __init__(self, id_evento, calificacion, comentario, animo):
        self.id_evento = id_evento
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

def cargar_reviews_desde_json():
    try:
        with open("reviews.json", "r") as file:
            data = json.load(file)
            reviews = []
            for review_data in data:
                review = Review(
                    review_data["id_evento"],
                    review_data["calificacion"],
                    review_data["comentario"],
                    review_data["animo"]
                )
                reviews.append(review)
            return reviews
    except FileNotFoundError:
        return []

def guardar_review(review):
    try:
        with open("reviews.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append({
        "id_evento": review.id_evento,
        "calificacion": review.calificacion,
        "comentario": review.comentario,
        "animo": review.animo
    })

    with open("reviews.json", "w") as file:
        json.dump(data, file)
