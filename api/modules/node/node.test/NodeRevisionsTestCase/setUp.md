# NodeRevisionsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 179–213 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L179-L213)
- **Class:** [NodeRevisionsTestCase](../NodeRevisionsTestCase.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    // Create and login user.
    $web_user = $this->drupalCreateUser(array('view revisions', 'revert revisions', 'edit any page content',
                                               'delete revisions', 'delete any page content'));
    $this->drupalLogin($web_user);

    // Create initial node.
    $node = $this->drupalCreateNode();
    $settings = get_object_vars($node);
    $settings['revision'] = 1;

    $nodes = array();
    $logs = array();

    // Get original node.
    $nodes[] = $node;

    // Create three revisions.
    $revision_count = 3;
    for ($i = 0; $i < $revision_count; $i++) {
      $logs[] = $settings['log'] = $this->randomName(32);

      // Create revision with random title and body and update variables.
      $this->drupalCreateNode($settings);
      $node = node_load($node->nid); // Make sure we get revision information.
      $settings = get_object_vars($node);

      $nodes[] = $node;
    }

    $this->nodes = $nodes;
    $this->logs = $logs;
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
