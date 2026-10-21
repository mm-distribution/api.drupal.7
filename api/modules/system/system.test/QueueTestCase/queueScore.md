# QueueTestCase::queueScore()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2194–2204 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2194-L2204)
- **Class:** [QueueTestCase](../QueueTestCase.md)
- **Module/theme:** system

## Signature

```php
function queueScore($items, $new_items)
```

## Documentation

```text
This function returns the number of equal items in two arrays.
```

## Code

```php
  function queueScore($items, $new_items) {
    $score = 0;
    foreach ($items as $item) {
      foreach ($new_items as $new_item) {
        if ($item === $new_item) {
          $score++;
        }
      }
    }
    return $score;
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
