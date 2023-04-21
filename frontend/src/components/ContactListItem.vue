<template>
    <div 
        class="flex self-center w-4/5 mt-8 border border-gray-200 rounded-lg shadow dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">
        
        <div class="flex flex-col justify-center p-4 leading-normal p-4">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{contact.name }}</h5>
            
            <div class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{  contact.message }}
            </div>
            
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContactListItem',
    props: {
        contact: {
            type: Object,
            required: true
        }
    }
}
</script>
