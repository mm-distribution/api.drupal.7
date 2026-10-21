# number_field_formatter_info()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 191–225 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L191-L225)
- **Module/theme:** number
- **Implements:** [hook_field_formatter_info()](../../../field.api.php/hook_field_formatter_info.md)

## Signature

```php
function number_field_formatter_info()
```

## Documentation

```text
Implements hook_field_formatter_info().
```

## Code

```php
function number_field_formatter_info() {
  return array(
    // The 'Default' formatter is different for integer fields on the one hand,
    // and for decimal and float fields on the other hand, in order to be able
    // to use different default values for the settings.
    'number_integer' => array(
      'label' => t('Default'),
      'field types' => array('number_integer'),
      'settings' =>  array(
        'thousand_separator' => '',
        // The 'decimal_separator' and 'scale' settings are not configurable
        // through the UI, and will therefore keep their default values. They
        // are only present so that the 'number_integer' and 'number_decimal'
        // formatters can use the same code.
        'decimal_separator' => '.',
        'scale' => 0,
        'prefix_suffix' => TRUE,
      ),
    ),
    'number_decimal' => array(
      'label' => t('Default'),
      'field types' => array('number_decimal', 'number_float'),
      'settings' =>  array(
        'thousand_separator' => '',
        'decimal_separator' => '.',
        'scale' => 2,
        'prefix_suffix' => TRUE,
      ),
    ),
    'number_unformatted' => array(
      'label' => t('Unformatted'),
      'field types' => array('number_integer', 'number_decimal', 'number_float'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
