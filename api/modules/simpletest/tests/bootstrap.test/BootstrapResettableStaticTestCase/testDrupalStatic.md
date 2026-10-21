# BootstrapResettableStaticTestCase::testDrupalStatic()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 714–733 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L714-L733)
- **Class:** [BootstrapResettableStaticTestCase](../BootstrapResettableStaticTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalStatic()
```

## Documentation

```text
Test that a variable reference returned by drupal_static() gets reset when
drupal_static_reset() is called.
```

## Code

```php
  function testDrupalStatic() {
    $name = __CLASS__ . '_' . __METHOD__;
    $var = &drupal_static($name, 'foo');
    $this->assertEqual($var, 'foo', 'Variable returned by drupal_static() was set to its default.');

    // Call the specific reset and the global reset each twice to ensure that
    // multiple resets can be issued without odd side effects.
    $var = 'bar';
    drupal_static_reset($name);
    $this->assertEqual($var, 'foo', 'Variable was reset after first invocation of name-specific reset.');
    $var = 'bar';
    drupal_static_reset($name);
    $this->assertEqual($var, 'foo', 'Variable was reset after second invocation of name-specific reset.');
    $var = 'bar';
    drupal_static_reset();
    $this->assertEqual($var, 'foo', 'Variable was reset after first invocation of global reset.');
    $var = 'bar';
    drupal_static_reset();
    $this->assertEqual($var, 'foo', 'Variable was reset after second invocation of global reset.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
