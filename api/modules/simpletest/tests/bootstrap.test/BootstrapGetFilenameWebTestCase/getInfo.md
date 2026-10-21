# BootstrapGetFilenameWebTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 503–509 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L503-L509)
- **Class:** [BootstrapGetFilenameWebTestCase](../BootstrapGetFilenameWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Get filename test (full installation)',
      'description' => 'Test that drupal_get_filename() works correctly in the context of a full Drupal installation.',
      'group' => 'Bootstrap',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
