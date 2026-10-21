# MenuTestCase::testUnpublishedNodeMenuItem()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 645–683 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L645-L683)
- **Class:** [MenuTestCase](../MenuTestCase.md)
- **Module/theme:** menu

## Signature

```php
function testUnpublishedNodeMenuItem()
```

## Documentation

```text
Tests that menu admin lists can include menu items for unpublished nodes.
```

## Code

```php
  function testUnpublishedNodeMenuItem() {
    // Log in as an administrator who can view unpublished nodes.
    $menu_and_node_admin_user = $this->drupalCreateUser(array(
      'bypass node access',
      'administer menu',
    ));
    $this->drupalLogin($menu_and_node_admin_user);

    // Create an unpublished node with a menu link.
    $title = $this->randomName();
    $node = $this->drupalCreateNode(array(
      'type' => 'article',
      'title' => $title,
      'status' => NODE_NOT_PUBLISHED,
    ));
    $edit = array(
      'link_path' => 'node/' . $node->nid,
      'link_title' => $title,
      'description' => '',
      'enabled' => TRUE,
      'expanded' => TRUE,
      'parent' => 'navigation:0',
      'weight' => '0',
    );
    $this->drupalPost('admin/structure/menu/manage/navigation/add', $edit, t('Save'));

    // Verify that the administrator can see the menu link (with a label
    // indicating that it is unpublished) on the menu management page.
    $this->drupalGet('admin/structure/menu/manage/navigation');
    $this->assertText($title . ' (unpublished)', 'Menu link to unpublished node is visible to users with "bypass node access" permission.');

    // Verify that a user who cannot view unpublished nodes does not see the
    // menu link on the menu management page.
    $menu_admin_user = $this->drupalCreateUser(array('administer menu'));
    $this->drupalLogin($menu_admin_user);
    $this->drupalGet('admin/structure/menu/manage/navigation');
    $this->assertResponse(200);
    $this->assertNoText($title, 'Menu link to unpublished node is not visible to users without the "bypass node access" permission.');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
