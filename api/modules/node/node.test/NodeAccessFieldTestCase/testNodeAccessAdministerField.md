# NodeAccessFieldTestCase::testNodeAccessAdministerField()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2893–2930 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2893-L2930)
- **Class:** [NodeAccessFieldTestCase](../NodeAccessFieldTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeAccessAdministerField()
```

## Documentation

```text
Tests administering fields when node access is restricted.
```

## Code

```php
  function testNodeAccessAdministerField() {
    // Create a page node.
    $langcode = LANGUAGE_NONE;
    $field_data = array();
    $value = $field_data[$langcode][0]['value'] = $this->randomName();
    $node = $this->drupalCreateNode(array($this->field_name => $field_data));

    // Log in as the administrator and confirm that the field value is present.
    $this->drupalLogin($this->admin_user);
    $this->drupalGet("node/{$node->nid}");
    $this->assertText($value, 'The saved field value is visible to an administrator.');

    // Log in as the content admin and try to view the node.
    $this->drupalLogin($this->content_admin_user);
    $this->drupalGet("node/{$node->nid}");
    $this->assertText('Access denied', 'Access is denied for the content admin.');

    // Modify the field default as the content admin.
    $edit = array();
    $default = 'Sometimes words have two meanings';
    $edit["{$this->field_name}[$langcode][0][value]"] = $default;
    $this->drupalPost(
      "admin/structure/types/manage/page/fields/{$this->field_name}",
      $edit,
      t('Save settings')
    );

    // Log in as the administrator.
    $this->drupalLogin($this->admin_user);

    // Confirm that the existing node still has the correct field value.
    $this->drupalGet("node/{$node->nid}");
    $this->assertText($value, 'The original field value is visible to an administrator.');

    // Confirm that the new default value appears when creating a new node.
    $this->drupalGet('node/add/page');
    $this->assertRaw($default, 'The updated default value is displayed when creating a new node.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
