# locale_update_7003()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 140–143 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L140-L143)
- **Module/theme:** locale
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function locale_update_7003()
```

## Documentation

```text
Update "language_count" variable.
```

## Code

```php
function locale_update_7003() {
  $languages = language_list('enabled');
  variable_set('language_count', count($languages[1]));
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
