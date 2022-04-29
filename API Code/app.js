const express = require("express")
const app = express()
const cors = require("cors")
const mongoose = require("mongoose")
const config = require("./utils/config")
const middleware = require("./utils/middleware")
const movieRouter = require("./controllers/movie") //need routers for other models

mongoose
  .connect(config.MONGODB_URI)
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((error) => {
    console.log("Error connecting to MongoDB: ", error.message);
  });

app.use(cors())
app.use(express.json())
app.use(middleware.requestLogger)

app.use("/api/movie", movieRouter)

app.use(middleware.unknownEndpoint)
app.use(middleware.errorHandler)

module.exports = app