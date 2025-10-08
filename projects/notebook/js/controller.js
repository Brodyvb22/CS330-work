'use strict';

class NotebookController {
  constructor(model, view) {
    this.model = model;
    this.view = view;

    this.titleInput = document.getElementById('title');
    this.textInput = document.getElementById('text');
    this.colorSelect = document.getElementById('color');
    this.addButton = document.getElementById('addNote');

    this.titleHelp = document.getElementById('titleHelp');
    this.textHelp = document.getElementById('textHelp');
    this.colorHelp = document.getElementById('colorHelp');

    this.addButton.addEventListener('click', () => this.handleAddNote());
    this.view.notesContainer.addEventListener('click', e => this.handleDelete(e));

    this.view.renderNotes(this.model.notes);
  }

  handleAddNote() {
    const title = this.titleInput.value.trim();
    const text = this.textInput.value.trim();
    const color = this.colorSelect.value;

    let valid = true;

    if (!title) {
      this.titleHelp.style.display = 'block';
      valid = false;
    } else {
      this.titleHelp.style.display = 'none';
    }

    if (!text) {
      this.textHelp.style.display = 'block';
      valid = false;
    } else {
      this.textHelp.style.display = 'none';
    }

    if (!color) {
      this.colorHelp.style.display = 'block';
      valid = false;
    } else {
      this.colorHelp.style.display = 'none';
    }

    if (!valid) return;

    const note = this.model.addNote(title, text, color);
    this.view.renderNotes(this.model.notes);

    this.titleInput.value = '';
    this.textInput.value = '';
    this.colorSelect.selectedIndex = 0;
  }

  handleDelete(e) {
    if (e.target.classList.contains('deleteNote')) {
      const noteElem = e.target.closest('.note');
      const noteId = Number(noteElem.dataset.id);
      this.model.deleteNote(noteId);
      this.view.renderNotes(this.model.notes);
    }
  }
}

const model = new NotebookModel();
const view = new NotebookView();
new NotebookController(model, view);


