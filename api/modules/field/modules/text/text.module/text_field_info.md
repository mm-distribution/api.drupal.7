# text_field_info()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 32–57 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L32-L57)
- **Module/theme:** text
- **Implements:** [hook_field_info()](../../../field.api.php/hook_field_info.md)

## Signature

```php
function text_field_info()
```

## Documentation

```text
Implements hook_field_info().

Field settings:
  - max_length: the maximum length for a varchar field.
Instance settings:
  - text_processing: whether text input filters should be used.
  - display_summary: whether the summary field should be displayed.
    When empty and not displayed the summary will take its value from the
    trimmed value of the main text field.
```

## Code

```php
function text_field_info() {
  return array(
    'text' => array(
      'label' => t('Text'),
      'description' => t('This field stores varchar text in the database.'),
      'settings' => array('max_length' => 255),
      'instance_settings' => array('text_processing' => 0),
      'default_widget' => 'text_textfield',
      'default_formatter' => 'text_default',
    ),
    'text_long' => array(
      'label' => t('Long text'),
      'description' => t('This field stores long text in the database.'),
      'instance_settings' => array('text_processing' => 0),
      'default_widget' => 'text_textarea',
      'default_formatter' => 'text_default',
    ),
    'text_with_summary' => array(
      'label' => t('Long text and summary'),
      'description' => t('This field stores long text in the database along with optional summary text.'),
      'instance_settings' => array('text_processing' => 1, 'display_summary' => 0),
      'default_widget' => 'text_textarea_with_summary',
      'default_formatter' => 'text_default',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
