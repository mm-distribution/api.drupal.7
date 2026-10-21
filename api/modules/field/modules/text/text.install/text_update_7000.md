# text_update_7000()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.install`](_file.md), lines 72–95 · [local source](../../../../../../source/modules/field/modules/text/text.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.install#L72-L95)
- **Module/theme:** text

## Signature

```php
function text_update_7000()
```

## Documentation

```text
Change text field 'format' columns into varchar.
```

## Code

```php
function text_update_7000() {
  $spec = array(
    'type' => 'varchar',
    'length' => 255,
    'not null' => FALSE,
  );
  $fields = _update_7000_field_read_fields(array(
    'module' => 'text',
    'storage_type' => 'field_sql_storage',
  ));
  foreach ($fields as $field) {
    if ($field['deleted']) {
      $table = "field_deleted_data_{$field['id']}";
      $revision_table = "field_deleted_revision_{$field['id']}";
    }
    else {
      $table = "field_data_{$field['field_name']}";
      $revision_table = "field_revision_{$field['field_name']}";
    }
    $column = $field['field_name'] . '_' . 'format';
    db_change_field($table, $column, $column, $spec);
    db_change_field($revision_table, $column, $column, $spec);
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.install) · Licensed GPL-2.0-or-later (see LICENSE)._
