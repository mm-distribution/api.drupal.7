# menu_test_menu()

- **Type:** Function
- **File:** [`modules/simpletest/tests/menu_test.module`](_file.md), lines 11–345 · [local source](../../../../../source/modules/simpletest/tests/menu_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module#L11-L345)
- **Module/theme:** batch_test
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function menu_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function menu_test_menu() {
  // The name of the menu changes during the course of the test. Using a $_GET.
  $items['menu_name_test'] = array(
    'title' => 'Test menu_name router item',
    'page callback' => 'node_save',
    'menu_name' => menu_test_menu_name(),
  );
  // This item is of type MENU_CALLBACK with no parents to test title.
  $items['menu_callback_title'] = array(
    'title' => 'Menu Callback Title',
    'page callback' => 'menu_test_callback',
    'type' => MENU_CALLBACK,
    'access arguments' => array('access content'),
  );
  // Use FALSE as 'title callback' to bypass t().
  $items['menu_no_title_callback'] = array(
    'title' => 'A title with @placeholder',
    'title callback' => FALSE,
    'title arguments' => array('@placeholder' => 'some other text'),
    'page callback' => 'menu_test_callback',
    'access arguments' => array('access content'),
  );

  // Hidden link for menu_link_maintain tests
  $items['menu_test_maintain/%'] = array(
    'title' => 'Menu maintain test',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
   );
  // Hierarchical tests.
  $items['menu-test/hierarchy/parent'] = array(
    'title' => 'Parent menu router',
    'page callback' => 'node_page_default',
  );
  $items['menu-test/hierarchy/parent/child'] = array(
    'title' => 'Child menu router',
    'page callback' => 'node_page_default',
  );
  $items['menu-test/hierarchy/parent/child2/child'] = array(
    'title' => 'Unattached subchild router',
    'page callback' => 'node_page_default',
  );
  // Theme callback tests.
  $items['menu-test/theme-callback/%'] = array(
    'title' => 'Page that displays different themes',
    'page callback' => 'menu_test_theme_page_callback',
    'access arguments' => array('access content'),
    'theme callback' => 'menu_test_theme_callback',
    'theme arguments' => array(2),
  );
  $items['menu-test/theme-callback/%/inheritance'] = array(
    'title' => 'Page that tests theme callback inheritance.',
    'page callback' => 'menu_test_theme_page_callback',
    'page arguments' => array(TRUE),
    'access arguments' => array('access content'),
  );
  $items['menu-test/no-theme-callback'] = array(
    'title' => 'Page that displays different themes without using a theme callback.',
    'page callback' => 'menu_test_theme_page_callback',
    'access arguments' => array('access content'),
  );
  // Path containing "exotic" characters.
  $path = "menu-test/ -._~!$'\"()*@[]?&+%#,;=:" . // "Special" ASCII characters.
    "%23%25%26%2B%2F%3F" . // Characters that look like a percent-escaped string.
    "éøïвβ中國書۞"; // Characters from various non-ASCII alphabets.
  $items[$path] = array(
    'title' => '"Exotic" path',
    'page callback' => 'menu_test_callback',
    'access arguments' => array('access content'),
  );

  // Hidden tests; base parents.
  // Same structure as in Menu and Block modules. Since those structures can
  // change, we need to simulate our own in here.
  $items['menu-test'] = array(
    'title' => 'Menu test root',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );
  $items['menu-test/hidden'] = array(
    'title' => 'Hidden test root',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );

  // Hidden tests; one dynamic argument.
  $items['menu-test/hidden/menu'] = array(
    'title' => 'Menus',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );
  $items['menu-test/hidden/menu/list'] = array(
    'title' => 'List menus',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['menu-test/hidden/menu/add'] = array(
    'title' => 'Add menu',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'type' => MENU_LOCAL_ACTION,
  );
  $items['menu-test/hidden/menu/settings'] = array(
    'title' => 'Settings',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'type' => MENU_LOCAL_TASK,
    'weight' => 5,
  );
  $items['menu-test/hidden/menu/manage/%menu'] = array(
    'title' => 'Customize menu',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );
  $items['menu-test/hidden/menu/manage/%menu/list'] = array(
    'title' => 'List links',
    'weight' => -10,
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'context' => MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE,
  );
  $items['menu-test/hidden/menu/manage/%menu/add'] = array(
    'title' => 'Add link',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'type' => MENU_LOCAL_ACTION,
  );
  $items['menu-test/hidden/menu/manage/%menu/edit'] = array(
    'title' => 'Edit menu',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'type' => MENU_LOCAL_TASK,
    'context' => MENU_CONTEXT_PAGE | MENU_CONTEXT_INLINE,
  );
  $items['menu-test/hidden/menu/manage/%menu/delete'] = array(
    'title' => 'Delete menu',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );

  // Hidden tests; two dynamic arguments.
  $items['menu-test/hidden/block'] = array(
    'title' => 'Blocks',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );
  $items['menu-test/hidden/block/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['menu-test/hidden/block/add'] = array(
    'title' => 'Add block',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'type' => MENU_LOCAL_ACTION,
  );
  $items['menu-test/hidden/block/manage/%/%'] = array(
    'title' => 'Configure block',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
  );
  $items['menu-test/hidden/block/manage/%/%/configure'] = array(
    'title' => 'Configure block',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'context' => MENU_CONTEXT_INLINE,
  );
  $items['menu-test/hidden/block/manage/%/%/delete'] = array(
    'title' => 'Delete block',
    'page callback' => 'node_page_default',
    'access arguments' => array('access content'),
    'type' => MENU_LOCAL_TASK,
    'context' => MENU_CONTEXT_NONE,
  );

  // Breadcrumbs tests.
  // @see MenuBreadcrumbTestCase
  $base = array(
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
  );
  // Local tasks: Second level below default local task.
  $items['menu-test/breadcrumb/tasks'] = array(
    'title' => 'Breadcrumbs test: Local tasks',
  ) + $base;
  $items['menu-test/breadcrumb/tasks/first'] = array(
    'title' => 'First',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  ) + $base;
  $items['menu-test/breadcrumb/tasks/second'] = array(
    'title' => 'Second',
    'type' => MENU_LOCAL_TASK,
  ) + $base;
  $items['menu-test/breadcrumb/tasks/first/first'] = array(
    'title' => 'First first',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  ) + $base;
  $items['menu-test/breadcrumb/tasks/first/second'] = array(
    'title' => 'First second',
    'type' => MENU_LOCAL_TASK,
  ) + $base;
  $items['menu-test/breadcrumb/tasks/second/first'] = array(
    'title' => 'Second first',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  ) + $base;
  $items['menu-test/breadcrumb/tasks/second/second'] = array(
    'title' => 'Second second',
    'type' => MENU_LOCAL_TASK,
  ) + $base;

  // Menu trail tests.
  // @see MenuTrailTestCase
  $items['menu-test/menu-trail'] = array(
    'title' => 'Menu trail - Case 1',
    'page callback' => 'menu_test_menu_trail_callback',
    'access arguments' => array('access content'),
  );
  $items['admin/config/development/menu-trail'] = array(
    'title' => 'Menu trail - Case 2',
    'description' => 'Tests menu_tree_set_path()',
    'page callback' => 'menu_test_menu_trail_callback',
    'access arguments' => array('access administration pages'),
  );
  $items['menu-test/custom-403-page'] = array(
    'title' => 'Custom 403 page',
    'page callback' => 'menu_test_custom_403_404_callback',
    'access arguments' => array('access content'),
  );
  $items['menu-test/custom-404-page'] = array(
    'title' => 'Custom 404 page',
    'page callback' => 'menu_test_custom_403_404_callback',
    'access arguments' => array('access content'),
  );

  // File inheritance tests. This menu item should inherit the page callback
  // system_admin_menu_block_page() and therefore render its children as links
  // on the page.
  $items['admin/config/development/file-inheritance'] = array(
    'title' => 'File inheritance',
    'description' => 'Test file inheritance',
    'access arguments' => array('access content'),
  );
  $items['admin/config/development/file-inheritance/inherit'] = array(
    'title' => 'Inherit',
    'description' => 'File inheritance test description',
    'page callback' => 'menu_test_callback',
    'access arguments' => array('access content'),
  );

  $items['menu_login_callback'] = array(
    'title' => 'Used as a login path',
    'page callback' => 'menu_login_callback',
    'access callback' => TRUE,
  );

  $items['menu-title-test/case1'] = array(
   'title' => 'Example title - Case 1',
   'access callback' => TRUE,
   'page callback' => 'menu_test_callback',
  );
  $items['menu-title-test/case2'] = array(
   'title' => 'Example @sub1 - Case @op2',
   // If '2' is not in quotes, the argument becomes arg(2).
   'title arguments' => array('@sub1' => 'title', '@op2' => '2'),
   'access callback' => TRUE,
   'page callback' => 'menu_test_callback',
  );
  $items['menu-title-test/case3'] = array(
   'title' => 'Example title',
   'title callback' => 'menu_test_title_callback',
   'access callback' => TRUE,
   'page callback' => 'menu_test_callback',
  );
  $items['menu-title-test/case4'] = array(
   // Title gets completely ignored. Good thing, too.
   'title' => 'Bike sheds full of blue smurfs',
   'title callback' => 'menu_test_title_callback',
   // If '4' is not in quotes, the argument becomes arg(4).
   'title arguments' => array('Example title', '4'),
   'access callback' => TRUE,
   'page callback' => 'menu_test_callback',
  );

  // Load arguments inheritance test.
  $items['menu-test/arguments/%menu_test_argument/%'] = array(
    'title' => 'Load arguments inheritance test',
    'load arguments' => array(3),
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
  );
  $items['menu-test/arguments/%menu_test_argument/%/default'] = array(
    'title' => 'Default local task',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['menu-test/arguments/%menu_test_argument/%/task'] = array(
    'title' => 'Local task',
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
  );
  // For this path, load arguments should be inherited for the first loader only.
  $items['menu-test/arguments/%menu_test_argument/%menu_test_other_argument/common-loader'] = array(
    'title' => 'Local task',
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
    'type' => MENU_LOCAL_TASK,
  );
  // For these paths, no load arguments should be inherited.
  // Not on the same position.
  $items['menu-test/arguments/%/%menu_test_argument/different-loaders-1'] = array(
    'title' => 'An item not sharing the same loader',
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
  );
  // Not the same loader.
  $items['menu-test/arguments/%menu_test_other_argument/%/different-loaders-2'] = array(
    'title' => 'An item not sharing the same loader',
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
  );
  // Not the same loader.
  $items['menu-test/arguments/%/%/different-loaders-3'] = array(
    'title' => 'An item not sharing the same loader',
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
  );
  // Explict load arguments should not be overriden (even if empty).
  $items['menu-test/arguments/%menu_test_argument/%/explicit-arguments'] = array(
    'title' => 'An item defining explicit load arguments',
    'load arguments' => array(),
    'page callback' => 'menu_test_callback',
    'access callback' => TRUE,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
