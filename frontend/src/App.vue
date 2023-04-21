<template>
    <Header />

  <body>
    <router-view />
    <Contact v-if="isNotContactList"/>
  </body>
</template>

<script>
import Header from './components/Header.vue'
import Contact from './components/Contact.vue'

export default {
  name: 'App',
  components: {
    Header: Header,
    Contact: Contact,
  },
  computed: {
  isNotContactList() {
     return this.$route.name != 'ContactList'
  }
}
}
</script>

<style scoped>
body {
  font-family: 'Nunito', sans-serif;
  }
</style>
