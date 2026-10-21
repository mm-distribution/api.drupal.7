# text_field_instance_settings_form()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 87–109 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L87-L109)
- **Module/theme:** text
- **Implements:** [hook_field_instance_settings_form()](../../../../field_ui/field_ui.api.php/hook_field_instance_settings_form.md)

## Signature

```php
function text_field_instance_settings_form($field, $instance)
```

## Documentation

```text
Implements hook_field_instance_settings_form().
```

## Code

```php
function text_field_instance_settings_form($field, $instance) {
  $settings = $instance['settings'];

  $form['text_processing'] = array(
    '#type' => 'radios',
    '#title' => t('Text processing'),
    '#default_value' => $settings['text_processing'],
    '#options' => array(
      t('Plain text'),
      t('Filtered text (user selects text format)'),
    ),
  );
  if ($field['type'] == 'text_with_summary') {
    $form['display_summary'] = array(
      '#type' => 'checkbox',
      '#title' => t('Summary input'),
      '#default_value' => $settings['display_summary'],
      '#description' => t('This allows authors to input an explicit summary, to be displayed instead of the automatically trimmed text when using the "Summary or trimmed" display type.'),
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
