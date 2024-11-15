from forum.models import Topic


class TopicRepository:
    model = Topic

    def create_topic(self, title, content, author):
        topic = Topic(
            title=title,
            content=content,
            author=author
        )
        topic.save()

    def delete_topic_by_id(self, id):
        try:
            self.model.objects.get(id=id).delete()
        except Topic.DoesNotExist:
            pass
