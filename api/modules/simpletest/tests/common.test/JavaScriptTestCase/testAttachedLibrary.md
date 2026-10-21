# JavaScriptTestCase::testAttachedLibrary()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2004–2009 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2004-L2009)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testAttachedLibrary()
```

## Documentation

```text
Tests the addition of libraries through the #attached['library'] property.
```

## Code

```php
  function testAttachedLibrary() {
    $element['#attached']['library'][] = array('system', 'farbtastic');
    drupal_render($element);
    $scripts = drupal_get_js();
    $this->assertTrue(strpos($scripts, 'misc/farbtastic/farbtastic.js'), 'The attached_library property adds the additional libraries.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
