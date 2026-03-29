const foldButtons = document.getElementsByClassName("fold-button");

for (let i = 0; i < foldButtons.length; i++) {
    foldButtons[i].addEventListener("click", function (event) {
        const button = event.target;
        const post = button.parentElement;

        const author = post.getElementsByClassName("article-author")[0];
        const createdDate = post.getElementsByClassName("article-created-date")[0];
        const articleText = post.getElementsByClassName("article-text")[0];

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