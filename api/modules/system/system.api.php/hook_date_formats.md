# hook_date_formats()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4215–4233 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4215-L4233)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_date_formats()
```

## Documentation

```text
Define additional date formats.

This hook is used to define the PHP date format strings that can be assigned
to date types in the administrative interface. A module can provide date
format strings for the core-provided date types ('long', 'medium', and
'short'), or for date types defined in hook_date_format_types() by itself
or another module.

Since date formats can be locale-specific, you can specify the locales that
each date format string applies to. There may be more than one locale for a
format. There may also be more than one format for the same locale. For
example d/m/Y and Y/m/d work equally well in some locales. You may wish to
define some additional date formats that aren't specific to any one locale,
for example, "Y m". For these cases, the 'locales' component of the return
value should be omitted.

Providing a date format here does not normally assign the format to be
used with the associated date type -- a user has to choose a format for each
date type in the administrative interface. There is one exception: locale
initialization chooses a locale-specific format for the three core-provided
types (see locale_get_localized_date_format() for details). If your module
needs to ensure that a date type it defines has a format associated with it,
call @code variable_set('date_format_' . $type, $format); @endcode
where $type is the machine-readable name defined in hook_date_format_types(),
and $format is a PHP date format string.

@return
  A list of date formats to offer as choices in the administrative
  interface. Each date format is a keyed array consisting of three elements:
  - 'type': The date type name that this format can be used with, as
    declared in an implementation of hook_date_format_types().
  - 'format': A PHP date format string to use when formatting dates. It
    can contain any of the formatting options described at
    http://php.net/manual/function.date.php
  - 'locales': (optional) An array of 2 and 5 character locale codes,
    defining which locales this format applies to (for example, 'en',
    'en-us', etc.). If your date format is not language-specific, leave this
    array empty.

@see hook_date_format_types()
```

## Code

```php
function hook_date_formats() {
  return array(
    array(
      'type' => 'mymodule_extra_long',
      'format' => 'l jS F Y H:i:s e',
      'locales' => array('en-ie'),
    ),
    array(
      'type' => 'mymodule_extra_long',
      'format' => 'l jS F Y h:i:sa',
      'locales' => array('en', 'en-us'),
    ),
    array(
      'type' => 'short',
      'format' => 'F Y',
      'locales' => array(),
    ),
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_date_formats()".

- [system_date_formats()](../system.module/system_date_formats.md) — `modules/system/system.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
