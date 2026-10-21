# timer_start()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 481–486 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L481-L486)

## Signature

```php
function timer_start($name)
```

## Documentation

```text
Starts the timer with the specified name.

If you start and stop the same timer multiple times, the measured intervals
will be accumulated.

@param $name
  The name of the timer.
```

## Code

```php
function timer_start($name) {
  global $timers;

  $timers[$name]['start'] = microtime(TRUE);
  $timers[$name]['count'] = isset($timers[$name]['count']) ? ++$timers[$name]['count'] : 1;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
