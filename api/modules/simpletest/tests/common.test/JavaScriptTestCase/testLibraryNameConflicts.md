# JavaScriptTestCase::testLibraryNameConflicts()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1982–1985 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1982-L1985)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testLibraryNameConflicts()
```

## Documentation

```text
Tests that multiple modules can implement the same library.

@see common_test_library()
```

## Code

```php
  function testLibraryNameConflicts() {
    $farbtastic = drupal_get_library('common_test', 'farbtastic');
    $this->assertEqual($farbtastic['title'], 'Custom Farbtastic Library', 'Alternative libraries can be added to the page.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
