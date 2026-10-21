# field_sql_storage_update_7002()

- **Type:** Function
- **File:** [`modules/field/modules/field_sql_storage/field_sql_storage.install`](_file.md), lines 197–211 · [local source](../../../../../../source/modules/field/modules/field_sql_storage/field_sql_storage.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install#L197-L211)
- **Module/theme:** field_sql_storage
- **Topics:** [updates-6.x-to-7.x](../../../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function field_sql_storage_update_7002()
```

## Documentation

```text
Fix primary keys in field revision data tables.
```

## Code

```php
function field_sql_storage_update_7002() {
  $results = db_select('field_config', 'fc', array('fetch' => PDO::FETCH_ASSOC))
    ->fields('fc')
    ->condition('storage_module', 'field_sql_storage')
    ->execute();
  foreach ($results as $field) {
    // Revision tables of deleted fields do not need to be fixed, since no new
    // data is written to them.
    if (!$field['deleted']) {
      $table = "field_revision_{$field['field_name']}";
      db_drop_primary_key($table);
      db_add_primary_key($table, array('entity_type', 'entity_id', 'revision_id', 'deleted', 'delta', 'language'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/field_sql_storage/field_sql_storage.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/field_sql_storage/field_sql_storage.install) · Licensed GPL-2.0-or-later (see LICENSE)._
