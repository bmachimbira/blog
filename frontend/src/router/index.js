import { createRouter, createWebHistory } from "vue-router"
import Article from "../components/Article.vue"
import Home from "../components/Home.vue"
import Contact from "../components/Contact.vue"
import ContactList from "../components/Contacts.vue"
import PageNotFound from "../components/PageNotFound.vue"

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/article/:id",
        name: "Article",
        component: Article,
    },
    {
        path: '/contact',
        name: "Contact",
        component: Contact,
    },
    {
        path: '/admin/contacts',
        name: "ContactList",
        component: ContactList,
    },
    {
        path: '/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router