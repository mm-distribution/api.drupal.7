# MenuRouterTestCase::testFileInheritance()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 186–189 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L186-L189)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFileInheritance()
```

## Documentation

```text
Test that 'page callback', 'file' and 'file path' keys are properly
inherited from parent menu paths.
```

## Code

```php
  function testFileInheritance() {
    $this->drupalGet('admin/config/development/file-inheritance');
    $this->assertText('File inheritance test description', 'File inheritance works.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
