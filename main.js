const BASE_URL = "https://brodyvb22.pythonanywhere.com";

//amuse me
document.getElementById("btnAmuse").addEventListener("click", async (e) => {
  e.preventDefault();

  const lang = document.getElementById("selLang").value;
  const cat = document.getElementById("selCat").value;
  const num = document.getElementById("selNum").value;

  const jokesDiv = document.getElementById("jokes");
  const errorDiv = document.getElementById("error");
  jokesDiv.innerHTML = "";
  errorDiv.innerHTML = "";

  const url = `${BASE_URL}/api/v1/jokes/${lang}/${cat}/${num}`;

  try {
    const res = await fetch(url);
    const data = await res.json();

    jokesDiv.innerHTML = "";
    if (data.error) {
      errorDiv.innerText = data.error;
      return;
    }

    if (!data.jokes || data.jokes.length === 0) {
      jokesDiv.innerHTML = "<p>No jokes found.</p>";
      return;
    }

    data.jokes.forEach((joke, i) => {
      const box = document.createElement("div");
      box.className = "box";
      box.textContent = `${i + 1}. ${joke}`;
      jokesDiv.appendChild(box);
    });

  } catch (err) {
    errorDiv.innerText = "Error fetching jokes.";
    console.error(err);
  }
});

//get by id
document.getElementById("getJokesID").addEventListener("click", async () => {

  const id = document.getElementById("jokeID").value.trim();
  const jokesDiv = document.getElementById("jokes");
  const errorDiv = document.getElementById("error");
  jokesDiv.innerHTML = "";
  errorDiv.innerHTML = "";

  if (!id) {
    errorDiv.innerText = "Please enter a joke ID.";
    return;
  }

  const url = `${BASE_URL}/api/v1/jokes/${id}`;

  try {
    const res = await fetch(url);
    const data = await res.json();

    jokesDiv.innerHTML = "";
    if (data.error) {
      errorDiv.innerText = data.error;
      return;
    }


    const jokeText = data.joke;
    if (!jokeText) {
      jokesDiv.innerHTML = "<p>No joke found for that ID.</p>";
      return;
    }

    const box = document.createElement("div");
    box.className = "box";
    box.textContent = `Joke #${id}: ${jokeText}`;
    jokesDiv.appendChild(box);

  } catch (err) {
    errorDiv.innerText = "Error fetching joke by ID.";
    console.error(err);
  }
});
