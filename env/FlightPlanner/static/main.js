// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

function create_post() {
    console.log("create post is working!") // sanity check
    console.log($('#post-form').val())
};