# FormsFormStoragePageCacheTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1455–1461 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1455-L1461)
- **Class:** [FormsFormStoragePageCacheTestCase](../FormsFormStoragePageCacheTestCase.md)
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
      'name'  => 'Forms using form storage on cached pages',
      'description'  => 'Tests a form using form storage and makes sure validation and caching works when page caching for anonymous users is turned on.',
      'group' => 'Form API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
