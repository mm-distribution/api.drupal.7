# ThemeRegistry::initializeRegistry()

- **Type:** Method
- **File:** [`includes/theme.inc`](../_file.md), lines 410–414 · [local source](../../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L410-L414)
- **Class:** [ThemeRegistry](../ThemeRegistry.md)

## Signature

```php
function initializeRegistry()
```

## Documentation

```text
Initializes the full theme registry.

@return
  An array with the keys of the full theme registry, but the values
  initialized to NULL.
```

## Code

```php
  function initializeRegistry() {
    $this->completeRegistry = theme_get_registry();

    return array_fill_keys(array_keys($this->completeRegistry), NULL);
  }
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
