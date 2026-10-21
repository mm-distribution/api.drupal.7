# hook_field_extra_fields_display_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2456–2460 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2456-L2460)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_extra_fields_display_alter(&$displays, $context)
```

## Documentation

```text
Alters the display settings of pseudo-fields before an entity is displayed.

This hook is called once per displayed entity. If the result of the hook
involves reading from the database, it is highly recommended to statically
cache the information.

@param $displays
  An array of display settings for the pseudo-fields in the entity, keyed
  by pseudo-field names.
@param $context
  An associative array containing:
  - entity_type: The entity type; e.g., 'node' or 'user'.
  - bundle: The bundle name.
  - view_mode: The view mode, e.g. 'full', 'teaser'...

@ingroup field_types
```

## Code

```php
function hook_field_extra_fields_display_alter(&$displays, $context) {
  if ($context['entity_type'] == 'taxonomy_term' && $context['view_mode'] == 'full') {
    $displays['description']['visible'] = FALSE;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_extra_fields_display_alter()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
