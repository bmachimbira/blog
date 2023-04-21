<template>
    <div @click="loadArticle()"
        class="flex self-center w-3/5 mt-8 border border-gray-200 rounded-lg shadow dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
        <img class="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-l-lg" :src="imgPath"
            alt="">
        <div class="flex flex-col justify-center p-4 leading-normal">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ post.title }}</h5>
            <div class="mb-3 font-normal text-gray-700 dark:text-gray-400" v-if="post.content.length < 250">{{
                post.content
            }}</div>
            <div class="mb-3 font-normal text-gray-700 dark:text-gray-400" v-else>{{ post.content.substring(0, 250) +
                ".."
            }}
            </div>
            <div class="wrapfooter">
                <span class="author-meta">
                    <span class="post-name">Authored by {{ post.author }} on {{ publishDate }}</span>
                </span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ArticleListItem',
    data() {
        return {
            imgPath: this.post.thumbnail,
            publishDate: this.formatDate(this.post.published_date)
        }
    },
    props: {
        post: {
            type: Object,
            required: true
        }
    },
    methods: {
        loadArticle() {
            this.$router.push({
                name: 'Article',
                params: {
                    id: this.post.id
                }
            })
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            // Then specify how you want your dates to be formatted
            return new Intl.DateTimeFormat('default', { dateStyle: 'long' }).format(date);
        }
    }
}
</script>