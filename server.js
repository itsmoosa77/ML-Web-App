const express = require('express');
const { exec } = require('child_process');
const path = require('path');
const multer = require('multer');
const fs = require('fs');

const app = express();
const port = 3000;

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Configure multer for file uploads
const upload = multer({ dest: 'uploads/' });

// Handle POST request to /apply-model
app.post('/apply-model', upload.single('dataset'), (req, res) => {
  console.log('Received POST request to /apply-model');
  
  if (!req.file) {
    console.log('No file uploaded');
    return res.status(400).send('No file uploaded.');
  }

  const pythonPath = 'C:/Anaconda/envs/ml_project/python.exe'
  const scriptPath = path.join(__dirname, 'scripts', 'ml_script.py');
  const datasetPath = req.file.path;
  const selectedModel = req.body.model;

  console.log(`Executing: "${pythonPath}" "${scriptPath}" "${datasetPath}" "${selectedModel}"`);

  exec(`"${pythonPath}" "${scriptPath}" "${datasetPath}" "${selectedModel}"`, {
    cwd: __dirname
  }, (error, stdout, stderr) => {
    // Clean up the uploaded file
    fs.unlink(datasetPath, (err) => {
      if (err) console.error(`Error deleting file: ${err}`);
    });

    if (error) {
      console.error(`Error: ${error.message}`);
      return res.status(500).send(`Error executing Python script: ${error.message}`);
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return res.status(500).send(`Error in Python script: ${stderr}`);
    }
    console.log(`stdout: ${stdout}`);
    res.send(stdout);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});