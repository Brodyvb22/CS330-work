'use strict';

class NotebookView {
  constructor() {
    this.notesContainer = document.getElementById('notesContainer');
  }

  renderNotes(notes) {
    this.notesContainer.innerHTML = '';

    const grouped = {};
    notes.forEach(note => {
      if (!grouped[note.color]) grouped[note.color] = [];
      grouped[note.color].push(note);
    });

    for (const color in grouped) {
      const colorSection = document.createElement('div');
        colorSection.classList.add('mb-5');

      const notesList = document.createElement('div');
      grouped[color].forEach(note => {
        const noteElem = this.createNoteElement(note);
        notesList.appendChild(noteElem);
      });

      colorSection.appendChild(notesList);
      this.notesContainer.appendChild(colorSection);
    }
  }

  createNoteElement(note) {
    const noteBox = document.createElement('article');
    noteBox.classList.add('message', note.color, 'note');
    noteBox.dataset.id = note.id;

    const header = document.createElement('div');
    header.classList.add('message-header');
    header.innerHTML = `
      <p>${note.title}</p>
      <button class="delete deleteNote"></button>
    `;

    const body = document.createElement('div');
    body.classList.add('message-body');
    body.innerHTML = `
      <p>${note.text}</p>
      <small><em>${note.date}</em></small>
    `;

    noteBox.appendChild(header);
    noteBox.appendChild(body);
    return noteBox;
  }
}

// Make view accessible globally
window.NotebookView = NotebookView;
