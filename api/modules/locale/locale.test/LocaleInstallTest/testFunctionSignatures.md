# LocaleInstallTest::testFunctionSignatures()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1452–1456 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1452-L1456)
- **Class:** [LocaleInstallTest](../LocaleInstallTest.md)
- **Module/theme:** locale

## Signature

```php
function testFunctionSignatures()
```

## Documentation

```text
Verify that function signatures of t() and st() are equal.
```

## Code

```php
  function testFunctionSignatures() {
    $reflector_t = new ReflectionFunction('t');
    $reflector_st = new ReflectionFunction('st');
    $this->assertEqual($reflector_t->getParameters(), $reflector_st->getParameters(), 'Function signatures of t() and st() are equal.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
