# hook_field_attach_preprocess_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1455–1457 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1455-L1457)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_attach](../../../topics/field_attach.md)

## Signature

```php
function hook_field_attach_preprocess_alter(&$variables, $context)
```

## Documentation

```text
Alter field_attach_preprocess() variables.

This hook is invoked while preprocessing the field.tpl.php template file
in field_attach_preprocess().

@param $variables
  The variables array is passed by reference and will be populated with field
  values.
@param $context
  An associative array containing:
  - entity_type: The type of $entity; for example, 'node' or 'user'.
  - entity: The entity with fields to render.
  - element: The structured array containing the values ready for rendering.
```

## Code

```php
function hook_field_attach_preprocess_alter(&$variables, $context) {
  // @todo Needs function body.
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_attach_preprocess_alter()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
