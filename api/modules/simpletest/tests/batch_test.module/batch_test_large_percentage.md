# batch_test_large_percentage()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 322–327 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L322-L327)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_large_percentage()
```

## Documentation

```text
Menu callback: fire a batch process without a form submission.
```

## Code

```php
function batch_test_large_percentage() {
  batch_test_stack(NULL, TRUE);

  batch_set(_batch_test_batch_5());
  batch_process('batch-test/redirect');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
