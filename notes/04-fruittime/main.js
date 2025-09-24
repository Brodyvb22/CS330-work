function saveReview(){
    let fruitName = document.querySelector("#fruitName").value;
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

    let all_reviews = localStorage.getItem("all_reviews");
    if (all_reviews){
      all_reviews = JSON.parse(all_reviews);
    } else {
      all_reviews = [];
    }
    let newReviewItem = {};
    newReviewIem = fruitName;
    newReviewItem.rating = fruitRating;
    newReviewItem.text = fruitReview;
    all_reviews.push(newReviewItem);
    localStorage.setItem("all_reviews", JSON.stringify(all_reviews));

}

function loadReviews(){
  let all_reviews = localStorage.getItem("all_reviews");
  all_reviews = all_reviews ?JSON.parse(all_reviews) : [];

  let allReviewsElement = document.querySelector("#reviewsDiv");
  for (let review of all_reviews){
    
  }
}
