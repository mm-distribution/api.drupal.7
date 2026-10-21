# text_field_schema()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.install`](_file.md), lines 11–67 · [local source](../../../../../../source/modules/field/modules/text/text.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.install#L11-L67)
- **Module/theme:** text
- **Implements:** [hook_field_schema()](../../../field.api.php/hook_field_schema.md)

## Signature

```php
function text_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function text_field_schema($field) {
  switch ($field['type']) {
    case 'text':
      $columns = array(
        'value' => array(
          'type' => 'varchar',
          'length' => $field['settings']['max_length'],
          'not null' => FALSE,
        ),
      );
      break;

    case 'text_long':
      $columns = array(
        'value' => array(
          'type' => 'text',
          'size' => 'big',
          'not null' => FALSE,
        ),
      );
      break;

    case 'text_with_summary':
      $columns = array(
        'value' => array(
          'type' => 'text',
          'size' => 'big',
          'not null' => FALSE,
        ),
        'summary' => array(
          'type' => 'text',
          'size' => 'big',
          'not null' => FALSE,
        ),
      );
      break;
  }
  $columns += array(
    'format' => array(
      'type' => 'varchar',
      'length' => 255,
      'not null' => FALSE,
    ),
  );
  return array(
    'columns' => $columns,
    'indexes' => array(
      'format' => array('format'),
    ),
    'foreign keys' => array(
      'format' => array(
        'table' => 'filter_format',
        'columns' => array('format' => 'format'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.install) · Licensed GPL-2.0-or-later (see LICENSE)._
