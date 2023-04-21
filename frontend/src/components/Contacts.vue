<template>
    <div v-for="contact in contacts" :key="contact.id">
        <ContactListItem :contact="contact" />
    </div>
</template>

<script>
import axios from 'axios'
import ContactListItem from './ContactListItem.vue'

export default {
    name: 'ContactList',
    data() {
        return {
            contacts: []
        }
    },
    components: {
        ContactListItem: ContactListItem
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/contacts')
            .then((response) => {
                this.contacts = response.data
            })
    }
}
</script>