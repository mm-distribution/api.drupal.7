# field_test_field_widget_properties_alter()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 232–237 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L232-L237)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_field_widget_properties_alter()](../../field.api.php/hook_field_widget_properties_alter.md)

## Signature

```php
function field_test_field_widget_properties_alter(&$widget, $context)
```

## Documentation

```text
Implements hook_field_widget_properties_alter().
```

## Code

```php
function field_test_field_widget_properties_alter(&$widget, $context) {
  // Make the alter_test_text field 42 characters for nodes and comments.
  if (in_array($context['entity_type'], array('node', 'comment')) && ($context['field']['field_name'] == 'alter_test_text')) {
    $widget['settings']['size'] = 42;
  }
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
