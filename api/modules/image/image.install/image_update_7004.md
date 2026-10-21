# image_update_7004()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 426–456 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L426-L456)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function image_update_7004()
```

## Documentation

```text
Use a large setting (512 and 1024 characters) for the length of the image alt
and title fields.
```

## Code

```php
function image_update_7004() {
  $alt_spec = array(
    'type' => 'varchar',
    'length' => 512,
    'not null' => FALSE,
  );

  $title_spec = array(
    'type' => 'varchar',
    'length' => 1024,
    'not null' => FALSE,
  );

  $fields = _update_7000_field_read_fields(array(
    'module' => 'image',
    'storage_type' => 'field_sql_storage',
  ));

  foreach ($fields as $field_name => $field) {
    $tables = array(
      _field_sql_storage_tablename($field),
      _field_sql_storage_revision_tablename($field),
    );
    $alt_column = $field['field_name'] . '_alt';
    $title_column = $field['field_name'] . '_title';
    foreach ($tables as $table) {
      db_change_field($table, $alt_column, $alt_column, $alt_spec);
      db_change_field($table, $title_column, $title_column, $title_spec);
    }
  }
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
