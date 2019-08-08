Vue.component('answer', {
    data: function () {
        return {
            show: false
        }
    },
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

                        <hr>

                        <div class="mb-0" style="font-size:small">
                            Hello my guy
                        </div>
                        <div class="text-xs mb-1" style="text-align:right">
                            <a :href="userurl" style="color: #808080">{{ username }}</a>
                        </div>
                        
                        <div class="mb-0" style="font-size:small">
                            Hello my guy
                        </div>
                        <div class="text-xs mb-1" style="text-align:right">
                            <a :href="userurl" style="color: #808080">{{ username }}</a>
                        </div>

                        <hr>

                        <a href="javascript:void(0)" v-on:click="show=true" v-if="!show" style="font-size:x-small">Add a comment</a>

                        <form v-if="show" action="/action_page.php">
                            <div class="form-group" style="overflow:auto">
                                <textarea type="text" class="form-control" id="comment" style="margin-top: 0px; margin-bottom: 0px; height: 189px;"></textarea>
                            </div>
                            <button type="submit" class="btn btn-success">Submit</button>
                        </form>
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