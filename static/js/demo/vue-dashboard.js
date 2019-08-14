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
})

Vue.component('pageselector', {
    data: function () {
        console.log('here!!')
        var currp = parseInt(this.currentpage, 10);
        var maxp = parseInt(this.maxpage, 10);

        var middle = [];
        for (let i = currp - 2; i <= currp + 2; i++) {
            if (i > 0 && i <= maxp){
                middle.push(i);
            };
        };

        console.log(middle)

        return {
            currp: currp,
            maxp: maxp,
            middle: middle
        }
    },
    props: ['currentpage', 'maxpage', 'query'],
    template:`
    <div class="card-transparent mb-4">
        <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">

                <li class="page-item" v-if="currp > 3">
                    <a class="page-link" :href="'dashboard?' + query + '&pagenum=' + '1'">1</a>
                </li>

                <li class="page-item disabled" v-if="(currp - 2) > 2">
                    <a class="page-link" href="#">...</a>
                </li>

                <li class="page-item" v-for="page in middle">
                    <a class="page-link" :href="'dashboard?' + query + '&pagenum=' + page.toString()">{{ page }}</a>
                </li>

                <li class="page-item disabled" v-if="(currp + 2) <= maxp - 2">
                    <a class="page-link" href="#">...</a>
                </li>

                <li class="page-item" v-if="(currp + 2) < maxp">
                    <a class="page-link" :href="'dashboard?' + query + '&pagenum=' + maxpage">{{ maxpage }}</a>
                </li>

            </ul>
        </nav>

    </div>
    `
})



var app1 = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!'
    },
    methods: {
        showMe: function () {
            //event.preventDefault;
            alert(' I am clicked');
        }
    }
})

var pageselectapp = new Vue({
    el: '#pageselectapp'
})