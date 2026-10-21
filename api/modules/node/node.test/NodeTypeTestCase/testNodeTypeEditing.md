# NodeTypeTestCase::testNodeTypeEditing()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1541–1589 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1541-L1589)
- **Class:** [NodeTypeTestCase](../NodeTypeTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTypeEditing()
```

## Documentation

```text
Tests editing a node type using the UI.
```

## Code

```php
  function testNodeTypeEditing() {
    $web_user = $this->drupalCreateUser(array('bypass node access', 'administer content types', 'administer fields'));
    $this->drupalLogin($web_user);

    $instance = field_info_instance('node', 'body', 'page');
    $this->assertEqual($instance['label'], 'Body', 'Body field was found.');

    // Verify that title and body fields are displayed.
    $this->drupalGet('node/add/page');
    $this->assertRaw('Title', 'Title field was found.');
    $this->assertRaw('Body', 'Body field was found.');

    // Rename the title field.
    $edit = array(
      'title_label' => 'Foo',
    );
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    // Refresh the field information for the rest of the test.
    field_info_cache_clear();

    $this->drupalGet('node/add/page');
    $this->assertRaw('Foo', 'New title label was displayed.');
    $this->assertNoRaw('Title', 'Old title label was not displayed.');

    // Change the name, machine name and description.
    $edit = array(
      'name' => 'Bar',
      'type' => 'bar',
      'description' => 'Lorem ipsum.',
    );
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    field_info_cache_clear();

    $this->drupalGet('node/add');
    $this->assertRaw('Bar', 'New name was displayed.');
    $this->assertRaw('Lorem ipsum', 'New description was displayed.');
    $this->clickLink('Bar');
    $this->assertEqual(url('node/add/bar', array('absolute' => TRUE)), $this->getUrl(), 'New machine name was used in URL.');
    $this->assertRaw('Foo', 'Title field was found.');
    $this->assertRaw('Body', 'Body field was found.');

    // Remove the body field.
    $this->drupalPost('admin/structure/types/manage/bar/fields/body/delete', NULL, t('Delete'));
    // Resave the settings for this type.
    $this->drupalPost('admin/structure/types/manage/bar', array(), t('Save content type'));
    // Check that the body field doesn't exist.
    $this->drupalGet('node/add/bar');
    $this->assertNoRaw('Body', 'Body field was not found.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
