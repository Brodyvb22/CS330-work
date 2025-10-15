"use strict";

const btn = document.getElementById("getQuestionsBtn");
btn.addEventListener("click", getQuestions);

async function getQuestions() {
    const categorySelect = document.getElementById("categorySelect");
    const numberInput = document.getElementById("numberInput");
    const warningMsg = document.getElementById("warningMsg");
    const questionsDiv = document.getElementById("questionsDiv");

    warningMsg.textContent = "";
    questionsDiv.innerHTML = "";

    const chosenCategory = categorySelect.value;
    const chosenNumber = parseInt(numberInput.value);

    if (!chosenNumber || chosenNumber < 1 || chosenNumber > 10) {
        warningMsg.textContent = "Please enter a number between 1 and 10.";
        warningMsg.classList.add("is-warning");
        return;
    }

    try {
        const data = await getData(chosenNumber, chosenCategory);

        displayQuestion(questionsDiv, data.results);
    } catch (error) {
        console.error("Error fetching questions:", error);
        warningMsg.textContent = "Failed to fetch trivia questions. Try again.";
        warningMsg.classList.add("is-danger");
    }
}

async function getData(chosenNumber, chosenCategory) {
    const BASE_URL = "https://opentdb.com/api.php?";
    const url = `${BASE_URL}amount=${chosenNumber}&category=${chosenCategory}&type=multiple`;
    const response = await fetch(url);
    return await response.json();
}

function displayQuestion(questionSection, questionPool) {
    questionPool.forEach((questionObj, index) => {
        const card = document.createElement("div");
        card.classList.add("card", "column", "is-half");

        card.classList.add(questionObj.difficulty);

        const cardContent = document.createElement("div");
        cardContent.classList.add("card-content");

        const title = document.createElement("p");
        title.classList.add("title", "is-5");
        title.innerHTML = `${index + 1}. ${questionObj.question}`;
        cardContent.appendChild(title);

        const allAnswers = [...questionObj.incorrect_answers, questionObj.correct_answer];
        shuffleArray(allAnswers);

        const list = document.createElement("ol");
        list.classList.add("content");
        allAnswers.forEach((answer) => {
            const li = document.createElement("li");
            li.innerHTML = answer;
            if (answer === questionObj.correct_answer) {
                li.dataset.correct = "true";
            }
            list.appendChild(li);
        });
        cardContent.appendChild(list);

        const footer = document.createElement("footer");
        footer.classList.add("card-footer");

        const category = document.createElement("p");
        category.classList.add("card-footer-item");
        category.textContent = questionObj.category;

        const difficulty = document.createElement("p");
        difficulty.classList.add("card-footer-item");
        difficulty.textContent = `Difficulty: ${questionObj.difficulty}`;

        const revealBtn = document.createElement("button");
        revealBtn.classList.add("button", "is-link", "is-small", "card-footer-item");
        revealBtn.textContent = "Reveal Answer";
        revealBtn.addEventListener("click", () => revealAnswer(list));

        revealBtn.addEventListener("click", () => {
            list.querySelectorAll("li").forEach((li) => {
                if (li.dataset.correct === "true") {
                    li.classList.add("correct_answer");
                }
            });
        });

        footer.append(category, difficulty, revealBtn);
        card.append(cardContent, footer);

        questionSection.appendChild(card);
    });
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}
