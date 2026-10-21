# DrupalTagsHandlingTestCase::testDrupalImplodeTags()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 719–727 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L719-L727)
- **Class:** [DrupalTagsHandlingTestCase](../DrupalTagsHandlingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalImplodeTags()
```

## Documentation

```text
Implode a series of tags.
```

## Code

```php
  function testDrupalImplodeTags() {
    $tags = array_values($this->validTags);
    // Let's explode and implode to our heart's content.
    for ($i = 0; $i < 10; $i++) {
      $string = drupal_implode_tags($tags);
      $tags = drupal_explode_tags($string);
    }
    $this->assertTags($tags);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
