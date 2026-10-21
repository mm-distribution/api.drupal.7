# PSR0WebTest::testArithmetics()

- **Type:** Method
- **File:** [`modules/simpletest/lib/Drupal/simpletest/Tests/PSR0WebTest.php`](../_file.md), lines 15–17 · [local source](../../../../../../../../../source/modules/simpletest/lib/Drupal/simpletest/Tests/PSR0WebTest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/lib/Drupal/simpletest/Tests/PSR0WebTest.php#L15-L17)
- **Class:** [PSR0WebTest](../PSR0WebTest.md)
- **Module/theme:** simpletest

## Signature

```php
function testArithmetics()
```

## Documentation

_No docblock in source._

## Code

```php
  function testArithmetics() {
    $this->assert(1 + 1 == 2, '1 + 1 == 2');
  }
```

---
_Drupal 7.103 · [modules/simpletest/lib/Drupal/simpletest/Tests/PSR0WebTest.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/lib/Drupal/simpletest/Tests/PSR0WebTest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
