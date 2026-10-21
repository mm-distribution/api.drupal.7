# hook_field_display_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2392–2401 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2392-L2401)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_display_alter(&$display, $context)
```

## Documentation

```text
Alters the display settings of a field before it gets displayed.

Note that instead of hook_field_display_alter(), which is called for all
fields on all entity types, hook_field_display_ENTITY_TYPE_alter() may be
used to alter display settings for fields on a specific entity type only.

This hook is called once per field per displayed entity. If the result of the
hook involves reading from the database, it is highly recommended to
statically cache the information.

@param $display
  The display settings that will be used to display the field values, as
  found in the 'display' key of $instance definitions.
@param $context
  An associative array containing:
  - entity_type: The entity type; e.g., 'node' or 'user'.
  - field: The field being rendered.
  - instance: The instance being rendered.
  - entity: The entity being rendered.
  - view_mode: The view mode, e.g. 'full', 'teaser'...

@see hook_field_display_ENTITY_TYPE_alter()
```

## Code

```php
function hook_field_display_alter(&$display, $context) {
  // Leave field labels out of the search index.
  // Note: The check against $context['entity_type'] == 'node' could be avoided
  // by using hook_field_display_node_alter() instead of
  // hook_field_display_alter(), resulting in less function calls when
  // rendering non-node entities.
  if ($context['entity_type'] == 'node' && $context['view_mode'] == 'search_index') {
    $display['label'] = 'hidden';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_display_alter()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
