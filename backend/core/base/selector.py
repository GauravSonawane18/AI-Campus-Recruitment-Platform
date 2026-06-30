class BaseSelector:
    """
    Base Selector.

    Every selector in the project should inherit from this class.

    Selectors are responsible ONLY for database read operations.
    They must never create, update, or delete records.
    """

    model = None

    @classmethod
    def all(cls):
        return cls.model.objects.all()

    @classmethod
    def filter(cls, **kwargs):
        return cls.model.objects.filter(**kwargs)

    @classmethod
    def get(cls, **kwargs):
        return cls.model.objects.get(**kwargs)

    @classmethod
    def exists(cls, **kwargs):
        return cls.model.objects.filter(**kwargs).exists()

    @classmethod
    def count(cls, **kwargs):
        return cls.model.objects.filter(**kwargs).count()