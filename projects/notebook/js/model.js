'use strict';

class NotebookModel {
  constructor() {
    this.notes = this.loadNotes();
  }

  loadNotes() {
    const saved = localStorage.getItem('notes');
    return saved ? JSON.parse(saved) : [];
  }

  saveNotes() {
    localStorage.setItem('notes', JSON.stringify(this.notes));
  }

  addNote(title, text, color) {
    const date = new Date();
    const formattedDate = date.toLocaleString('en-US', {
      month: '2-digit',
      day: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: false
    });
    const note = {
      id: Date.now(),
      title,
      text,
      color,
      date: formattedDate
    };
    this.notes.push(note);
    this.saveNotes();
    return note;
  }

  deleteNote(id) {
    this.notes = this.notes.filter(note => note.id !== id);
    this.saveNotes();
  }
}

window.NotebookModel = NotebookModel;
