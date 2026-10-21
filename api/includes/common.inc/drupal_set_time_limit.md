# drupal_set_time_limit()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2948–2956 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2948-L2956)
- **Topics:** [php_wrappers](../../topics/php_wrappers.md)

## Signature

```php
function drupal_set_time_limit($time_limit)
```

## Documentation

```text
Attempts to set the PHP maximum execution time.

This function is a wrapper around the PHP function set_time_limit().
When called, set_time_limit() restarts the timeout counter from zero.
In other words, if the timeout is the default 30 seconds, and 25 seconds
into script execution a call such as set_time_limit(20) is made, the
script will run for a total of 45 seconds before timing out.

If the current time limit is not unlimited it is possible to decrease the
total time limit if the sum of the new time limit and the current time spent
running the script is inferior to the original time limit. It is inherent to
the way set_time_limit() works, it should rather be called with an
appropriate value every time you need to allocate a certain amount of time
to execute a task than only once at the beginning of the script.

Before calling set_time_limit(), we check if this function is available
because it could be disabled by the server administrator. We also hide all
the errors that could occur when calling set_time_limit(), because it is
not possible to reliably ensure that PHP or a security extension will
not issue a warning/error if they prevent the use of this function.

@param $time_limit
  An integer specifying the new time limit, in seconds. A value of 0
  indicates unlimited execution time.

@ingroup php_wrappers
```

## Code

```php
function drupal_set_time_limit($time_limit) {
  if (function_exists('set_time_limit')) {
    $current = ini_get('max_execution_time');
    // Do not set time limit if it is currently unlimited.
    if ($current != 0) {
      @set_time_limit($time_limit);
    }
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
