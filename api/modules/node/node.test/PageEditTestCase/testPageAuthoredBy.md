# PageEditTestCase::testPageAuthoredBy()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 404–444 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L404-L444)
- **Class:** [PageEditTestCase](../PageEditTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPageAuthoredBy()
```

## Documentation

```text
Tests changing a node's "authored by" field.
```

## Code

```php
  function testPageAuthoredBy() {
    $this->drupalLogin($this->admin_user);

    // Create node to edit.
    $langcode = LANGUAGE_NONE;
    $body_key = "body[$langcode][0][value]";
    $edit = array();
    $edit['title'] = $this->randomName(8);
    $edit[$body_key] = $this->randomName(16);
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the node was authored by the currently logged in user.
    $node = $this->drupalGetNodeByTitle($edit['title']);
    $this->assertIdentical($node->uid, $this->admin_user->uid, 'Node authored by admin user.');

    // Try to change the 'authored by' field to an invalid user name.
    $edit = array(
      'name' => 'invalid-name',
    );
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $this->assertText('The username invalid-name does not exist.');

    // Change the authored by field to an empty string, which should assign
    // authorship to the anonymous user (uid 0).
    $edit['name'] = '';
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $node = node_load($node->nid, NULL, TRUE);
    $this->assertIdentical($node->uid, '0', 'Node authored by anonymous user.');

    // Change the authored by field to another user's name (that is not
    // logged in).
    $edit['name'] = $this->web_user->name;
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    $node = node_load($node->nid, NULL, TRUE);
    $this->assertIdentical($node->uid, $this->web_user->uid, 'Node authored by normal user.');

    // Check that normal users cannot change the authored by information.
    $this->drupalLogin($this->web_user);
    $this->drupalGet('node/' . $node->nid . '/edit');
    $this->assertNoFieldByName('name');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
