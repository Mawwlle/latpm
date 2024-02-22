import pandas as pd

from file.services import csv_file

__all__ = ("csv_file",)


def convert_to_dataframe(qs, fields=None, index=None) -> pd.DataFrame:
    """
    ::param qs is an QuerySet from Django
    ::fields is a list of field names from the Model of the QuerySet
    ::index is the preferred index column we want our dataframe to be set to

    Using the methods from above, we can easily build a dataframe
    from this data.
    """
    lookup_fields = csv_file.get_lookup_fields(qs.model, fields=fields)

    index_col = None
    if index in lookup_fields:
        index_col = index
    elif "id" in lookup_fields:
        index_col = "id"

    values = csv_file.qs_to_dataset(qs, fields=fields)
    df = pd.DataFrame.from_records(values, columns=lookup_fields, index=index_col)

    return df
