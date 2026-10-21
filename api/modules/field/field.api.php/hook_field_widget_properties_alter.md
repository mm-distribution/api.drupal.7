# hook_field_widget_properties_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1012–1019 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1012-L1019)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_widget](../../../topics/field_widget.md)

## Signature

```php
function hook_field_widget_properties_alter(&$widget, $context)
```

## Documentation

```text
Alters the widget properties of a field instance before it gets displayed.

Note that instead of hook_field_widget_properties_alter(), which is called
for all fields on all entity types,
hook_field_widget_properties_ENTITY_TYPE_alter() may be used to alter widget
properties for fields on a specific entity type only.

This hook is called once per field per added or edit entity. If the result
of the hook involves reading from the database, it is highly recommended to
statically cache the information.

@param $widget
  The instance's widget properties.
@param $context
  An associative array containing:
  - entity_type: The entity type; e.g., 'node' or 'user'.
  - entity: The entity object.
  - field: The field that the widget belongs to.
  - instance: The instance of the field.

@see hook_field_widget_properties_ENTITY_TYPE_alter()
```

## Code

```php
function hook_field_widget_properties_alter(&$widget, $context) {
  // Change a widget's type according to the time of day.
  $field = $context['field'];
  if ($context['entity_type'] == 'node' && $field['field_name'] == 'field_foo') {
    $time = date('H');
    $widget['type'] = $time < 12 ? 'widget_am' : 'widget_pm';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_widget_properties_alter()".

- [field_test_field_widget_properties_alter()](../tests/field_test.module/field_test_field_widget_properties_alter.md) — `modules/field/tests/field_test.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
