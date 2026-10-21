# hook_countries_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4727–4730 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4727-L4730)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_countries_alter(&$countries)
```

## Documentation

```text
Alter the default country list.

@param $countries
  The associative array of countries keyed by ISO 3166-1 country code.

@see country_get_list()
@see _country_get_predefined_list()
```

## Code

```php
function hook_countries_alter(&$countries) {
  // Elbonia is now independent, so add it to the country list.
  $countries['EB'] = 'Elbonia';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_countries_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
