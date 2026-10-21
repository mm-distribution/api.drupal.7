# MenuRouterTestCase::testMenuHidden()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 427–511 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L427-L511)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuHidden()
```

## Documentation

```text
Tests menu link depth and parents of local tasks and menu callbacks.
```

## Code

```php
  function testMenuHidden() {
    // Verify links for one dynamic argument.
    $links = db_select('menu_links', 'ml')
      ->fields('ml')
      ->condition('ml.router_path', 'menu-test/hidden/menu%', 'LIKE')
      ->orderBy('ml.router_path')
      ->execute()
      ->fetchAllAssoc('router_path', PDO::FETCH_ASSOC);

    $parent = $links['menu-test/hidden/menu'];
    $depth = $parent['depth'] + 1;
    $plid = $parent['mlid'];

    $link = $links['menu-test/hidden/menu/list'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/menu/add'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/menu/settings'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/menu/manage/%'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $parent = $links['menu-test/hidden/menu/manage/%'];
    $depth = $parent['depth'] + 1;
    $plid = $parent['mlid'];

    $link = $links['menu-test/hidden/menu/manage/%/list'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/menu/manage/%/add'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/menu/manage/%/edit'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/menu/manage/%/delete'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    // Verify links for two dynamic arguments.
    $links = db_select('menu_links', 'ml')
      ->fields('ml')
      ->condition('ml.router_path', 'menu-test/hidden/block%', 'LIKE')
      ->orderBy('ml.router_path')
      ->execute()
      ->fetchAllAssoc('router_path', PDO::FETCH_ASSOC);

    $parent = $links['menu-test/hidden/block'];
    $depth = $parent['depth'] + 1;
    $plid = $parent['mlid'];

    $link = $links['menu-test/hidden/block/list'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/block/add'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/block/manage/%/%'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $parent = $links['menu-test/hidden/block/manage/%/%'];
    $depth = $parent['depth'] + 1;
    $plid = $parent['mlid'];

    $link = $links['menu-test/hidden/block/manage/%/%/configure'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));

    $link = $links['menu-test/hidden/block/manage/%/%/delete'];
    $this->assertEqual($link['depth'], $depth, format_string('%path depth @link_depth is equal to @depth.', array('%path' => $link['router_path'], '@link_depth' => $link['depth'], '@depth' => $depth)));
    $this->assertEqual($link['plid'], $plid, format_string('%path plid @link_plid is equal to @plid.', array('%path' => $link['router_path'], '@link_plid' => $link['plid'], '@plid' => $plid)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
