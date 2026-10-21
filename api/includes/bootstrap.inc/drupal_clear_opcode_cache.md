# drupal_clear_opcode_cache()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3941–3961 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3941-L3961)

## Signature

```php
function drupal_clear_opcode_cache($filepath)
```

## Documentation

```text
Invalidates a PHP file from any active opcode caches.

If the opcode cache does not support the invalidation of individual files,
the entire cache will be flushed.

@param string $filepath
  The absolute path of the PHP file to invalidate.
```

## Code

```php
function drupal_clear_opcode_cache($filepath) {
  if (!defined('PHP_VERSION_ID') || PHP_VERSION_ID < 50300) {
    // Below PHP 5.3, clearstatcache does not accept any function parameters.
    clearstatcache();
  }
  else {
    clearstatcache(TRUE, $filepath);
  }

  // Zend OPcache.
  if (function_exists('opcache_invalidate')) {
    opcache_invalidate($filepath, TRUE);
  }
  // APC.
  if (function_exists('apc_delete_file')) {
    // apc_delete_file() throws a PHP warning in case the specified file was
    // not compiled yet.
    // @see http://php.net/apc-delete-file
    @apc_delete_file($filepath);
  }
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
