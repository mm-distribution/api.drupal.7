# NodeCreationTestCase::testNodeCreation()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 620–634 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L620-L634)
- **Class:** [NodeCreationTestCase](../NodeCreationTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeCreation()
```

## Documentation

```text
Creates a "Basic page" node and verifies its consistency in the database.
```

## Code

```php
  function testNodeCreation() {
    // Create a node.
    $edit = array();
    $langcode = LANGUAGE_NONE;
    $edit["title"] = $this->randomName(8);
    $edit["body[$langcode][0][value]"] = $this->randomName(16);
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the Basic page has been created.
    $this->assertRaw(t('!post %title has been created.', array('!post' => 'Basic page', '%title' => $edit["title"])), 'Basic page created.');

    // Check that the node exists in the database.
    $node = $this->drupalGetNodeByTitle($edit["title"]);
    $this->assertTrue($node, 'Node found in database.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
