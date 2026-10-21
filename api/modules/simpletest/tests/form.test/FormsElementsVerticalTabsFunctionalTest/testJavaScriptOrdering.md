# FormsElementsVerticalTabsFunctionalTest::testJavaScriptOrdering()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1214–1219 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1214-L1219)
- **Class:** [FormsElementsVerticalTabsFunctionalTest](../FormsElementsVerticalTabsFunctionalTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testJavaScriptOrdering()
```

## Documentation

```text
Ensures that vertical-tabs.js is included before collapse.js.

Otherwise, collapse.js adds "SHOW" or "HIDE" labels to the tabs.
```

## Code

```php
  function testJavaScriptOrdering() {
    $this->drupalGet('form_test/vertical-tabs');
    $position1 = strpos($this->content, 'misc/vertical-tabs.js');
    $position2 = strpos($this->content, 'misc/collapse.js');
    $this->assertTrue($position1 !== FALSE && $position2 !== FALSE && $position1 < $position2, 'vertical-tabs.js is included before collapse.js');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
