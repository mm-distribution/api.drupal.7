# _batch_test_callback_2()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.callbacks.inc`](_file.md), lines 29–57 · [local source](../../../../../source/modules/simpletest/tests/batch_test.callbacks.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc#L29-L57)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_callback_2($start, $total, $sleep, &$context)
```

## Documentation

```text
Implements callback_batch_operation().

Multistep batch operation.
```

## Code

```php
function _batch_test_callback_2($start, $total, $sleep, &$context) {
  // Initialize context with progress information.
  if (!isset($context['sandbox']['current'])) {
    $context['sandbox']['current'] = $start;
    $context['sandbox']['count'] = 0;
  }

  // Process by groups of 5 (arbitrary value).
  $limit = 5;
  for ($i = 0; $i < $limit && $context['sandbox']['count'] < $total; $i++) {
    // No-op, but ensure the batch take a couple iterations.
    // Batch needs time to run for the test, so sleep a bit.
    usleep($sleep);
    // Track execution, and store some result for post-processing in the
    // 'finished' callback.
    $id = $context['sandbox']['current'] + $i;
    batch_test_stack("op 2 id $id");
    $context['results'][2][] = $id;

    // Update progress information.
    $context['sandbox']['count']++;
  }
  $context['sandbox']['current'] += $i;

  // Inform batch engine about progress.
  if ($context['sandbox']['count'] != $total) {
    $context['finished'] = $context['sandbox']['count'] / $total;
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.callbacks.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.callbacks.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
