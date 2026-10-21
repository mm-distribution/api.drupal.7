# drupal_multilingual()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3098–3103 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3098-L3103)

## Signature

```php
function drupal_multilingual()
```

## Documentation

```text
Returns TRUE if there is more than one language enabled.

@return
  TRUE if more than one language is enabled.
```

## Code

```php
function drupal_multilingual() {
  // The "language_count" variable stores the number of enabled languages to
  // avoid unnecessarily querying the database when building the list of
  // enabled languages on monolingual sites.
  return variable_get('language_count', 1) > 1;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
