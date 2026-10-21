# field_info_max_weight()

- **Type:** Function
- **File:** [`modules/field/field.info.inc`](_file.md), lines 712–734 · [local source](../../../../source/modules/field/field.info.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc#L712-L734)
- **Module/theme:** field
- **Topics:** [field_info](../../../topics/field_info.md)

## Signature

```php
function field_info_max_weight($entity_type, $bundle, $context)
```

## Documentation

```text
Returns the maximum weight of all the components in an entity.

This includes fields, 'extra_fields', and other components added by
third-party modules (e.g. field_group).

@param $entity_type
  The type of entity; e.g. 'node' or 'user'.
@param $bundle
  The bundle name.
@param $context
  The context for which the maximum weight is requested. Either 'form', or
  the name of a view mode.
@return
  The maximum weight of the entity's components, or NULL if no components
  were found.
```

## Code

```php
function field_info_max_weight($entity_type, $bundle, $context) {
  $weights = array();

  // Collect weights for fields.
  foreach (field_info_instances($entity_type, $bundle) as $instance) {
    if ($context == 'form') {
      $weights[] = $instance['widget']['weight'];
    }
    elseif (isset($instance['display'][$context]['weight'])) {
      $weights[] = $instance['display'][$context]['weight'];
    }
  }
  // Collect weights for extra fields.
  foreach (field_info_extra_fields($entity_type, $bundle, $context) as $extra) {
    $weights[] = $extra['weight'];
  }

  // Let other modules feedback about their own additions.
  $weights = array_merge($weights, module_invoke_all('field_info_max_weight', $entity_type, $bundle, $context));
  $max_weight = $weights ? max($weights) : NULL;

  return $max_weight;
}
```

---
_Drupal 7.103 · [modules/field/field.info.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.info.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
