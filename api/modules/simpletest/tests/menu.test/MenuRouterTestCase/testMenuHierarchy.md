# MenuRouterTestCase::testMenuHierarchy()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 415–422 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L415-L422)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuHierarchy()
```

## Documentation

```text
Tests for menu hierarchy.
```

## Code

```php
  function testMenuHierarchy() {
    $parent_link = db_query('SELECT * FROM {menu_links} WHERE link_path = :link_path', array(':link_path' => 'menu-test/hierarchy/parent'))->fetchAssoc();
    $child_link = db_query('SELECT * FROM {menu_links} WHERE link_path = :link_path', array(':link_path' => 'menu-test/hierarchy/parent/child'))->fetchAssoc();
    $unattached_child_link = db_query('SELECT * FROM {menu_links} WHERE link_path = :link_path', array(':link_path' => 'menu-test/hierarchy/parent/child2/child'))->fetchAssoc();

    $this->assertEqual($child_link['plid'], $parent_link['mlid'], 'The parent of a directly attached child is correct.');
    $this->assertEqual($unattached_child_link['plid'], $parent_link['mlid'], 'The parent of a non-directly attached child is correct.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
