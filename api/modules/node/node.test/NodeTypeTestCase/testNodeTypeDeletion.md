# NodeTypeTestCase::testNodeTypeDeletion()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1642–1678 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1642-L1678)
- **Class:** [NodeTypeTestCase](../NodeTypeTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTypeDeletion()
```

## Documentation

```text
Tests deleting a content type that still has content.
```

## Code

```php
  function testNodeTypeDeletion() {
    // Create a content type programmatically.
    $type = $this->drupalCreateContentType();

    // Log in a test user.
    $web_user = $this->drupalCreateUser(array(
      'bypass node access',
      'administer content types',
    ));
    $this->drupalLogin($web_user);

    // Add a new node of this type.
    $node = $this->drupalCreateNode(array('type' => $type->type));
    // Attempt to delete the content type, which should not be allowed.
    $this->drupalGet('admin/structure/types/manage/' . $type->name . '/delete');
    $this->assertRaw(
      t(
        '%type is used by 1 piece of content on your site. You cannot remove this content type until you have removed all of the %type content.',
        array('%type' => $type->name)
      ),
      'The content type will not be deleted until all nodes of that type are removed.'
    );
    $this->assertNoText(t('This action cannot be undone.'), 'The node type deletion confirmation form is not available.');

    // Delete the node.
    node_delete($node->nid);
    // Attempt to delete the content type, which should now be allowed.
    $this->drupalGet('admin/structure/types/manage/' . $type->name . '/delete');
    $this->assertRaw(
      t(
        'Are you sure you want to delete the content type %type?',
        array('%type' => $type->name)
      ),
      'The content type is available for deletion.'
    );
    $this->assertText(t('This action cannot be undone.'), 'The node type deletion confirmation form is available.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
