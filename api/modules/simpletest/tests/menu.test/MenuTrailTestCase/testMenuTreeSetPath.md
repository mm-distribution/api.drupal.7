# MenuTrailTestCase::testMenuTreeSetPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 1593–1651 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L1593-L1651)
- **Class:** [MenuTrailTestCase](../MenuTrailTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuTreeSetPath()
```

## Documentation

```text
Tests active trails are properly affected by menu_tree_set_path().
```

## Code

```php
  function testMenuTreeSetPath() {
    $home = array('<front>' => 'Home');
    $config_tree = array(
      'admin' => t('Administration'),
      'admin/config' => t('Configuration'),
    );
    $config = $home + $config_tree;

    // The menu_test_menu_tree_set_path system variable controls whether or not
    // the menu_test_menu_trail_callback() callback (used by all paths in these
    // tests) issues an overriding call to menu_trail_set_path().
    $test_menu_path = array(
      'menu_name' => 'management',
      'path' => 'admin/config/system/site-information',
    );

    $breadcrumb = $home + array(
      'menu-test' => t('Menu test root'),
    );
    $tree = array(
      'menu-test' => t('Menu test root'),
      'menu-test/menu-trail' => t('Menu trail - Case 1'),
    );

    // Test the tree generation for the Navigation menu.
    variable_del('menu_test_menu_tree_set_path');
    $this->assertBreadcrumb('menu-test/menu-trail', $breadcrumb, t('Menu trail - Case 1'), $tree);

    // Override the active trail for the Management tree; it should not affect
    // the Navigation tree.
    variable_set('menu_test_menu_tree_set_path', $test_menu_path);
    $this->assertBreadcrumb('menu-test/menu-trail', $breadcrumb, t('Menu trail - Case 1'), $tree);

    $breadcrumb = $config + array(
      'admin/config/development' => t('Development'),
    );
    $tree = $config_tree + array(
      'admin/config/development' => t('Development'),
      'admin/config/development/menu-trail' => t('Menu trail - Case 2'),
    );

    $override_breadcrumb = $config + array(
      'admin/config/system' => t('System'),
      'admin/config/system/site-information' => t('Site information'),
    );
    $override_tree = $config_tree + array(
      'admin/config/system' => t('System'),
      'admin/config/system/site-information' => t('Site information'),
    );

    // Test the tree generation for the Management menu.
    variable_del('menu_test_menu_tree_set_path');
    $this->assertBreadcrumb('admin/config/development/menu-trail', $breadcrumb, t('Menu trail - Case 2'), $tree);

    // Override the active trail for the Management tree; it should affect the
    // breadcrumbs and Management tree.
    variable_set('menu_test_menu_tree_set_path', $test_menu_path);
    $this->assertBreadcrumb('admin/config/development/menu-trail', $override_breadcrumb, t('Menu trail - Case 2'), $override_tree);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
