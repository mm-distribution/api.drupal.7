# drupal_language_initialize()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3055–3075 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3055-L3075)

## Signature

```php
function drupal_language_initialize()
```

## Documentation

```text
Initializes all the defined language types.
```

## Code

```php
function drupal_language_initialize() {
  $types = language_types();

  // Ensure the language is correctly returned, even without multilanguage
  // support. Also make sure we have a $language fallback, in case a language
  // negotiation callback needs to do a full bootstrap.
  // Useful for eg. XML/HTML 'lang' attributes.
  $default = language_default();
  foreach ($types as $type) {
    $GLOBALS[$type] = $default;
  }
  if (drupal_multilingual()) {
    include_once DRUPAL_ROOT . '/includes/language.inc';
    foreach ($types as $type) {
      $GLOBALS[$type] = language_initialize($type);
    }
    // Allow modules to react on language system initialization in multilingual
    // environments.
    bootstrap_invoke_all('language_init');
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
