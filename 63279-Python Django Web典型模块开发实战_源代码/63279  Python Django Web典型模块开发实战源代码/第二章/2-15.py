class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields="__all__"#将整个表的所有字段都序列化
        fields = ('title', 'isbn', 'author')  # 指定序列化某些字段
