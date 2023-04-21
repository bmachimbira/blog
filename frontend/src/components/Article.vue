<template>
    <div class="blogDetail">
        <img :src="this.post.thumbnail" alt="">
        <div style="font-size: 28px;">{{ post.title}}</div>
        <h4><span>Authored by {{ post.author }}</span></h4>
        <div class="blogDetail__body">
        {{ post.content }}
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Article',
    data() {
        return {
            post: {},
        }
    },
    mounted() {
        var id = this.$route.params.id
        axios.get('http://127.0.0.1:8000/api/articles/' + id)
            .then((response) => {
                this.post = response.data
            })
    }
}
</script>

<style scoped>
.blogDetail {
    width: 55%;
    max-width: 900px;
    margin: 50px auto;
}

.blogDetail__head span:nth-child(2):after {
    content: '.';
    margin-left: 5px;
    vertical-align: top;
}

.blogDetail__head span {
    margin-left: 5px;
    color: rgb(128, 128, 128);
}

.blogDetail {
    margin-bottom: 15px;
}

.blogDetail>img {
    margin: 15px 0;
}

.blogDetail img {
    width: 30%;
}

.blogDetail .blogDetail__profileImg {
    width: 30px;
    height: 30px;
    border-radius: 100%;
    vertical-align: middle;
}

.blogDetail__body p {
    color: rgb(62, 60, 60);
    font-size: 18px;
}

.blogDetail__body {
    margin: 20px 0 5px;
}

.blogDetail__body img,
video {
    margin: 5px 0;
}
</style>
  