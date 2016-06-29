from lattern.models import Post

Post.objects.all()
Post.objects.order_by('-created_at')
