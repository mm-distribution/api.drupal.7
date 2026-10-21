# _batch_test_theme_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 490–498 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L490-L498)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_theme_callback()
```

## Documentation

```text
Batch callback function for testing the theme used on the progress page.
```

## Code

```php
function _batch_test_theme_callback() {
  // Because drupalGet() steps through the full progressive batch before
  // returning control to the test function, we cannot test that the correct
  // theme is being used on the batch processing page by viewing that page
  // directly. Instead, we save the theme being used in a variable here, so
  // that it can be loaded and inspected in the thread running the test.
  global $theme;
  batch_test_stack($theme);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
