# ForumTestCase::doAdminTests()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 286–359 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L286-L359)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
private function doAdminTests($user)
```

## Documentation

```text
Runs admin tests on the admin user.

@param object $user
  The logged in user.
```

## Code

```php
  private function doAdminTests($user) {
    // Login the user.
    $this->drupalLogin($user);

    // Enable the active forum block.
    $edit = array();
    $edit['blocks[forum_active][region]'] = 'sidebar_second';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertResponse(200);
    $this->assertText(t('The block settings have been updated.'), 'Active forum topics forum block was enabled');

    // Enable the new forum block.
    $edit = array();
    $edit['blocks[forum_new][region]'] = 'sidebar_second';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
    $this->assertResponse(200);
    $this->assertText(t('The block settings have been updated.'), '[New forum topics] Forum block was enabled');

    // Retrieve forum menu id.
    $mlid = db_query_range("SELECT mlid FROM {menu_links} WHERE link_path = 'forum' AND menu_name = 'navigation' AND module = 'system' ORDER BY mlid ASC", 0, 1)->fetchField();

    // Add forum to navigation menu.
    $edit = array();
    $this->drupalPost('admin/structure/menu/manage/navigation', $edit, t('Save configuration'));
    $this->assertResponse(200);

    // Edit forum taxonomy.
    // Restoration of the settings fails and causes subsequent tests to fail.
    $this->container = $this->editForumTaxonomy();
    // Create forum container.
    $this->container = $this->createForum('container');
    // Verify "edit container" link exists and functions correctly.
    $this->drupalGet('admin/structure/forum');
    $this->clickLink('edit container');
    $this->assertRaw('Edit container', 'Followed the link to edit the container');
    // Create forum inside the forum container.
    $this->forum = $this->createForum('forum', $this->container['tid']);
    // Verify the "edit forum" link exists and functions correctly.
    $this->drupalGet('admin/structure/forum');
    $this->clickLink('edit forum');
    $this->assertRaw('Edit forum', 'Followed the link to edit the forum');
    // Navigate back to forum structure page.
    $this->drupalGet('admin/structure/forum');
    // Create second forum in container.
    $this->delete_forum = $this->createForum('forum', $this->container['tid']);
    // Save forum overview.
    $this->drupalPost('admin/structure/forum/', array(), t('Save'));
    $this->assertRaw(t('The configuration options have been saved.'));
    // Delete this second forum.
    $this->deleteForum($this->delete_forum['tid']);
    // Create forum at the top (root) level.
    $this->root_forum = $this->createForum('forum');

    // Test vocabulary form alterations.
    $this->drupalGet('admin/structure/taxonomy/forums/edit');
    $this->assertFieldByName('op', t('Save'), 'Save button found.');
    $this->assertNoFieldByName('op', t('Delete'), 'Delete button not found.');

    // Test term edit form alterations.
    $this->drupalGet('taxonomy/term/' . $this->container['tid'] . '/edit');
    // Test parent field been hidden by forum module.
    $this->assertNoField('parent[]', 'Parent field not found.');

    // Test tags vocabulary form is not affected.
    $this->drupalGet('admin/structure/taxonomy/tags/edit');
    $this->assertFieldByName('op', t('Save'), 'Save button found.');
    $this->assertFieldByName('op', t('Delete'), 'Delete button found.');
    // Test tags vocabulary term form is not affected.
    $this->drupalGet('admin/structure/taxonomy/tags/add');
    $this->assertField('parent[]', 'Parent field found.');
    // Test relations fieldset exists.
    $relations_fieldset = $this->xpath("//fieldset[@id='edit-relations']");
    $this->assertTrue(isset($relations_fieldset[0]), 'Relations fieldset element found.');
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
