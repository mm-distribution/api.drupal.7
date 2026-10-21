# text_field_widget_info()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 460–478 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L460-L478)
- **Module/theme:** text
- **Implements:** [hook_field_widget_info()](../../../field.api.php/hook_field_widget_info.md)

## Signature

```php
function text_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().
```

## Code

```php
function text_field_widget_info() {
  return array(
    'text_textfield' => array(
      'label' => t('Text field'),
      'field types' => array('text'),
      'settings' => array('size' => 60),
    ),
    'text_textarea' => array(
      'label' => t('Text area (multiple rows)'),
      'field types' => array('text_long'),
      'settings' => array('rows' => 5),
    ),
    'text_textarea_with_summary' => array(
      'label' => t('Text area with a summary'),
      'field types' => array('text_with_summary'),
      'settings' => array('rows' => 20, 'summary_rows' => 5),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
