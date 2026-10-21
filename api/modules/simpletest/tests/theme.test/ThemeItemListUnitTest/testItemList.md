# ThemeItemListUnitTest::testItemList()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 279–290 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L279-L290)
- **Class:** [ThemeItemListUnitTest](../ThemeItemListUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testItemList()
```

## Documentation

```text
Test item list rendering.
```

## Code

```php
  function testItemList() {
    $items = array('a', array('data' => 'b', 'children' => array('c' => 'c', 'd' => 'd', 'e' => 'e')), 'f');
    $expected = '<div class="item-list"><ul><li class="first">a</li>
<li>b<div class="item-list"><ul><li class="first">c</li>
<li>d</li>
<li class="last">e</li>
</ul></div></li>
<li class="last">f</li>
</ul></div>';
    $output = theme('item_list', array('items' => $items));
    $this->assertIdentical($expected, $output, 'Item list is rendered correctly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
