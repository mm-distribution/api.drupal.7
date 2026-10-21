# text_field_formatter_settings_summary()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 243–254 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L243-L254)
- **Module/theme:** text
- **Implements:** [hook_field_formatter_settings_summary()](../../../../field_ui/field_ui.api.php/hook_field_formatter_settings_summary.md)

## Signature

```php
function text_field_formatter_settings_summary($field, $instance, $view_mode)
```

## Documentation

```text
Implements hook_field_formatter_settings_summary().
```

## Code

```php
function text_field_formatter_settings_summary($field, $instance, $view_mode) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $summary = '';

  if (strpos($display['type'], '_trimmed') !== FALSE) {
    $summary = t('Trimmed limit: @trim_length characters', array('@trim_length' => $settings['trim_length']));
  }

  return $summary;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
