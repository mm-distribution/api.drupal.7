# NodeEntityViewModeAlterTest::testNodeViewModeChange()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2953–2979 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2953-L2979)
- **Class:** [NodeEntityViewModeAlterTest](../NodeEntityViewModeAlterTest.md)
- **Module/theme:** node

## Signature

```php
function testNodeViewModeChange()
```

## Documentation

```text
Create a "Basic page" node and verify its consistency in the database.
```

## Code

```php
  function testNodeViewModeChange() {
    $web_user = $this->drupalCreateUser(array('create page content', 'edit own page content'));
    $this->drupalLogin($web_user);

    // Create a node.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName(8);
    $edit["body[$langcode][0][value]"] = 'Data that should appear only in the body for the node.';
    $edit["body[$langcode][0][summary]"] = 'Extra data that should appear only in the teaser for the node.';
    $this->drupalPost('node/add/page', $edit, t('Save'));

    $node = $this->drupalGetNodeByTitle($edit["title"]);

    // Set the flag to alter the view mode and view the node.
    variable_set('node_test_change_view_mode', 'teaser');
    $this->drupalGet('node/' . $node->nid);

    // Check that teaser mode is viewed.
    $this->assertText('Extra data that should appear only in the teaser for the node.', 'Teaser text present');
    // Make sure body text is not present.
    $this->assertNoText('Data that should appear only in the body for the node.', 'Body text not present');

    // Test that the correct build mode has been set.
    $build = node_view($node);
    $this->assertEqual($build['#view_mode'], 'teaser', 'The view mode has correctly been set to teaser.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
