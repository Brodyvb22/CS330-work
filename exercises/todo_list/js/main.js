"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

/**
 * Add a new task to the list
 * 
 * Validate form, collect input values, and call `addRow` to add a new row to the table
 */
function addTask() {
    // TODO: Implement this function
    let titleEl = document.querySelector("#title");
    let assignedToEl = document.querySelector("#assignedTo");
    let priorityEl = document.querySelector("#priority");
    let dueDateEl = document.querySelector("#dueDate");

    if (!titleEl.value || !dueDateEl.value || !assignedToEl.value || !priorityEl.value) {
        //alert("All fields are required!");
        return;
    }

    let vals = [
        titleEl.value,
        assignedToEl.value,
        priorityEl.value,
        dueDateEl.value
    ];

    addRow(vals, document.querySelector("#taskList > tbody"));
}


/**
 * Add a new row to the table
 * 
 * Add each value as a separate cell
 * The first cell must be a checkbox to mark a task complete
 * 
 * @param {string[]} valueList list of task attributes
 * @param {Object} parent DOM node to append to
 */

function addRow(valueList, parent) {
    // TODO: Implement this function
    let row = document.createElement("tr");

    let checkboxCell = document.createElement("td");
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("change", removeRow);
    checkboxCell.appendChild(checkbox);
    row.appendChild(checkboxCell);

    valueList.forEach((val) => {
        let cell = document.createElement("td");
        cell.textContent = val;
        row.appendChild(cell);
    });

    switch (valueList[2]) {
        case "Critical":
            row.classList.add("critical");
            break;
        case "Important":
            row.classList.add("important");
            break;
        case "Normal":
            row.classList.add("normal");
            break;
        case "Low":
            row.classList.add("low");
            break;
    }

    parent.appendChild(row);
}


/**
 * Remove a table row corresponding to the selected checkbox after a 2 second timeout
 * 
 */
function removeRow() {
    // TODO: Implement this function
    let row = this.closest("tr"); 

    if (this.checked) {
        setTimeout(() => {
            if (this.checked) { 
                row.remove();
            }
        }, 2000);
    }
}


/**
 * Remove all table rows
 * 
 */
function selectAll() {
    let tbody = document.querySelector("#taskList > tbody");
    tbody.innerHTML = "";
}

/**
 * Add options to the specified element
 * 
 * @param {string} selectId `select` element to populate
 * @param {string[]} sList array of options
 */
function populateSelect(selectId, sList) {
    // TODO: Implement this function
    let select = document.getElementById(selectId);
    select.innerHTML = "";  

    sList.forEach(item => {
        let option = document.createElement("option");
        option.value = item;
        option.textContent = item;
        select.appendChild(option);
    });
}


window.onload = function () {
    // Populate select elements automatically on page load
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
};
