# BootstrapMiscTestCase::testMisc()

- **Type:** Method
- **File:** [`modules/simpletest/tests/bootstrap.test`](../_file.md), lines 752–758 · [local source](../../../../../../source/modules/simpletest/tests/bootstrap.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test#L752-L758)
- **Class:** [BootstrapMiscTestCase](../BootstrapMiscTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMisc()
```

## Documentation

```text
Test miscellaneous functions in bootstrap.inc.
```

## Code

```php
  function testMisc() {
    // Test drupal_array_merge_deep().
    $link_options_1 = array('fragment' => 'x', 'attributes' => array('title' => 'X', 'class' => array('a', 'b')), 'language' => 'en');
    $link_options_2 = array('fragment' => 'y', 'attributes' => array('title' => 'Y', 'class' => array('c', 'd')), 'html' => TRUE);
    $expected = array('fragment' => 'y', 'attributes' => array('title' => 'Y', 'class' => array('a', 'b', 'c', 'd')), 'language' => 'en', 'html' => TRUE);
    $this->assertIdentical(drupal_array_merge_deep($link_options_1, $link_options_2), $expected, 'drupal_array_merge_deep() returned a properly merged array.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/bootstrap.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/bootstrap.test) · Licensed GPL-2.0-or-later (see LICENSE)._
