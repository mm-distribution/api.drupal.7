# DBLogTestCase::doNode()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 347–403 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L347-L403)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
private function doNode($type)
```

## Documentation

```text
Generates and then verifies some node events.

@param string $type
  A node type (e.g., 'article', 'page' or 'poll').
```

## Code

```php
  private function doNode($type) {
    // Create user.
    $perm = array('create ' . $type . ' content', 'edit own ' . $type . ' content', 'delete own ' . $type . ' content');
    $user = $this->drupalCreateUser($perm);
    // Login user.
    $this->drupalLogin($user);

    // Create a node using the form in order to generate an add content event
    // (which is not triggered by drupalCreateNode).
    $edit = $this->getContent($type);
    $langcode = LANGUAGE_NONE;
    $title = $edit["title"];
    $this->drupalPost('node/add/' . $type, $edit, t('Save'));
    $this->assertResponse(200);
    // Retrieve the node object.
    $node = $this->drupalGetNodeByTitle($title);
    $this->assertTrue($node != NULL, format_string('Node @title was loaded', array('@title' => $title)));
    // Edit the node.
    $edit = $this->getContentUpdate($type);
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertResponse(200);
    // Delete the node.
    $this->drupalPost('node/' . $node->nid . '/delete', array(), t('Delete'));
    $this->assertResponse(200);
    // View the node (to generate page not found event).
    $this->drupalGet('node/' . $node->nid);
    $this->assertResponse(404);
    // View the database log report (to generate access denied event).
    $this->drupalGet('admin/reports/dblog');
    $this->assertResponse(403);

    // Login the admin user.
    $this->drupalLogin($this->big_user);
    // View the database log report.
    $this->drupalGet('admin/reports/dblog');
    $this->assertResponse(200);

    // Verify that node events were recorded.
    // Was node content added?
    $this->assertLogMessage(t('@type: added %title.', array('@type' => $type, '%title' => $title)), 'DBLog event was recorded: [content added]');
    // Was node content updated?
    $this->assertLogMessage(t('@type: updated %title.', array('@type' => $type, '%title' => $title)), 'DBLog event was recorded: [content updated]');
    // Was node content deleted?
    $this->assertLogMessage(t('@type: deleted %title.', array('@type' => $type, '%title' => $title)), 'DBLog event was recorded: [content deleted]');

    // View the database log access-denied report page.
    $this->drupalGet('admin/reports/access-denied');
    $this->assertResponse(200);
    // Verify that the 'access denied' event was recorded.
    $this->assertText(t('admin/reports/dblog'), 'DBLog event was recorded: [access denied]');

    // View the database log page-not-found report page.
    $this->drupalGet('admin/reports/page-not-found');
    $this->assertResponse(200);
    // Verify that the 'page not found' event was recorded.
    $this->assertText(t('node/@nid', array('@nid' => $node->nid)), 'DBLog event was recorded: [page not found]');
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
