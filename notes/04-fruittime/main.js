<<<<<<< HEAD
function saveReview(){
    let fruitName = document.querySelectory("#fruitName").value;
    let fruitReview = document.querySelector("#fruitReview").value;
    let fruitRating = "";
    if (fruitName == ""){
        return;
    }
    try{
    let fruitRating = document.querySelector("input[name=`rating`]:checked").value
    console.log(fruitName, fruitReview, fruitRating);
    } catch (e) {
        return;
    }
    console.log(fruitRating);
    let newReview = document.createElement("p");
    newReview.classList.add("box");
    newReview.innerHTML = `<strong>${fruitName}</strong><br>${fruitReview}`;
    
    switch(fruitRating){
        case 1:
            newReview.classList.add("has-background-danger");
            break;
        case 2:
            newReview.classList.add("has-background-warning-light");
            break;
        case 3:
            newReview.classList.add("has-background-info");
            break;
        case 4:
            newReview.classList.add("has-background-success");
            break;
    }

    let allReviews = document.querySelector("#reviewsDiv");
    allReviews.appendChild(newReview);
    document.querySelector(newReview).value=""; ///this was the second attempt to clear after submission
    fruitName.innerHTML=""; ///do this with all input areas to clear on submit
=======
function saveReview() {
  let fruitName = document.querySelector("#fruitName").value;
  let fruiReview = document.querySelector("#fruitReview").value;
  let fruitRating = "";
  if (fruitName === "") {
    return;
  }
  try {
    fruitRating = parseInt(
      document.querySelector("input[name='rating']:checked").value
    );
  } catch (e) {
    return;
  }
  let newReview = document.createElement("p");
  newReview.classList.add("box");
  newReview.innerHTML = `<strong>${fruitName}</strong><br>${fruiReview}`;

  switch (fruitRating) {
    case 1:
      newReview.classList.add("has-background-danger");
      break;
    case 2:
      newReview.classList.add("has-background-warning-light");
      break;
    case 3:
      newReview.classList.add("has-background-info");
      break;
    case 4:
      newReview.classList.add("has-background-success");
      break;
  }
  let allReviews = document.querySelector("#reviewsDiv");
  allReviews.appendChild(newReview);
  document.querySelector("#fruitName").value = "";
>>>>>>> bec812f1035e3fd70ddc9fc720e83eb2a8832196
}
