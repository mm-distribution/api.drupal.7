# hook_field_info_max_weight()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2353–2361 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2353-L2361)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_info](../../../topics/field_info.md)

## Signature

```php
function hook_field_info_max_weight($entity_type, $bundle, $context)
```

## Documentation

```text
Returns the maximum weight for the entity components handled by the module.

Field API takes care of fields and 'extra_fields'. This hook is intended for
third-party modules adding other entity components (e.g. field_group).

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

@ingroup field_info
```

## Code

```php
function hook_field_info_max_weight($entity_type, $bundle, $context) {
  $weights = array();

  foreach (my_module_entity_additions($entity_type, $bundle, $context) as $addition) {
    $weights[] = $addition['weight'];
  }

  return $weights ? max($weights) : NULL;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_info_max_weight()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
