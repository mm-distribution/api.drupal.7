# country_get_list()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 2409–2415 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L2409-L2415)

## Signature

```php
function country_get_list()
```

## Documentation

```text
Get list of all predefined and custom countries.

@return
  An array of all country code => country name pairs.
```

## Code

```php
function country_get_list() {
  include_once DRUPAL_ROOT . '/includes/iso.inc';
  $countries = _country_get_predefined_list();
  // Allow other modules to modify the country list.
  drupal_alter('countries', $countries);
  return $countries;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
