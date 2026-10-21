# UrlAlterFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 133–139 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L133-L139)
- **Class:** [UrlAlterFunctionalTest](../UrlAlterFunctionalTest.md)
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
      'name' => t('URL altering'),
      'description' => t('Tests hook_url_inbound_alter() and hook_url_outbound_alter().'),
      'group' => t('Path API'),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
