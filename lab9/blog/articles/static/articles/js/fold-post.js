const foldButtons = document.getElementsByClassName("fold-button");

for (let i = 0; i < foldButtons.length; i++) {
    foldButtons[i].addEventListener("click", function (event) {
        const button = event.target;
        const post = button.closest(".one-post");

        const author = post.querySelector(".article-author");
        const createdDate = post.querySelector(".article-created-date");
        const articleText = post.querySelector(".article-text");

        const isFolded = button.classList.contains("folded");
        const displayState = isFolded ? "block" : "none";

        if (isFolded) {
            button.textContent = "свернуть";
            button.classList.remove("folded");
        } else {
            button.textContent = "развернуть";
            button.classList.add("folded");
        }

        author.style.display = displayState;
        createdDate.style.display = displayState;
        articleText.style.display = displayState;
    });
}