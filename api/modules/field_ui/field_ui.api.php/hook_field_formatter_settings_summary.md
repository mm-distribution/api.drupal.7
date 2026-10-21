# hook_field_formatter_settings_summary()

- **Type:** Hook (documentation function)
- **File:** [`modules/field_ui/field_ui.api.php`](_file.md), lines 192–203 · [local source](../../../../source/modules/field_ui/field_ui.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php#L192-L203)
- **Module/theme:** field_ui
- **Topics:** [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_formatter_settings_summary($field, $instance, $view_mode)
```

## Documentation

```text
Return a short summary for the current formatter settings of an instance.

If an empty result is returned, the formatter is assumed to have no
configurable settings, and no UI will be provided to display a settings
form.

@param $field
  The field structure.
@param $instance
  The instance structure.
@param $view_mode
  The view mode for which a settings summary is requested.

@return
  A string containing a short summary of the formatter settings.
```

## Code

```php
function hook_field_formatter_settings_summary($field, $instance, $view_mode) {
  $display = $instance['display'][$view_mode];
  $settings = $display['settings'];

  $summary = '';

  if ($display['type'] == 'text_trimmed' || $display['type'] == 'text_summary_or_trimmed') {
    $summary = t('Length: @chars chars', array('@chars' => $settings['trim_length']));
  }

  return $summary;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_formatter_settings_summary()".

- [field_test_field_formatter_settings_summary()](../../field/tests/field_test.field.inc/field_test_field_formatter_settings_summary.md) — `modules/field/tests/field_test.field.inc`
- [image_field_formatter_settings_summary()](../../image/image.field.inc/image_field_formatter_settings_summary.md) — `modules/image/image.field.inc`
- [number_field_formatter_settings_summary()](../../field/modules/number/number.module/number_field_formatter_settings_summary.md) — `modules/field/modules/number/number.module`
- [text_field_formatter_settings_summary()](../../field/modules/text/text.module/text_field_formatter_settings_summary.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field_ui/field_ui.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
