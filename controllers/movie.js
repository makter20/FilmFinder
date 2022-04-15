const movieRouter = require("express").Router()
const Movie = require("../models/Movie")

movieRouter.get("/", (req, res) => {
    Movie.find({}).then((users) => {
        res.json(users)
    })
})

movieRouter.get("/:movieId", (req, res, next) => {
    id = req.params.movieId
    Movie.findOne({movieId: id}, function (error, docs) {
        if (error) {
            next(error)
        }

        else {
            res.json(docs)
        }

    })
})

movieRouter.post("/", (req, res, next) => {

    newMovie = new Movie({
        movieId: req.body.movieId,
        title: req.body.title,
        date: new Date(req.body.date),
        genres: req.body.genres
    })

    if(newMovie) {
        newMovie
            .save()
            .then((savedMovie) => {
                res.json(savedMovie)
            })
            .catch((error) => {
                next(error)
            })
    }

})



//delete and update

module.exports = movieRouter