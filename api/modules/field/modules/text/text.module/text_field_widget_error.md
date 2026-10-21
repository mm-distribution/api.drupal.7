# text_field_widget_error()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 577–589 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L577-L589)
- **Module/theme:** text
- **Implements:** [hook_field_widget_error()](../../../field.api.php/hook_field_widget_error.md)

## Signature

```php
function text_field_widget_error($element, $error, $form, &$form_state)
```

## Documentation

```text
Implements hook_field_widget_error().
```

## Code

```php
function text_field_widget_error($element, $error, $form, &$form_state) {
  switch ($error['error']) {
    case 'text_summary_max_length':
      $error_element = $element[$element['#columns'][1]];
      break;

    default:
      $error_element = $element[$element['#columns'][0]];
      break;
  }

  form_error($error_element, $error['message']);
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
