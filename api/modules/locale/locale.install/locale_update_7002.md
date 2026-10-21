# locale_update_7002()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 117–126 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L117-L126)
- **Module/theme:** locale
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function locale_update_7002()
```

## Documentation

```text
Updates URL language negotiation by adding the URL fallback detection method.
```

## Code

```php
function locale_update_7002() {
  // language.inc may not have been included during bootstrap if there is not
  // more than one language currently enabled.
  require_once DRUPAL_ROOT . '/includes/language.inc';
  $language_types_info = language_types_info();
  $info = $language_types_info[LANGUAGE_TYPE_URL];
  if (isset($info['fixed'])) {
    language_negotiation_set(LANGUAGE_TYPE_URL, array_flip($info['fixed']));
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
