# ThemeTableTestCase::testThemeTableNoStickyHeaders()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 197–208 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L197-L208)
- **Class:** [ThemeTableTestCase](../ThemeTableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeTableNoStickyHeaders()
```

## Documentation

```text
If $sticky is FALSE, no tableheader.js should be included.
```

## Code

```php
  function testThemeTableNoStickyHeaders() {
    $header = array('one', 'two', 'three');
    $rows = array(array(1,2,3), array(4,5,6), array(7,8,9));
    $attributes = array();
    $caption = NULL;
    $colgroups = array();
    $this->content = theme('table', array('header' => $header, 'rows' => $rows, 'attributes' => $attributes, 'caption' => $caption, 'colgroups' => $colgroups, 'sticky' => FALSE));
    $js = drupal_add_js();
    $this->assertFalse(isset($js['misc/tableheader.js']), 'tableheader.js was not included because $sticky = FALSE.');
    $this->assertNoRaw('sticky-enabled', 'Table does not have a class of sticky-enabled because $sticky = FALSE.');
    drupal_static_reset('drupal_add_js');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
