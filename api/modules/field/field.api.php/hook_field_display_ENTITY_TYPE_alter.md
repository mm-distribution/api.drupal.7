# hook_field_display_ENTITY_TYPE_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 2427–2432 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L2427-L2432)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_display_ENTITY_TYPE_alter(&$display, $context)
```

## Documentation

```text
Alters the display settings of a field on a given entity type before it gets displayed.

Modules can implement hook_field_display_ENTITY_TYPE_alter() to alter display
settings for fields on a specific entity type, rather than implementing
hook_field_display_alter().

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

@see hook_field_display_alter()
```

## Code

```php
function hook_field_display_ENTITY_TYPE_alter(&$display, $context) {
  // Leave field labels out of the search index.
  if ($context['view_mode'] == 'search_index') {
    $display['label'] = 'hidden';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_display_ENTITY_TYPE_alter()".

- [node_field_display_node_alter()](../../node/node.module/node_field_display_node_alter.md) — `modules/node/node.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
