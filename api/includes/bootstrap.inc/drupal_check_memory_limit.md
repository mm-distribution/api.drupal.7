# drupal_check_memory_limit()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3920–3930 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3920-L3930)

## Signature

```php
function drupal_check_memory_limit($required, $memory_limit = NULL)
```

## Documentation

```text
Compares the memory required for an operation to the available memory.

@param $required
  The memory required for the operation, expressed as a number of bytes with
  optional SI or IEC binary unit prefix (e.g. 2, 3K, 5MB, 10G, 6GiB, 8bytes,
  9mbytes).
@param $memory_limit
  (optional) The memory limit for the operation, expressed as a number of
  bytes with optional SI or IEC binary unit prefix (e.g. 2, 3K, 5MB, 10G,
  6GiB, 8bytes, 9mbytes). If no value is passed, the current PHP
  memory_limit will be used. Defaults to NULL.

@return
  TRUE if there is sufficient memory to allow the operation, or FALSE
  otherwise.
```

## Code

```php
function drupal_check_memory_limit($required, $memory_limit = NULL) {
  if (!isset($memory_limit)) {
    $memory_limit = ini_get('memory_limit');
  }

  // There is sufficient memory if:
  // - No memory limit is set.
  // - The memory limit is set to unlimited (-1).
  // - The memory limit is greater than the memory required for the operation.
  return ((!$memory_limit) || ($memory_limit == -1) || (parse_size($memory_limit) >= parse_size($required)));
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
