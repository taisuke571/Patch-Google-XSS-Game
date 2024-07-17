var defaultMessage = "Welcome!<br><br>This is your <i>personal</i>"
    + " stream. You can post anything you want here, especially "
    + "<span style='color: #f00ba7'>madness</span>.";
var DB = new PostDB(defaultMessage);

function displayPosts() {
    var containerEl = document.getElementById("post-container");
    while (containerEl.firstChild) {
        containerEl.removeChild(containerEl.firstChild);
    }

    var posts = DB.getPosts();
    for (var i = 0; i < posts.length; i++) {
        var table = document.createElement('table');
        table.className = "message";

        var tr = document.createElement('tr');
        var td1 = document.createElement('td');
        td1.setAttribute('valign', 'top');
        var img = document.createElement('img');
        img.src = "/static/level2_icon.png";
        td1.appendChild(img);

        var td2 = document.createElement('td');
        td2.setAttribute('valign', 'top');
        td2.className = "message-container";

        var div = document.createElement('div');
        div.className = "shim";
        td2.appendChild(div);

        var b = document.createElement('b');
        b.textContent = "You";
        td2.appendChild(b);

        var span = document.createElement('span');
        span.className = "date";
        span.textContent = new Date(posts[i].date);
        td2.appendChild(span);

        var blockquote = document.createElement('blockquote');
        blockquote.innerHTML = posts[i].message;
        td2.appendChild(blockquote);

        tr.appendChild(td1);
        tr.appendChild(td2);
        table.appendChild(tr);
        containerEl.appendChild(table);
    }
}

window.addEventListener('load', function() {
    document.getElementById('clear-form').onsubmit = function() {
        DB.clear(function() { displayPosts(); });
        return false;
    }

    document.getElementById('post-form').onsubmit = function() {
        var message = document.getElementById('post-content').value;
        DB.save(message, function() { displayPosts(); });
        document.getElementById('post-content').value = "";
        return false;
    }

    displayPosts();
});
