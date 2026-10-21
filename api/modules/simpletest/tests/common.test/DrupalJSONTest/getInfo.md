# DrupalJSONTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3090–3096 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3090-L3096)
- **Class:** [DrupalJSONTest](../DrupalJSONTest.md)
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
      'name' => 'JSON',
      'description' => 'Perform unit tests on the drupal_json_encode() and drupal_json_decode() functions.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
