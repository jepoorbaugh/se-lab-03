"use strict";

// Ensure topic and author inputs can only contain values within their respective datalists
const topic_input = document.querySelector("#topic-input");
const topic_datalist = document.querySelector("#topic-data-list");
const topic_submit = document.querySelector("#topic-submit");

topic_input.addEventListener("change", () => {
    // Set topic input to lowercase
    topic_input.value = topic_input.value.toLowerCase();

    if (topic_datalist.querySelector(`[value="${topic_input.value}"]`) === null) {
        topic_submit.disabled = true;
    } else {
        topic_submit.disabled = false;
    }
});

const author_input = document.querySelector("#author-input");
const author_datalist = document.querySelector("#author-data-list");
const author_submit = document.querySelector("#author-submit");

author_input.addEventListener("change", () => {
    // Set author input to lowercase
    author_input.value = author_input.value.toLowerCase();

    if (author_datalist.querySelector(`[value="${author_input.value}"]`) === null) {
        author_submit.disabled = true;
    } else {
        author_submit.disabled = false;
    }
});
