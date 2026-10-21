# MenuTestCase::doMenuTests()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 209–275 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L209-L275)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function doMenuTests($menu_name = 'navigation')
```

## Documentation

```text
Test menu functionality using navigation menu.
```

## Code

```php
  function doMenuTests($menu_name = 'navigation') {
    // Add nodes to use as links for menu links.
    $node1 = $this->drupalCreateNode(array('type' => 'article'));
    $node2 = $this->drupalCreateNode(array('type' => 'article'));
    $node3 = $this->drupalCreateNode(array('type' => 'article'));
    $node4 = $this->drupalCreateNode(array('type' => 'article'));
    $node5 = $this->drupalCreateNode(array('type' => 'article'));

    // Add menu links.
    $item1 = $this->addMenuLink(0, 'node/' . $node1->nid, $menu_name);
    $item2 = $this->addMenuLink($item1['mlid'], 'node/' . $node2->nid, $menu_name, FALSE);
    $item3 = $this->addMenuLink($item2['mlid'], 'node/' . $node3->nid, $menu_name);
    $this->assertMenuLink($item1['mlid'], array('depth' => 1, 'has_children' => 1, 'p1' => $item1['mlid'], 'p2' => 0));
    $this->assertMenuLink($item2['mlid'], array('depth' => 2, 'has_children' => 1, 'p1' => $item1['mlid'], 'p2' => $item2['mlid'], 'p3' => 0));
    $this->assertMenuLink($item3['mlid'], array('depth' => 3, 'has_children' => 0, 'p1' => $item1['mlid'], 'p2' => $item2['mlid'], 'p3' => $item3['mlid'], 'p4' => 0));

    // Add 102 menu links with increasing weights, then make sure the last-added
    // item's weight doesn't get changed because of the old hardcoded delta = 50
    $items = array();
    for ($i = -50; $i <= 51; $i++) {
      $items[$i] = $this->addMenuLink(0, 'node/' . $node1->nid, $menu_name, TRUE, strval($i));
    }
    $this->assertMenuLink($items[51]['mlid'], array('weight' => '51'));

    // Verify menu links.
    $this->verifyMenuLink($item1, $node1);
    $this->verifyMenuLink($item2, $node2, $item1, $node1);
    $this->verifyMenuLink($item3, $node3, $item2, $node2);

    // Add more menu links.
    $item4 = $this->addMenuLink(0, 'node/' . $node4->nid, $menu_name);
    $item5 = $this->addMenuLink($item4['mlid'], 'node/' . $node5->nid, $menu_name);
    $this->assertMenuLink($item4['mlid'], array('depth' => 1, 'has_children' => 1, 'p1' => $item4['mlid'], 'p2' => 0));
    $this->assertMenuLink($item5['mlid'], array('depth' => 2, 'has_children' => 0, 'p1' => $item4['mlid'], 'p2' => $item5['mlid'], 'p3' => 0));

    // Modify menu links.
    $this->modifyMenuLink($item1);
    $this->modifyMenuLink($item2);

    // Toggle menu links.
    $this->toggleMenuLink($item1);
    $this->toggleMenuLink($item2);

    // Move link and verify that descendants are updated.
    $this->moveMenuLink($item2, $item5['mlid'], $menu_name);
    $this->assertMenuLink($item1['mlid'], array('depth' => 1, 'has_children' => 0, 'p1' => $item1['mlid'], 'p2' => 0));
    $this->assertMenuLink($item4['mlid'], array('depth' => 1, 'has_children' => 1, 'p1' => $item4['mlid'], 'p2' => 0));
    $this->assertMenuLink($item5['mlid'], array('depth' => 2, 'has_children' => 1, 'p1' => $item4['mlid'], 'p2' => $item5['mlid'], 'p3' => 0));
    $this->assertMenuLink($item2['mlid'], array('depth' => 3, 'has_children' => 1, 'p1' => $item4['mlid'], 'p2' => $item5['mlid'], 'p3' => $item2['mlid'], 'p4' => 0));
    $this->assertMenuLink($item3['mlid'], array('depth' => 4, 'has_children' => 0, 'p1' => $item4['mlid'], 'p2' => $item5['mlid'], 'p3' => $item2['mlid'], 'p4' => $item3['mlid'], 'p5' => 0));

    // Enable a link via the overview form.
    $this->disableMenuLink($item1);
    $edit = array();

    // Note in the UI the 'mlid:x[hidden]' form element maps to enabled, or
    // NOT hidden.
    $edit['mlid:' . $item1['mlid'] . '[hidden]'] = TRUE;
    $this->drupalPost('admin/structure/menu/manage/' . $item1['menu_name'], $edit, t('Save configuration'));

    // Verify in the database.
    $this->assertMenuLink($item1['mlid'], array('hidden' => 0));

    // Save menu links for later tests.
    $this->items[] = $item1;
    $this->items[] = $item2;
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
