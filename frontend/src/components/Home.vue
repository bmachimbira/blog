<template>
    <main>
        <ArticleList />
    </main>
</template>
<script>
import ArticleList from  './ArticleList.vue'

export default {
    name: 'Home',
    components: {
        ArticleList: ArticleList,
    }
}
</script>
