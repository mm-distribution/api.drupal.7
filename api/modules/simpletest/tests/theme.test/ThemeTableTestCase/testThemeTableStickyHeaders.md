# ThemeTableTestCase::testThemeTableStickyHeaders()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 184–192 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L184-L192)
- **Class:** [ThemeTableTestCase](../ThemeTableTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeTableStickyHeaders()
```

## Documentation

```text
Tableheader.js provides 'sticky' table headers, and is included by default.
```

## Code

```php
  function testThemeTableStickyHeaders() {
    $header = array('one', 'two', 'three');
    $rows = array(array(1,2,3), array(4,5,6), array(7,8,9));
    $this->content = theme('table', array('header' => $header, 'rows' => $rows));
    $js = drupal_add_js();
    $this->assertTrue(isset($js['misc/tableheader.js']), 'tableheader.js was included when $sticky = TRUE.');
    $this->assertRaw('sticky-enabled', 'Table has a class of sticky-enabled when $sticky = TRUE.');
    drupal_static_reset('drupal_add_js');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
