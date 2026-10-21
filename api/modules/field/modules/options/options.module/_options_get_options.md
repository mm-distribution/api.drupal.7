# _options_get_options()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 244–261 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L244-L261)
- **Module/theme:** options

## Signature

```php
function _options_get_options($field, $instance, $properties, $entity_type, $entity)
```

## Documentation

```text
Collects the options for a field.
```

## Code

```php
function _options_get_options($field, $instance, $properties, $entity_type, $entity) {
  // Get the list of options.
  $options = (array) module_invoke($field['module'], 'options_list', $field, $instance, $entity_type, $entity);

  // Sanitize the options.
  _options_prepare_options($options, $properties);

  if (!$properties['optgroups']) {
    $options = options_array_flatten($options);
  }

  if ($properties['empty_option']) {
    $label = theme('options_none', array('instance' => $instance, 'option' => $properties['empty_option']));
    $options = array('_none' => $label) + $options;
  }

  return $options;
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
