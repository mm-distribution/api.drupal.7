# list_field_info()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 24–55 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L24-L55)
- **Module/theme:** list
- **Implements:** [hook_field_info()](../../../field.api.php/hook_field_info.md)

## Signature

```php
function list_field_info()
```

## Documentation

```text
Implements hook_field_info().
```

## Code

```php
function list_field_info() {
  return array(
    'list_integer' => array(
      'label' => t('List (integer)'),
      'description' => t("This field stores integer values from a list of allowed 'value => label' pairs, i.e. 'Lifetime in days': 1 => 1 day, 7 => 1 week, 31 => 1 month."),
      'settings' => array('allowed_values' => array(), 'allowed_values_function' => ''),
      'default_widget' => 'options_select',
      'default_formatter' => 'list_default',
    ),
    'list_float' => array(
      'label' => t('List (float)'),
      'description' => t("This field stores float values from a list of allowed 'value => label' pairs, i.e. 'Fraction': 0 => 0, .25 => 1/4, .75 => 3/4, 1 => 1."),
      'settings' => array('allowed_values' => array(), 'allowed_values_function' => ''),
      'default_widget' => 'options_select',
      'default_formatter' => 'list_default',
    ),
    'list_text' => array(
      'label' => t('List (text)'),
      'description' => t("This field stores text values from a list of allowed 'value => label' pairs, i.e. 'US States': IL => Illinois, IA => Iowa, IN => Indiana."),
      'settings' => array('allowed_values' => array(), 'allowed_values_function' => ''),
      'default_widget' => 'options_select',
      'default_formatter' => 'list_default',
    ),
    'list_boolean' => array(
      'label' => t('Boolean'),
      'description' => t('This field stores simple on/off or yes/no options.'),
      'settings' => array('allowed_values' => array(), 'allowed_values_function' => ''),
      'default_widget' => 'options_buttons',
      'default_formatter' => 'list_default',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
