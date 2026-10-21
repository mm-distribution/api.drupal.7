# hook_date_format_types()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4141–4148 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4141-L4148)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_date_format_types()
```

## Documentation

```text
Define additional date types.

Next to the 'long', 'medium' and 'short' date types defined in core, any
module can define additional types that can be used when displaying dates,
by implementing this hook. A date type is basically just a name for a date
format.

Date types are used in the administration interface: a user can assign
date format types defined in hook_date_formats() to date types defined in
this hook. Once a format has been assigned by a user, the machine name of a
type can be used in the format_date() function to format a date using the
chosen formatting.

To define a date type in a module and make sure a format has been assigned to
it, without requiring a user to visit the administrative interface, use
@code variable_set('date_format_' . $type, $format); @endcode
where $type is the machine-readable name defined here, and $format is a PHP
date format string.

To avoid namespace collisions with date types defined by other modules, it is
recommended that each date type starts with the module name. A date type
can consist of letters, numbers and underscores.

@return
  An array of date types where the keys are the machine-readable names and
  the values are the human-readable labels.

@see hook_date_formats()
@see format_date()
```

## Code

```php
function hook_date_format_types() {
  // Define the core date format types.
  return array(
    'long' => t('Long'),
    'medium' => t('Medium'),
    'short' => t('Short'),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_date_format_types()".

- [system_date_format_types()](../system.module/system_date_format_types.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
