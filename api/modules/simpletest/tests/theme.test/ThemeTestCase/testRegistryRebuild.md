# ThemeTestCase::testRegistryRebuild()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 118–126 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L118-L126)
- **Class:** [ThemeTestCase](../ThemeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRegistryRebuild()
```

## Documentation

```text
Ensures the theme registry is rebuilt when modules are disabled/enabled.
```

## Code

```php
  function testRegistryRebuild() {
    $this->assertIdentical(theme('theme_test_foo', array('foo' => 'a')), 'a', 'The theme registry contains theme_test_foo.');

    module_disable(array('theme_test'), FALSE);
    $this->assertIdentical(theme('theme_test_foo', array('foo' => 'b')), '', 'The theme registry does not contain theme_test_foo, because the module is disabled.');

    module_enable(array('theme_test'), FALSE);
    $this->assertIdentical(theme('theme_test_foo', array('foo' => 'c')), 'c', 'The theme registry contains theme_test_foo again after re-enabling the module.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
