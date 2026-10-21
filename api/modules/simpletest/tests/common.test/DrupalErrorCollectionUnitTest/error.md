# DrupalErrorCollectionUnitTest::error()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2797–2815 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2797-L2815)
- **Class:** [DrupalErrorCollectionUnitTest](../DrupalErrorCollectionUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function error($message = '', $group = 'Other', array $caller = NULL)
```

## Documentation

```text
Error handler that collects errors in an array.

This test class is trying to verify that simpletest correctly sees errors
and warnings. However, it can't generate errors and warnings that
propagate up to the testing framework itself, or these tests would always
fail. So, this special copy of error() doesn't propagate the errors up
the class hierarchy. It just stuffs them into a protected collectedErrors
array for various assertions to inspect.
```

## Code

```php
  protected function error($message = '', $group = 'Other', array $caller = NULL) {
    // Due to a WTF elsewhere, simpletest treats debug() and verbose()
    // messages as if they were an 'error'. But, we don't want to collect
    // those here. This function just wants to collect the real errors (PHP
    // notices, PHP fatal errors, etc.), and let all the 'errors' from the
    // 'User notice' group bubble up to the parent classes to be handled (and
    // eventually displayed) as normal.
    if ($group == 'User notice') {
      parent::error($message, $group, $caller);
    }
    // Everything else should be collected but not propagated.
    else {
      $this->collectedErrors[] = array(
        'message' => $message,
        'group' => $group,
        'caller' => $caller
      );
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
