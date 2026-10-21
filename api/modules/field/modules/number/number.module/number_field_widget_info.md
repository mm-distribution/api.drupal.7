# number_field_widget_info()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 330–337 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L330-L337)
- **Module/theme:** number
- **Implements:** [hook_field_widget_info()](../../../field.api.php/hook_field_widget_info.md)

## Signature

```php
function number_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().
```

## Code

```php
function number_field_widget_info() {
  return array(
    'number' => array(
      'label' => t('Text field'),
      'field types' => array('number_integer', 'number_decimal', 'number_float'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
