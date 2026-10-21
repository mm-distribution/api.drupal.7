# number_field_schema()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.install`](_file.md), lines 11–45 · [local source](../../../../../../source/modules/field/modules/number/number.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.install#L11-L45)
- **Module/theme:** number
- **Implements:** [hook_field_schema()](../../../field.api.php/hook_field_schema.md)

## Signature

```php
function number_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function number_field_schema($field) {
  switch ($field['type']) {
    case 'number_integer' :
      $columns = array(
        'value' => array(
          'type' => 'int',
          'not null' => FALSE
        ),
      );
      break;

    case 'number_float' :
      $columns = array(
        'value' => array(
          'type' => 'float',
          'not null' => FALSE
        ),
      );
      break;

    case 'number_decimal' :
      $columns = array(
        'value' => array(
          'type' => 'numeric',
          'precision' => $field['settings']['precision'],
          'scale' => $field['settings']['scale'],
          'not null' => FALSE
        ),
      );
      break;
  }
  return array(
    'columns' => $columns,
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.install) · Licensed GPL-2.0-or-later (see LICENSE)._
