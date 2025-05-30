<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<script>

// #https://blogs.perl.org/users/ed_j/2017/10/graphql-perl---graphql-js-tutorial-translation-to-graphql-perl-and-mojoliciousplugingraphql.html
// curl -X POST -H "Content-Type: application/json" \
//    -d '{"query": "{ helloWorld }"}' \
//   http://localhost:5000/graphql
console.log(`script test`); 
const grapQLHost = `http://localhost:9000/`;
fetch('http://localhost:9000/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
  body: JSON.stringify({ query: '{ helloWorld }' }),
})
  .then((r) => r.json())
  .then((data) => console.log('data returned:', data));
  
  </script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      You’ve successfully created a project with
      <a href="https://vite.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>.
    </h3>

  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
