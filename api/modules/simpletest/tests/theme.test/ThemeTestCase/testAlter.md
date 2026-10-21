# ThemeTestCase::testAlter()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 87–90 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L87-L90)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAlter()
```

## Documentation

```text
Ensures theme hook_*_alter() implementations can run before anything is rendered.
```

## Code

```php
  function testAlter() {
    $this->drupalGet('theme-test/alter');
    $this->assertText('The altered data is test_theme_theme_test_alter_alter was invoked.', 'The theme was able to implement an alter hook during page building before anything was rendered.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
