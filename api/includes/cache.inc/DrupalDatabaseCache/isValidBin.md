# DrupalDatabaseCache::isValidBin()

- **Type:** Method
- **File:** [`includes/cache.inc`](../_file.md), lines 578–589 · [local source](../../../../source/includes/cache.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc#L578-L589)
- **Class:** [DrupalDatabaseCache](../DrupalDatabaseCache.md)

## Signature

```php
function isValidBin()
```

## Documentation

```text
Checks if $this->bin represents a valid cache table.

This check is required to ensure that non-cache tables are not truncated
accidentally when calling cache_clear_all().

@return boolean
```

## Code

```php
  function isValidBin() {
    if ($this->bin == 'cache' || substr($this->bin, 0, 6) == 'cache_') {
      // Skip schema check for bins with standard table names.
      return TRUE;
    }
    // These fields are required for any cache table.
    $fields = array('cid', 'data', 'expire', 'created', 'serialized');
    // Load the table schema.
    $schema = drupal_get_schema($this->bin);
    // Confirm that all fields are present.
    return isset($schema['fields']) && !array_diff($fields, array_keys($schema['fields']));
  }
```

---
_Drupal 7.103 · [includes/cache.inc](https://github.com/drupal/drupal/blob/7.103/includes/cache.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
