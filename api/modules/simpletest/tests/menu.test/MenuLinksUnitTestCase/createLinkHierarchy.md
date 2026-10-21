# MenuLinksUnitTestCase::createLinkHierarchy()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 689–735 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L689-L735)
- **Class:** [MenuLinksUnitTestCase](../MenuLinksUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function createLinkHierarchy($module = 'menu_test')
```

## Documentation

```text
Create a simple hierarchy of links.
```

## Code

```php
  function createLinkHierarchy($module = 'menu_test') {
    // First remove all the menu links.
    db_truncate('menu_links')->execute();

    // Then create a simple link hierarchy:
    // - $parent
    //   - $child-1
    //      - $child-1-1
    //      - $child-1-2
    //   - $child-2
    $base_options = array(
      'link_title' => 'Menu link test',
      'module' => $module,
      'menu_name' => 'menu_test',
    );

    $links['parent'] = $base_options + array(
      'link_path' => 'menu-test/parent',
    );
    menu_link_save($links['parent']);

    $links['child-1'] = $base_options + array(
      'link_path' => 'menu-test/parent/child-1',
      'plid' => $links['parent']['mlid'],
    );
    menu_link_save($links['child-1']);

    $links['child-1-1'] = $base_options + array(
      'link_path' => 'menu-test/parent/child-1/child-1-1',
      'plid' => $links['child-1']['mlid'],
    );
    menu_link_save($links['child-1-1']);

    $links['child-1-2'] = $base_options + array(
      'link_path' => 'menu-test/parent/child-1/child-1-2',
      'plid' => $links['child-1']['mlid'],
    );
    menu_link_save($links['child-1-2']);

    $links['child-2'] = $base_options + array(
      'link_path' => 'menu-test/parent/child-2',
      'plid' => $links['parent']['mlid'],
    );
    menu_link_save($links['child-2']);

    return $links;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
