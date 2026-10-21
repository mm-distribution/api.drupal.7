# timer_stop()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 522–538 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L522-L538)

## Signature

```php
function timer_stop($name)
```

## Documentation

```text
Stops the timer with the specified name.

@param $name
  The name of the timer.

@return
  A timer array. The array contains the number of times the timer has been
  started and stopped (count) and the accumulated timer value in ms (time).
```

## Code

```php
function timer_stop($name) {
  global $timers;

  if (isset($timers[$name]['start'])) {
    $stop = microtime(TRUE);
    $diff = round(($stop - $timers[$name]['start']) * 1000, 2);
    if (isset($timers[$name]['time'])) {
      $timers[$name]['time'] += $diff;
    }
    else {
      $timers[$name]['time'] = $diff;
    }
    unset($timers[$name]['start']);
  }

  return $timers[$name];
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
