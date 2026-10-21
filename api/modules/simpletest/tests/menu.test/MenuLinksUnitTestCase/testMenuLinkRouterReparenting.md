# MenuLinksUnitTestCase::testMenuLinkRouterReparenting()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 836–887 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L836-L887)
- **Class:** [MenuLinksUnitTestCase](../MenuLinksUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuLinkRouterReparenting()
```

## Documentation

```text
Test automatic reparenting of menu links derived from menu routers.
```

## Code

```php
  function testMenuLinkRouterReparenting() {
    // Run all the standard parenting tests on menu links derived from
    // menu routers.
    $this->testMenuLinkReparenting('system');

    // Additionnaly, test reparenting based on path.
    $links = $this->createLinkHierarchy('system');

    // Move child-1-2 has a child of child-2, making the link hierarchy
    // inconsistent with the path hierarchy.
    $links['child-1-2']['plid'] = $links['child-2']['mlid'];
    menu_link_save($links['child-1-2']);

    // Check the new hierarchy.
    $expected_hierarchy = array(
      'parent' => FALSE,
      'child-1' => 'parent',
      'child-1-1' => 'child-1',
      'child-2' => 'parent',
      'child-1-2' => 'child-2',
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);

    // Now delete 'parent' directly from the database, simulating a database
    // crash. 'child-1' and 'child-2' should get moved to the
    // top-level.
    // Don't do that at home.
    db_delete('menu_links')
      ->condition('mlid', $links['parent']['mlid'])
      ->execute();
    $expected_hierarchy = array(
      'child-1' => FALSE,
      'child-1-1' => 'child-1',
      'child-2' => FALSE,
      'child-1-2' => 'child-2',
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);

    // Now delete 'child-2' directly from the database, simulating a database
    // crash. 'child-1-2' will get reparented under 'child-1' based on its
    // path.
    // Don't do that at home.
    db_delete('menu_links')
      ->condition('mlid', $links['child-2']['mlid'])
      ->execute();
    $expected_hierarchy = array(
      'child-1' => FALSE,
      'child-1-1' => 'child-1',
      'child-1-2' => 'child-1',
    );
    $this->assertMenuLinkParents($links, $expected_hierarchy);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
