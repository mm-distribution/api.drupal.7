# field_test_field_widget_form_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 252–262 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L252-L262)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_form_alter()](../../field.api.php/hook_field_widget_form_alter.md)

## Signature

```php
function field_test_field_widget_form_alter(&$element, &$form_state, $context)
```

## Documentation

```text
Implements hook_field_widget_form_alter().
```

## Code

```php
function field_test_field_widget_form_alter(&$element, &$form_state, $context) {
  switch ($context['field']['field_name']) {
    case 'alter_test_text':
      drupal_set_message('Field size: ' . $context['instance']['widget']['settings']['size']);
      break;

    case 'alter_test_options':
      drupal_set_message('Widget type: ' . $context['instance']['widget']['type']);
      break;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
