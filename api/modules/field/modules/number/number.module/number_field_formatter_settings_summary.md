# number_field_formatter_settings_summary()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 279–292 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L279-L292)
- **Module/theme:** number
- **Implements:** [hook_field_formatter_settings_summary()](../../../../field_ui/field_ui.api.php/hook_field_formatter_settings_summary.md)

## Signature

```php
function number_field_formatter_settings_summary($field, $instance, $view_mode)
```

## Documentation

```text
Implements hook_field_formatter_settings_summary().
```

## Code

```php
function number_field_formatter_settings_summary($field, $instance, $view_mode) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $summary = array();
  if ($display['type'] == 'number_decimal' || $display['type'] == 'number_integer') {
    $summary[] = number_format(1234.1234567890, $settings['scale'], $settings['decimal_separator'], $settings['thousand_separator']);
    if ($settings['prefix_suffix']) {
      $summary[] = t('Display with prefix and suffix.');
    }
  }

  return implode('<br />', $summary);
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
