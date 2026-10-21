# MenuNodeTestCase::testMenuNodeFormWidget()

- **Type:** Method
- **File:** [`modules/menu/menu.test`](../_file.md), lines 757–859 · [local source](../../../../../source/modules/menu/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test#L757-L859)
- **Class:** [MenuNodeTestCase](../MenuNodeTestCase.md)
- **Module/theme:** menu

## Signature

```php
function testMenuNodeFormWidget()
```

## Documentation

```text
Test creating, editing, deleting menu links via node form widget.
```

## Code

```php
  function testMenuNodeFormWidget() {
    // Enable Navigation menu as available menu.
    $edit = array(
      'menu_options[navigation]' => 1,
    );
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    // Change default parent item to Navigation menu, so we can assert more
    // easily.
    $edit = array(
      'menu_parent' => 'navigation:0',
    );
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));

    // Verify that the menu link title on the node add form has the correct
    // maxlength.
    $this->drupalGet('node/add/page');
    $this->assertPattern('/<input .* id="edit-menu-link-title" .* maxlength="255" .* \/>/', 'Menu link title field has correct maxlength in node add form.');

    // Create a node with menu link disabled.
    $node_title = $this->randomName();
    $language = LANGUAGE_NONE;
    $edit = array(
      "title" => $node_title,
      "body[$language][0][value]" => $this->randomString(),
    );
    $this->drupalPost('node/add/page', $edit, t('Save'));
    $node = $this->drupalGetNodeByTitle($node_title);
    // Assert that there is no link for the node.
    $this->drupalGet('');
    $this->assertNoLink($node_title);

    // Edit the node, enable the menu link setting, but skip the link title.
    $edit = array(
      'menu[enabled]' => 1,
    );
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    // Assert that there is no link for the node.
    $this->drupalGet('');
    $this->assertNoLink($node_title);

    // Edit the node and create a menu link.
    $edit = array(
      'menu[enabled]' => 1,
      'menu[link_title]' => $node_title,
      'menu[weight]' => 17,
    );
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    // Assert that the link exists.
    $this->drupalGet('');
    $this->assertLink($node_title);

    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertOptionSelected('edit-menu-weight', 17, 'Menu weight correct in edit form');

    // Verify that the menu link title on the node edit form has the correct
    // maxlength.
    $this->assertPattern('/<input .* id="edit-menu-link-title" .* maxlength="255" .* \/>/', 'Menu link title field has correct maxlength in node edit form.');

    // Edit the node and remove the menu link.
    $edit = array(
      'menu[enabled]' => FALSE,
    );
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    // Assert that there is no link for the node.
    $this->drupalGet('');
    $this->assertNoLink($node_title);

    // Add a menu link to the Management menu.
    $item = array(
      'link_path' => 'node/' . $node->nid,
      'link_title' => $this->randomName(16),
      'menu_name' => 'management',
    );
    menu_link_save($item);

    // Assert that disabled Management menu is not shown on the node/$nid/edit page.
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertText('Provide a menu link', 'Link in not allowed menu not shown in node edit form');
    // Assert that the link is still in the management menu after save.
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $link = menu_link_load($item['mlid']);
    $this->assertTrue($link, 'Link in not allowed menu still exists after saving node');

    // Move the menu link back to the Navigation menu.
    $item['menu_name'] = 'navigation';
    menu_link_save($item);
    // Create a second node.
    $child_node = $this->drupalCreateNode(array('type' => 'article'));
    // Assign a menu link to the second node, being a child of the first one.
    $child_item = array(
      'link_path' => 'node/'. $child_node->nid,
      'link_title' => $this->randomName(16),
      'plid' => $item['mlid'],
    );
    menu_link_save($child_item);
    // Edit the first node.
    $this->drupalGet('node/'. $node->nid .'/edit');
    // Assert that it is not possible to set the parent of the first node to itself or the second node.
    $this->assertNoOption('edit-menu-parent', 'navigation:'. $item['mlid']);
    $this->assertNoOption('edit-menu-parent', 'navigation:'. $child_item['mlid']);
    // Assert that unallowed Management menu is not available in options.
    $this->assertNoOption('edit-menu-parent', 'management:0');
  }
```

---
_Drupal 7.103 · [modules/menu/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
