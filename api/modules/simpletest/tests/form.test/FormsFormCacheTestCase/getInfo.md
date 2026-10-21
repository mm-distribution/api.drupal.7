# FormsFormCacheTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1553–1559 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1553-L1559)
- **Class:** [FormsFormCacheTestCase](../FormsFormCacheTestCase.md)
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
      'name' => 'Form caching',
      'description' => 'Tests storage and retrieval of forms from cache.',
      'group' => 'Form API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
