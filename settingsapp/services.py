from models import Setting


def upsert(key, value):
    # This function inserts or updates a settings record in the settings table,
    # based on the input data provided. It ensures that the settings data is
    # always up-to-date and accurate, without the need for manual intervention.

    # get first entry
    entry = Setting.objects.filter(key=key).first()

    if not entry:
        entry.value = value

    entry.save()

    return entry
