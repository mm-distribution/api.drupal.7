# MenuRouterTestCase::testMenuLinkMaintain()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 323–364 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L323-L364)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMenuLinkMaintain()
```

## Documentation

```text
Tests for menu_link_maintain().
```

## Code

```php
  function testMenuLinkMaintain() {
    $admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($admin_user);

    // Create three menu items.
    menu_link_maintain('menu_test', 'insert', 'menu_test_maintain/1', 'Menu link #1');
    menu_link_maintain('menu_test', 'insert', 'menu_test_maintain/1', 'Menu link #1-1');
    menu_link_maintain('menu_test', 'insert', 'menu_test_maintain/2', 'Menu link #2');

    // Move second link to the main-menu, to test caching later on.
    db_update('menu_links')
      ->fields(array('menu_name' => 'main-menu'))
      ->condition('link_title', 'Menu link #1-1')
      ->condition('customized', 0)
      ->condition('module', 'menu_test')
      ->execute();
    menu_cache_clear('main-menu');

    // Load front page.
    $this->drupalGet('node');
    $this->assertLink(t('Menu link #1'), 0, 'Found menu link #1');
    $this->assertLink(t('Menu link #1-1'), 0, 'Found menu link #1-1');
    $this->assertLink(t('Menu link #2'), 0, 'Found menu link #2');

    // Rename all links for the given path.
    menu_link_maintain('menu_test', 'update', 'menu_test_maintain/1', 'Menu link updated');
    // Load a different page to be sure that we have up to date information.
    $this->drupalGet('menu_test_maintain/1');
    $this->assertLink(t('Menu link updated'), 0, 'Found updated menu link');
    $this->assertNoLink(t('Menu link #1'), 0, 'Not found menu link #1');
    $this->assertNoLink(t('Menu link #1'), 0, 'Not found menu link #1-1');
    $this->assertLink(t('Menu link #2'), 0, 'Found menu link #2');

    // Delete all links for the given path.
    menu_link_maintain('menu_test', 'delete', 'menu_test_maintain/1', '');
    // Load a different page to be sure that we have up to date information.
    $this->drupalGet('menu_test_maintain/2');
    $this->assertNoLink(t('Menu link updated'), 0, 'Not found deleted menu link');
    $this->assertNoLink(t('Menu link #1'), 0, 'Not found menu link #1');
    $this->assertNoLink(t('Menu link #1'), 0, 'Not found menu link #1-1');
    $this->assertLink(t('Menu link #2'), 0, 'Found menu link #2');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
