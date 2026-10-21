# PageEditTestCase::testPageEdit()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 337–399 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L337-L399)
- **Class:** [PageEditTestCase](../PageEditTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPageEdit()
```

## Documentation

```text
Checks node edit functionality.
```

## Code

```php
  function testPageEdit() {
    $this->drupalLogin($this->web_user);

    $langcode = LANGUAGE_NONE;
    $title_key = "title";
    $body_key = "body[$langcode][0][value]";
    // Create node to edit.
    $edit = array();
    $edit[$title_key] = $this->randomName(8);
    $edit[$body_key] = $this->randomName(16);
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the node exists in the database.
    $node = $this->drupalGetNodeByTitle($edit[$title_key]);
    $this->assertTrue($node, 'Node found in database.');

    // Check that "edit" link points to correct page.
    $this->clickLink(t('Edit'));
    $edit_url = url("node/$node->nid/edit", array('absolute' => TRUE));
    $actual_url = $this->getURL();
    $this->assertEqual($edit_url, $actual_url, 'On edit page.');

    // Check that the title and body fields are displayed with the correct values.
    $active = '<span class="element-invisible">' . t('(active tab)') . '</span>';
    $link_text = t('!local-task-title!active', array('!local-task-title' => t('Edit'), '!active' => $active));
    $this->assertText(strip_tags($link_text), 0, 'Edit tab found and marked active.');
    $this->assertFieldByName($title_key, $edit[$title_key], 'Title field displayed.');
    $this->assertFieldByName($body_key, $edit[$body_key], 'Body field displayed.');

    // Edit the content of the node.
    $edit = array();
    $edit[$title_key] = $this->randomName(8);
    $edit[$body_key] = $this->randomName(16);
    // Stay on the current page, without reloading.
    $this->drupalPost(NULL, $edit, t('Save'));

    // Check that the title and body fields are displayed with the updated values.
    $this->assertText($edit[$title_key], 'Title displayed.');
    $this->assertText($edit[$body_key], 'Body displayed.');

    // Login as a second administrator user.
    $second_web_user = $this->drupalCreateUser(array('administer nodes', 'edit any page content'));
    $this->drupalLogin($second_web_user);
    // Edit the same node, creating a new revision.
    $this->drupalGet("node/$node->nid/edit");
    $edit = array();
    $edit['title'] = $this->randomName(8);
    $edit[$body_key] = $this->randomName(16);
    $edit['revision'] = TRUE;
    $this->drupalPost(NULL, $edit, t('Save'));

    // Ensure that the node revision has been created.
    $revised_node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertNotIdentical($node->vid, $revised_node->vid, 'A new revision has been created.');
    // Ensure that the node author is preserved when it was not changed in the
    // edit form.
    $this->assertIdentical($node->uid, $revised_node->uid, 'The node author has been preserved.');
    // Ensure that the revision authors are different since the revisions were
    // made by different users.
    $first_node_version = node_load($node->nid, $node->vid);
    $second_node_version = node_load($node->nid, $revised_node->vid);
    $this->assertNotIdentical($first_node_version->revision_uid, $second_node_version->revision_uid, 'Each revision has a distinct user.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
