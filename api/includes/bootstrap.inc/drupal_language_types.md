# drupal_language_types()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3084–3090 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3084-L3090)

## Signature

```php
function drupal_language_types()
```

## Documentation

```text
Returns a list of the built-in language types.

@return
  An array of key-values pairs where the key is the language type and the
  value is its configurability.
```

## Code

```php
function drupal_language_types() {
  return array(
    LANGUAGE_TYPE_INTERFACE => TRUE,
    LANGUAGE_TYPE_CONTENT => FALSE,
    LANGUAGE_TYPE_URL => FALSE,
  );
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
