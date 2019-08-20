Vue.component('tabs', {
    data: function () {
        return {
            show: false
        }
    },
    template: `
    <div>
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item">
                <a class="nav-link active" id="asked-tab" data-toggle="tab" href="#asked" role="tab" aria-controls="asked" aria-selected="true">Questions Asked</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="liked-tab" data-toggle="tab" href="#liked" role="tab" aria-controls="liked" aria-selected="false">Liked</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="answered-tab" data-toggle="tab" href="#answered" role="tab" aria-controls="answered" aria-selected="false">Answered</a>
            </li>
        </ul>

        <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="asked" role="tabpanel" aria-labelledby="asked-tab">
                <slot name="asked"></slot>
            </div>
            <div class="tab-pane fade" id="liked" role="tabpanel" aria-labelledby="liked-tab">
                <slot name="liked"></slot>
            </div>
            <div class="tab-pane fade" id="answered" role="tabpanel" aria-labelledby="answered-tab">
                <slot name="answered"></slot>
            </div>
        </div>
    </div>
    `
});

Vue.component('question', {
    data: function () {
        return {
            toggleToLike: (this.liked == 'True'),
            toggleSuccess: false,
            numLikes: parseInt(this.numberlikes)
        }
    },
    props: ['questiontext', 'questionurl', 'moreinfo', 'username', 'userurl', 'numbercomments', 'timestamp', 'numberlikes', 'liked', 'tags'],
    template: `
    <!-- If you liked it, then toggleToLike is false, since when you toggle the like button it will unlike. -->
    <div class="card border-left-primary shadow h-10 py-2 mb-2">
        <div class="card-body">
            <div class="row no-gutters align-items-center">
                <div class="col mr-2">
                    <!-- Question goes here -->
                    <div class="mb-1">
                        <h5>
                            <a :href="questionurl">{{ questiontext }}</a>
                            <br>
                            <span v-for="tag in tags" class="badge badge-light text-lowercase">{{ tag }}</span>
                        </h5>
                    </div>
                    <!-- Username goes here -->
                    <div class="text-xs mb-1">
                        <a :href="userurl" style="color: #808080">{{ username }}</a> on {{ timestamp }}
                    </div>
                    <!-- Details go here -->
                    <div class="mb-1">
                        <p>{{ moreinfo }}</p>
                    </div>
                </div>

                <!-- Number of comments goes here -->
                <div class="col-auto">
                    <b>{{ numbercomments }}</b> <i class="fas fa-comments fa-2x text-gray-300"></i>
                </div>

                <!-- Number of likes goes here -->
                <div class="col-auto">
                    <b>&nbsp;&nbsp;{{ numLikes }}</b> 
                    <span v-if="!toggleToLike">
                        <i class="fas fa-thumbs-up fa-2x text-gray-300" v-on:click="
                            toggleToLike = !toggleToLike;
                            numLikes++;
                            toggleLike(1)
                        "></i>
                    </span>
                    <span v-else>
                        <i class="fas fa-thumbs-up fa-2x text-blue-300" v-on:click="
                            toggleToLike = !toggleToLike;
                            numLikes--;
                            toggleLike(0)
                        " style="color:#4e73df;"></i>
                    </span>
                </div>
            </div>
        </div>
    </div>`,
    methods: {
        toggleLike: function (likeValue) {
            // If 1 then like. If 0 then remove the like. If -1 then give dislike.
            console.log(this.questionurl);
            console.log(likeValue);

            this.$http.post('/testpost', {toggle: likeValue}).then(response => {

                // successfully sent
                console.log('true')
                return true;

            }, response => {
                // error callback
                console.log('false')
                return false;
            });

            // alert(likeValue);
        }
    }
});

new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!'
    }
});