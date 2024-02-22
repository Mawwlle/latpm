from io import BytesIO

import pandas as pd
from django.core.files import File
from django.db import models
from django.utils.text import slugify

from file.services import convert_to_dataframe


class DatasetManager(models.Manager):
    def create_new(self, qs, fields=None):
        df = convert_to_dataframe(qs, fields=fields)
        buffer = BytesIO()

        df.to_csv(buffer)

        model_name = slugify(qs.model.__name__)
        filename = "{}.csv".format(model_name)

        obj = self.model(
            name=filename.replace(".csv", ""),
            app=slugify(qs.model._meta.app_label),
            model=qs.model.__name__,
            lables=fields,
            object_count=qs.count(),
        )

        obj.save()
        obj.csvfile.save(filename, File(buffer, name=filename))

        return obj

    def create_with_concat(self, query_sets: list, fields=None):
        dfs = [convert_to_dataframe(qs, fields=fields) for qs in query_sets]

        df = pd.concat(dfs)
        buffer = BytesIO()

        df.to_csv(buffer)

        model_names = slugify(" ".join(qs.model.__name__ for qs in query_sets))
        filename = "{}.csv".format(model_names)

        obj = self.model(
            name=filename.replace(".csv", ""),
            app=slugify(" ".join(qs.model._meta.app_label for qs in query_sets)),
            lables=fields,
            object_count=sum(qs.count() for qs in query_sets),
        )

        obj.save()
        obj.csvfile.save(filename, File(buffer, name=filename))

        return obj


class DatasetModel(models.Model):
    name = models.CharField(max_length=120)
    app = models.CharField(max_length=120, null=True, blank=True)
    model = models.CharField(max_length=120, null=True, blank=True)
    lables = models.TextField(null=True, blank=True)
    object_count = models.IntegerField(default=0)
    csvfile = models.FileField(upload_to="datasets/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = DatasetManager()  # Attach the manager to the model
