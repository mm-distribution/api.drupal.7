# number_field_info()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 24–50 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L24-L50)
- **Module/theme:** number
- **Implements:** [hook_field_info()](../../../field.api.php/hook_field_info.md)

## Signature

```php
function number_field_info()
```

## Documentation

```text
Implements hook_field_info().
```

## Code

```php
function number_field_info() {
  return array(
    'number_integer' => array(
      'label' => t('Integer'),
      'description' => t('This field stores a number in the database as an integer.'),
      'instance_settings' => array('min' => '', 'max' => '', 'prefix' => '', 'suffix' => ''),
      'default_widget' => 'number',
      'default_formatter' => 'number_integer',
    ),
    'number_decimal' => array(
      'label' => t('Decimal'),
      'description' => t('This field stores a number in the database in a fixed decimal format.'),
      'settings' => array('precision' => 10, 'scale' => 2, 'decimal_separator' => '.'),
      'instance_settings' => array('min' => '', 'max' => '', 'prefix' => '', 'suffix' => ''),
      'default_widget' => 'number',
      'default_formatter' => 'number_decimal',
    ),
    'number_float' => array(
      'label' => t('Float'),
      'description' => t('This field stores a number in the database in a floating point format.'),
      'settings' => array('decimal_separator' => '.'),
      'instance_settings' => array('min' => '', 'max' => '', 'prefix' => '', 'suffix' => ''),
      'default_widget' => 'number',
      'default_formatter' => 'number_decimal',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
