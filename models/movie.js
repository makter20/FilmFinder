const mongoose = require("mongoose")

const movieSchema = new mongoose.Schema({
    movieId: Number,
    title: String,
    date: Date,
    genres: [String]
})

module.exports = mongoose.model("Movie", movieSchema)