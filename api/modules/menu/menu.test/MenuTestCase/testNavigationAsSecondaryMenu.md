# MenuTestCase::testNavigationAsSecondaryMenu()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 300–316 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L300-L316)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function testNavigationAsSecondaryMenu()
```

## Documentation

```text
Tries to use the navigation menu as the source for secondary links.
```

## Code

```php
  function testNavigationAsSecondaryMenu() {
    $this->drupalLogin($this->big_user);

    // Go to the menu settings page and make the navigation the source for the
    // secondary menu.
    $edit = array(
      'menu_main_links_source' => 'main-menu',
      'menu_secondary_links_source' => 'navigation',
    );
    $this->drupalGet('admin/structure/menu/settings');
    $this->drupalPost(NULL, $edit, t('Save configuration'));

    // Now visit the user page. There should be an 'Add content' link in the
    // navigation block and one in the secondary menu.
    $this->drupalGet('user');
    $this->assertNoUniqueText(t('Add content'));
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
