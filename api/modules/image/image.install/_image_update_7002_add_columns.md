# _image_update_7002_add_columns()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 288–299 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L288-L299)
- **Module/theme:** image
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function _image_update_7002_add_columns($table, $field_name)
```

## Documentation

```text
Add width and height columns to a specific table.

@param $table
  The name of the database table to be updated.
@param $columns
  Keyed array of columns this table is supposed to have.
```

## Code

```php
function _image_update_7002_add_columns($table, $field_name) {
  $spec = array(
    'type' => 'int',
    'unsigned' => TRUE,
  );

  $spec['description'] = 'The width of the image in pixels.';
  db_add_field($table, $field_name . '_width', $spec);

  $spec['description'] = 'The height of the image in pixels.';
  db_add_field($table, $field_name . '_height', $spec);
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
