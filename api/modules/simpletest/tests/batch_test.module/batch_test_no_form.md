# batch_test_no_form()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 312–317 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L312-L317)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_no_form()
```

## Documentation

```text
Menu callback: fire a batch process without a form submission.
```

## Code

```php
function batch_test_no_form() {
  batch_test_stack(NULL, TRUE);

  batch_set(_batch_test_batch_1());
  batch_process('batch-test/redirect');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
