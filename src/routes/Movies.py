from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Movies import Movie

# Models
from models.MoviesModel import MoviesModel

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_movies():
    try:
        movies = MoviesModel.get_movies()
        return jsonify(movies)
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@main.route('/<id>')
def get_movie(id):
    try:
        movie = MoviesModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        id = uuid.uuid4()
        movie = Movie(str(id), title, duration, released)

        affected_rows = MoviesModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as e:
        return jsonify({'message': str(e)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)

        affected_rows = MoviesModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie to delete"}), 404

    except Exception as e:
        return jsonify({'message': str(e)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = request.json['duration']
        released = request.json['released']
        movie = Movie(id, title, duration, released)

        affected_rows = MoviesModel.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movies can be updates"}), 500

    except Exception as e:
        return jsonify({'message': str(e)}), 500
