<template>
  <div class="flex items-center mt-52">
    <div class="bg-black shadow-md rounded px-8 pt-6 pb-8 mb-6" style="width: 400px;">
      <div class="identity-input mb-4">
        <label for="identity" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
          Name</label>
        <input id="identity"
          class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          type="text" placeholder="Name" aria-describedby="identityHelp" v-model="name" />
        <span class="text-xs text-red-700" id="identityHelp"></span>
      </div>


      <div class="identity-input mb-4">
        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
          Email</label>
        <input id="email"
          class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          type="text" placeholder="Email" aria-describedby="emailHelp" v-model="email" />
        <span class="text-xs text-red-700" id="emailHelp"></span>
      </div>

      <div class="identity-input mb-4">
        <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
          Phone</label>
        <input id="phone"
          class="{ valid: isValidPhoneNumber, invalid: !isValidPhoneNumber } block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          type="phone" placeholder="Phone" aria-describedby="phoneHelp" v-model="phone" @keyup="validatePhoneNumber" />
        <span class="text-xs text-red-700" id="phoneHelp"></span>
      </div>


      <div class="identity-input mb-4">
        <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your message</label>
        <textarea id="message" rows="4"
          class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Write your thoughts here..." v-model="message"></textarea>

        <span class="text-xs text-red-700" id="messageHelp"></span>
      </div>


      <div class="flex items-center justify-between">
        <button
          class="bg-blue-600 hover:bg-black text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          @click="submit">
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Contact',
  data() {
    return {
      name: "",
      email: "",
      phone: "",
      message: "",
      isValidPhoneNumber: true,
    }
  },
  methods: {
    async submit() {
      await axios.post('http://127.0.0.1:8000/api/contacts', {
        name: this.name,
        email: this.email,
        phone: this.phone,
        message: this.message
      })
        .then((response) => {
          console.log(response)
        })
    },
    validatePhoneNumber() {
      const validationRegex = /^\d{10}$/;
      if (this.phone.match(validationRegex)) {
        this.isValidPhoneNumber = true;
      } else {
        this.isValidPhoneNumber = false;
      }
    },
  },
}
</script>

<style scoped>
.invalid {
  border: 2px solid red;
}
.valid {
  border: 2px solid green;
}
.invalid-warning {
  margin: 10px auto;
  color: red;
}
</style>