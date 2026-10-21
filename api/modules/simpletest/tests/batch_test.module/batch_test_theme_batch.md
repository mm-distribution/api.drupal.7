# batch_test_theme_batch()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 476–485 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L476-L485)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_theme_batch()
```

## Documentation

```text
Menu callback: run a batch for testing theme used on the progress page.
```

## Code

```php
function batch_test_theme_batch() {
  batch_test_stack(NULL, TRUE);
  $batch = array(
    'operations' => array(
      array('_batch_test_theme_callback', array()),
    ),
  );
  batch_set($batch);
  batch_process('batch-test/redirect');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
