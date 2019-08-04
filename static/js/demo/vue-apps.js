Vue.component('answer', {
    props: ['answertext', 'username', 'userurl'],
    template: `
        <div class="card rounded-0 h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <!-- Answer goes here -->
                        <div class="mb-0">
                            <p>{{ answertext }}</p>
                        </div>
                        <!-- Username goes here -->
                        <div class="text-xs mb-1">
                            <a :href="userurl" style="color: #808080">{{ username }}</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>`
})

new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!'
    }
})