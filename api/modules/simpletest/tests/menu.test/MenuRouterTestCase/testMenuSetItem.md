# MenuRouterTestCase::testMenuSetItem()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 524–536 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L524-L536)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuSetItem()
```

## Documentation

```text
Test menu_set_item().
```

## Code

```php
  function testMenuSetItem() {
    $item = menu_get_item('node');

    $this->assertEqual($item['path'], 'node', "Path from menu_get_item('node') is equal to 'node'", 'menu');

    // Modify the path for the item then save it.
    $item['path'] = 'node_test';
    $item['href'] = 'node_test';

    menu_set_item('node', $item);
    $compare_item = menu_get_item('node');
    $this->assertEqual($compare_item, $item, 'Modified menu item is equal to newly retrieved menu item.', 'menu');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
