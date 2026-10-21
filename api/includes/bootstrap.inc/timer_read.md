# timer_read()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 497–510 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L497-L510)

## Signature

```php
function timer_read($name)
```

## Documentation

```text
Reads the current timer value without stopping the timer.

@param $name
  The name of the timer.

@return
  The current timer value in ms.
```

## Code

```php
function timer_read($name) {
  global $timers;

  if (isset($timers[$name]['start'])) {
    $stop = microtime(TRUE);
    $diff = round(($stop - $timers[$name]['start']) * 1000, 2);

    if (isset($timers[$name]['time'])) {
      $diff += $timers[$name]['time'];
    }
    return $diff;
  }
  return $timers[$name]['time'];
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
