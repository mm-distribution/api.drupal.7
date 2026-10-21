# list_field_schema()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.install`](_file.md), lines 11–46 · [local source](../../../../../../source/modules/field/modules/list/list.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install#L11-L46)
- **Module/theme:** list
- **Implements:** [hook_field_schema()](../../../field.api.php/hook_field_schema.md)

## Signature

```php
function list_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function list_field_schema($field) {
  switch ($field['type']) {
    case 'list_text':
      $columns = array(
        'value' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => FALSE,
        ),
      );
      break;
    case 'list_float':
      $columns = array(
        'value' => array(
          'type' => 'float',
          'not null' => FALSE,
        ),
      );
      break;
    case 'list_integer':
    case 'list_boolean':
      $columns = array(
        'value' => array(
          'type' => 'int',
          'not null' => FALSE,
        ),
      );
      break;
  }
  return array(
    'columns' => $columns,
    'indexes' => array(
      'value' => array('value'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install) · Licensed GPL-2.0-or-later (see LICENSE)._
