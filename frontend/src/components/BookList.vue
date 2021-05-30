<template>
    <div class="book-list-container">
        <h3>{{  list_title  }}</h3>
        <div class="book-item"
                v-for="book in books"
                :key="book.title"
                v-bind:books=books
            >
                <p>title: {{  book.title  }}</p>
                <p>author: {{  book.authors  }}</p>
        </div>
    </div>
</template>

<script>
export default {
  name: 'BookList',
  props: {
    books: Object,
    list_title: String
  }
}
</script>

<style>
.book-list-container{
    border: 3px solid #000;
    width: 100%;
}
.book-item{
    border: 3px solid #000;
    text-align: center;
}
</style>
