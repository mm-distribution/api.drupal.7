# FieldAttachStorageTestCase

- **Type:** Class
- **File:** [`modules/field/tests/field.test`](_file.md), lines 145–711 · [local source](../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L145-L711)
- **Module/theme:** field_test_schema_alter

## Signature

```php
class FieldAttachStorageTestCase extends FieldAttachTestCase
```

## Documentation

```text
Unit test class for storage-related field_attach_* functions.

All field_attach_* test work with all field_storage plugins and
all hook_field_attach_pre_{load,insert,update}() hooks.
```

## Methods (derived index)

- [getInfo()](FieldAttachStorageTestCase/getInfo.md)
- [testFieldAttachSaveLoad()](FieldAttachStorageTestCase/testFieldAttachSaveLoad.md) — Check field values insert, update and load.
- [testFieldAttachLoadMultiple()](FieldAttachStorageTestCase/testFieldAttachLoadMultiple.md) — Test the 'multiple' load feature.
- [testFieldAttachSaveLoadDifferentStorage()](FieldAttachStorageTestCase/testFieldAttachSaveLoadDifferentStorage.md) — Test saving and loading fields using different storage backends.
- [testFieldStorageDetailsAlter()](FieldAttachStorageTestCase/testFieldStorageDetailsAlter.md) — Test storage details alteration.
- [testFieldAttachSaveMissingData()](FieldAttachStorageTestCase/testFieldAttachSaveMissingData.md) — Tests insert and update with missing or NULL fields.
- [testFieldAttachSaveMissingDataDefaultValue()](FieldAttachStorageTestCase/testFieldAttachSaveMissingDataDefaultValue.md) — Test insert with missing or NULL fields, with default value.
- [testFieldHasData()](FieldAttachStorageTestCase/testFieldHasData.md) — Test field_has_data().
- [testFieldAttachDelete()](FieldAttachStorageTestCase/testFieldAttachDelete.md) — Test field_attach_delete().
- [testFieldAttachCreateRenameBundle()](FieldAttachStorageTestCase/testFieldAttachCreateRenameBundle.md) — Test field_attach_create_bundle() and field_attach_rename_bundle().
- [testFieldAttachDeleteBundle()](FieldAttachStorageTestCase/testFieldAttachDeleteBundle.md) — Test field_attach_delete_bundle().

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
