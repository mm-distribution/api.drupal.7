# SystemValidTokenTest::errorHandler()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3125–3130 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3125-L3130)
- **Class:** [SystemValidTokenTest](../SystemValidTokenTest.md)
- **Module/theme:** system

## Signature

```php
public function errorHandler($severity, $message, $file = NULL, $line = NULL)
```

## Documentation

```text
Overrides DrupalTestCase::errorHandler().
```

## Code

```php
  public function errorHandler($severity, $message, $file = NULL, $line = NULL) {
    if ($this->assertErrors) {
      return parent::errorHandler($severity, $message, $file, $line);
    }
    return TRUE;
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
