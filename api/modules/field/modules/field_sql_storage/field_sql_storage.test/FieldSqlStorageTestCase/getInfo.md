# FieldSqlStorageTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.test`](../_file.md), lines 21–27 · [local source](../../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test#L21-L27)
- **Class:** [FieldSqlStorageTestCase](../FieldSqlStorageTestCase.md)
- **Module/theme:** field_sql_storage

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name'  => 'Field SQL storage tests',
      'description'  => "Test field SQL storage module.",
      'group' => 'Field API'
    );
  }
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.test) · Licensed GPL-2.0-or-later (see LICENSE)._
