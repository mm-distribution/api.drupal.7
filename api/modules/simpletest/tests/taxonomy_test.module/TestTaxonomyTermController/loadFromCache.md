# TestTaxonomyTermController::loadFromCache()

- **Type:** Method
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](../_file.md), lines 178–180 · [local source](../../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L178-L180)
- **Class:** [TestTaxonomyTermController](../TestTaxonomyTermController.md)
- **Module/theme:** batch_test

## Signature

```php
public function loadFromCache($ids, $conditions = array())
```

## Documentation

_No docblock in source._

## Code

```php
  public function loadFromCache($ids, $conditions = array()) {
    return parent::cacheGet($ids, $conditions);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
