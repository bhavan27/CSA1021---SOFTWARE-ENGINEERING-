const express = require('express');

const app = express();
app.use(express.json());

let notes = [];

app.get('/notes', (req, res) => {
  res.json(notes);
});

app.post('/notes', (req, res) => {
  const note = req.body.note;

  if (!note) {
    return res.status(400).json({ message: 'Note is required' });
  }

  notes.push(note);
  res.json({
    message: 'Note added successfully',
    notes: notes
  });
});

app.listen(3000, '0.0.0.0', () => {
  console.log('Notes app running on port 3000');
});
