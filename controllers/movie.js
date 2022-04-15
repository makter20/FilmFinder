const movieRouter = require("express").Router()
const Movie = require("../models/Movie")

//get
movieRouter.get("/movieId/:movieId", (req, res, next) => {
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

//create
movieRouter.post("/", (req, res, next) => {

    newMovie = new Movie({
        movieId: req.body.movieId,
        title: req.body.title,
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

//update
movieRouter.put("/movieId/:movieId", (req, res, next) => {
    id = req.params.movieId
    
    const updatedMovie = {
        movieId: req.body.movieId,
        title: req.body.title,
        genres: req.body.genres
    }  

    Movie.updateOne({movieId: id}, updatedMovie)
        .then((result) => {
            res.json(result)
        })
        .catch((error) => {
            next(error)
        })

})

//delete
movieRouter.delete("/movieId/:movieId", (req, res, next) => {
    id = req.params.movieId
    Movie.deleteOne({movieId: id})
        .then((result) => {
            res.json(result)
        })
        .catch((err) => {
            next(error)
        })
})

//get all
movieRouter.get("/", (req, res) => {
    Movie.find({}).then((users) => {
        res.json(users)
    })
})

module.exports = movieRouter