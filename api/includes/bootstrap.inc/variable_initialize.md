# variable_initialize()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 1238–1268 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L1238-L1268)

## Signature

```php
function variable_initialize($conf = array())
```

## Documentation

```text
Loads the persistent variable table.

The variable table is composed of values that have been saved in the table
with variable_set() as well as those explicitly specified in the
configuration file.
```

## Code

```php
function variable_initialize($conf = array()) {
  // NOTE: caching the variables improves performance by 20% when serving
  // cached pages.
  if ($cached = cache_get('variables', 'cache_bootstrap')) {
    $variables = $cached->data;
  }
  else {
    // Cache miss. Avoid a stampede by acquiring a lock. If the lock fails to
    // acquire, optionally just continue with uncached processing.
    $name = 'variable_init';
    $lock_acquired = lock_acquire($name, 1);
    if (!$lock_acquired && variable_get('variable_initialize_wait_for_lock', FALSE)) {
      lock_wait($name);
      return variable_initialize($conf);
    }
    else {
      // Load the variables from the table.
      $variables = array_map('unserialize', db_query('SELECT name, value FROM {variable}')->fetchAllKeyed());
      if ($lock_acquired) {
        cache_set('variables', $variables, 'cache_bootstrap');
        lock_release($name);
      }
    }
  }

  foreach ($conf as $name => $value) {
    $variables[$name] = $value;
  }

  return $variables;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
