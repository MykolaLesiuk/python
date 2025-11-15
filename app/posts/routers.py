from flask import render_template, request, redirect, url_for, flash
from app import db
from .models import Post
from .forms import PostForm
from . import posts_bp


@posts_bp.route('/post')
def all_posts():
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template('posts/all_posts.html', posts=posts)


@posts_bp.route('/post/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data
        )
        db.session.add(post)
        db.session.commit()
        flash('Post added successfully!', 'success')
        return redirect(url_for('posts.all_posts'))  # ⚠️ змінено на 'posts.all_posts'
    return render_template('posts/add_post.html', form=form)


@posts_bp.route('/post/<int:id>')
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('posts/detail_post.html', post=post)


@posts_bp.route('/post/<int:id>/update', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        flash('Post updated!', 'info')
        return redirect(url_for('posts.post_detail', id=id))  # ⚠️ також оновлено
    return render_template('posts/add_post.html', form=form, post=post)


@posts_bp.route('/post/<int:id>/delete', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', 'warning')
        return redirect(url_for('posts.all_posts'))  # ⚠️ теж оновлено
    return render_template('posts/delete_confirm.html', post=post)