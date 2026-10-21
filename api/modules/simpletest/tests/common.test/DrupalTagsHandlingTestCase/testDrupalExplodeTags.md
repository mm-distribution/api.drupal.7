# DrupalTagsHandlingTestCase::testDrupalExplodeTags()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 710–714 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L710-L714)
- **Class:** [DrupalTagsHandlingTestCase](../DrupalTagsHandlingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalExplodeTags()
```

## Documentation

```text
Explode a series of tags.
```

## Code

```php
  function testDrupalExplodeTags() {
    $string = implode(', ', array_keys($this->validTags));
    $tags = drupal_explode_tags($string);
    $this->assertTags($tags);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
