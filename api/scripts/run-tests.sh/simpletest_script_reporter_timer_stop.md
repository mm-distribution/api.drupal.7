# simpletest_script_reporter_timer_stop()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 734–739 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L734-L739)

## Signature

```php
function simpletest_script_reporter_timer_stop()
```

## Documentation

```text
Stop the test timer.
```

## Code

```php
function simpletest_script_reporter_timer_stop() {
  echo "\n";
  $end = timer_stop('run-tests');
  echo "Test run duration: " . format_interval($end['time'] / 1000);
  echo "\n\n";
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
