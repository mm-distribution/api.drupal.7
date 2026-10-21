# MenuLinksUnitTestCase::testMenuLinkReparenting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 754–831 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L754-L831)
- **Class:** [MenuLinksUnitTestCase](../MenuLinksUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuLinkReparenting($module = 'menu_test')
```

## Documentation

```text
Test automatic reparenting of menu links.
```

## Code

```php
  function testMenuLinkReparenting($module = 'menu_test') {
    // Check the initial hierarchy.
    $links = $this->createLinkHierarchy($module);

    $expected_hierarchy = array(
      'parent' => FALSE,
      'child-1' => 'parent',
      'child-1-1' => 'child-1',
      'child-1-2' => 'child-1',
      'child-2' => 'parent',
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);

    // Start over, and move child-1 under child-2, and check that all the
    // childs of child-1 have been moved too.
    $links = $this->createLinkHierarchy($module);
    $links['child-1']['plid'] = $links['child-2']['mlid'];
    menu_link_save($links['child-1']);

    $expected_hierarchy = array(
      'parent' => FALSE,
      'child-1' => 'child-2',
      'child-1-1' => 'child-1',
      'child-1-2' => 'child-1',
      'child-2' => 'parent',
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);

    // Start over, and delete child-1, and check that the children of child-1
    // have been reassigned to the parent. menu_link_delete() will cowardly
    // refuse to delete a menu link defined by the system module, so skip the
    // test in that case.
    if ($module != 'system') {
      $links = $this->createLinkHierarchy($module);
      menu_link_delete($links['child-1']['mlid']);

      $expected_hierarchy = array(
        'parent' => FALSE,
        'child-1-1' => 'parent',
        'child-1-2' => 'parent',
        'child-2' => 'parent',
      );
      $this->assertMenuLinkParents($links, $expected_hierarchy);
    }

    // Start over, forcefully delete child-1 from the database, simulating a
    // database crash. Check that the children of child-1 have been reassigned
    // to the parent, going up on the old path hierarchy stored in each of the
    // links.
    $links = $this->createLinkHierarchy($module);
    // Don't do that at home.
    db_delete('menu_links')
      ->condition('mlid', $links['child-1']['mlid'])
      ->execute();

    $expected_hierarchy = array(
      'parent' => FALSE,
      'child-1-1' => 'parent',
      'child-1-2' => 'parent',
      'child-2' => 'parent',
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);

    // Start over, forcefully delete the parent from the database, simulating a
    // database crash. Check that the children of parent are now top-level.
    $links = $this->createLinkHierarchy($module);
    // Don't do that at home.
    db_delete('menu_links')
      ->condition('mlid', $links['parent']['mlid'])
      ->execute();

    $expected_hierarchy = array(
      'child-1-1' => 'child-1',
      'child-1-2' => 'child-1',
      'child-2' => FALSE,
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
