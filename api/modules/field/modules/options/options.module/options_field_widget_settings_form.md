# options_field_widget_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 155–166 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L155-L166)
- **Module/theme:** options
- **Implements:** [hook_field_widget_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_widget_settings_form.md)

## Signature

```php
function options_field_widget_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_widget_settings_form().
```

## Code

```php
function options_field_widget_settings_form($field, $instance) {
  $form = array();
  if ($instance['widget']['type'] == 'options_onoff') {
    $form['display_label'] = array(
      '#type' => 'checkbox',
      '#title' => t('Use field label instead of the "On value" as label'),
      '#default_value' => $instance['widget']['settings']['display_label'],
      '#weight' => -1,
    );
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
