# python_web_blog
This is a simple web-based blog.
Used:  Flask, HTML, CSS, Bootstrap, Jinja2

The blog requires MongoDB to be running without authentication enabled.

The available endpoints are:

    /
    /login
    /register
    /blogs
    /blogs/new
    /posts/<string:blog_id>
    /posts/new/<string:blog_id>
