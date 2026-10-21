# NodeTypeTestCase::testNodeTypeCreation()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1511–1536 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1511-L1536)
- **Class:** [NodeTypeTestCase](../NodeTypeTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTypeCreation()
```

## Documentation

```text
Tests creating a content type programmatically and via a form.
```

## Code

```php
  function testNodeTypeCreation() {
    // Create a content type programmaticaly.
    $type = $this->drupalCreateContentType();

    $type_exists = db_query('SELECT 1 FROM {node_type} WHERE type = :type', array(':type' => $type->type))->fetchField();
    $this->assertTrue($type_exists, 'The new content type has been created in the database.');

    // Login a test user.
    $web_user = $this->drupalCreateUser(array('create ' . $type->name . ' content'));
    $this->drupalLogin($web_user);

    $this->drupalGet('node/add/' . str_replace('_', '-', $type->name));
    $this->assertResponse(200, 'The new content type can be accessed at node/add.');

    // Create a content type via the user interface.
    $web_user = $this->drupalCreateUser(array('bypass node access', 'administer content types'));
    $this->drupalLogin($web_user);
    $edit = array(
      'name' => 'foo',
      'title_label' => 'title for foo',
      'type' => 'foo',
    );
    $this->drupalPost('admin/structure/types/add', $edit, t('Save content type'));
    $type_exists = db_query('SELECT 1 FROM {node_type} WHERE type = :type', array(':type' => 'foo'))->fetchField();
    $this->assertTrue($type_exists, 'The new content type has been created in the database.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
