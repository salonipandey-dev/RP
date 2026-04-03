const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();
require('dotenv').config();

console.log("MONGO_URI:", process.env.MONGO_URI);

const app = express();
app.use(express.json());

// Test route
app.get('/health', (req, res) => {
  res.json({ status: "ok" });
});

// MongoDB connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log("DB Error:", err));

// Start server
app.listen(5000, () => {
  console.log("Server running on port 5000");
});