<template>
    <div v-for="post in posts" :key="post.id">
        <ArticleListItem :post="post" />
    </div>
</template>

<script>
import axios from 'axios'
import ArticleListItem from './ArticleListItem.vue'

export default {
    name: 'ArticleList',
    data() {
        return {
            posts: []
        }
    },
    components: {
        ArticleListItem: ArticleListItem
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/articles')
            .then((response) => {
                this.posts = response.data
            })
    }
}
</script>