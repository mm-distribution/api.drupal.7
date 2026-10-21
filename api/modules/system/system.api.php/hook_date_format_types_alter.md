# hook_date_format_types_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4167–4171 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4167-L4171)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_date_format_types_alter(&$types)
```

## Documentation

```text
Modify existing date types.

Allows other modules to modify existing date types like 'long'. Called by
_system_date_format_types_build(). For instance, A module may use this hook
to apply settings across all date types, such as locking all date types so
they appear to be provided by the system.

@param $types
  A list of date types. Each date type is keyed by the machine-readable name
  and the values are associative arrays containing:
  - is_new: Set to FALSE to override previous settings.
  - module: The name of the module that created the date type.
  - type: The machine-readable date type name.
  - title: The human-readable date type name.
  - locked: Specifies that the date type is system-provided.
```

## Code

```php
function hook_date_format_types_alter(&$types) {
  foreach ($types as $name => $type) {
    $types[$name]['locked'] = 1;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_date_format_types_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
